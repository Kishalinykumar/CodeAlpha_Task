from flask import Flask, render_template, request, redirect, url_for
import yfinance as yf

app = Flask(__name__)

# In-memory portfolio
portfolio = []

@app.route('/')
def index():
    total_value = 0
    portfolio_data = []

    for stock in portfolio:
        ticker = yf.Ticker(stock['symbol'])
        stock_data = ticker.history(period="1d").iloc[-1]
        price = stock_data['Close']
        value = price * stock['quantity']
        total_value += value

        portfolio_data.append({
            'symbol': stock['symbol'],
            'quantity': stock['quantity'],
            'price': round(price, 2),
            'value': round(value, 2),
        })

    return render_template('index.html', portfolio=portfolio_data, total_value=round(total_value, 2))

@app.route('/add', methods=['POST'])
def add_stock():
    symbol = request.form['symbol'].upper()
    quantity = int(request.form['quantity'])

    for stock in portfolio:
        if stock['symbol'] == symbol:
            stock['quantity'] += quantity
            break
    else:
        portfolio.append({'symbol': symbol, 'quantity': quantity})

    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove_stock():
    symbol = request.form['symbol'].upper()
    global portfolio
    portfolio = [stock for stock in portfolio if stock['symbol'] != symbol]

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
