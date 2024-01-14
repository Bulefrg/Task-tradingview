ей репозиторій містить клас TradingChart, який дозволяє створювати та візуалізувати торговий графік з використанням фінансових даних. Графік включає свічки, зелені та червоні блоки замовлень (Order Blocks), а також лінії Breakout Swing (BOS). Клас використовує бібліотеки pandas, plotly, та yfinance.

Встановлення
Для використання цього класу потрібно встановити необхідні бібліотеки. Використовуйте команди:

bash
Copy code
pip install pandas
pip install plotly
pip install yfinance
Використання
Простий приклад використання класу TradingChart:

python
Copy code
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf

# Ваші налаштування для stock_symbol, start_date, end_date

trading_chart = TradingChart(stock_symbol, start_date, end_date)
trading_chart.plot_chart()
Параметри класу TradingChart
stock_symbol: Символ фінансового інструменту (наприклад, 'AAPL').
start_date: Початкова дата аналізу графіка у форматі 'YYYY-MM-DD'.
end_date: Кінцева дата аналізу графіка у форматі 'YYYY-MM-DD'.
range_value (за замовчуванням 15): Значення для аналізу структур низьких цін.
show_pd (за замовчуванням False): Відображати рівні PDH та PDL на графіку.
show_bearish_bos (за замовчуванням False): Відображати лінії BOS для bearish тенденцій.
show_bullish_bos (за замовчуванням False): Відображати лінії BOS для bullish тенденцій.
Інші параметри: Кольори та стилі для різних елементів графіку.
Методи класу TradingChart
plot_chart(): Відображає торговий графік з врахуванням усіх вказаних параметрів.
Приклад використання
python
Copy code
stock_symbol = 'AAPL'
start_date = '2023-06-03'
end_date = '2023-08-8'

trading_chart = TradingChart(stock_symbol, start_date, end_date)
trading_chart.plot_chart()
Додаткова інформація
Цей проект є частиною відбору на стажування в компанії Daitex. Він використовує бібліотеки та технічні підходи, які широко використовуються в реальному світі розробки торгових роботів та фінансового аналізу на мові програмування Python.
