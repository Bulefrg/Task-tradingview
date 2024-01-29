README.md
# Графік торгів з блоками ордерів

Цей Python скрипт надає клас TradingChart для візуалізації даних з акціями із використанням блоців ордерів за допомогою бібліотеки Plotly.

## Встановлення

1. Встановіть необхідні пакети за допомогою наступної команди:

```bash
pip install -r requirements.txt
Використання
python
Copy code
# Приклад використання:
from trading_chart import TradingChart

stock_symbol = 'BTC-USD'
start_date = '2023-06-03'
end_date = '2023-08-8'

trading_chart = TradingChart(stock_symbol, start_date, end_date)
trading_chart.plot_chart()
Клас: TradingChart
Методи
__init__(self, stock_symbol: str, start_date: str, end_date: str, range_value: int = 15, show_pd: bool = False, ...) -> None:
Ініціалізує об'єкт TradingChart.

stock_symbol: Символ акції (наприклад, 'BTC-USD').
start_date: Початкова дата для отримання даних про акцію у форматі 'YYYY-MM-DD'.
end_date: Кінцева дата для отримання даних про акцію у форматі 'YYYY-MM-DD'.
range_value: Значення для розрахунків (за замовчуванням - 15).
show_pd: Логічне значення для відображення чи приховання PD ліній на графіку (за замовчуванням - False).
... (інші параметри)
structure_low_index_pointer(self, data: pd.DataFrame, length: int) -> Optional[pd.Timestamp]:
Розраховує та повертає індекс найменшої точки структури.

data: Pandas DataFrame з даними про акцію.
length: Довжина вікна для розрахунку мінімуму.
add_long_box(self, box: Tuple[float, float, float, float]) -> None:
Додає довгий блок на графік.

box: Кортеж, який представляє координати блока (x0, x1, y0, y1).
add_short_box(self, box: Tuple[float, float, float, float]) -> None:
Додає короткий блок на графік.

box: Кортеж, який представляє координати блока (x0, x1, y0, y1).
add_bos_line(self, line: Tuple[float, float, float, float], color: str) -> None:
Додає лінію Buy/Sell (BOS) на графік.

line: Кортеж, який представляє координати лінії (x0, x1, y0, y1).
color: Колір лінії.
plot_chart(self) -> None:
Виводить графік торгів з блоками ордерів за допомогою Plotly.

Приклад Використання

# Приклад використання:
stock_symbol = 'BTC-USD'
start_date = '2023-06-03'
end_date = '2023-08-8'

trading_chart = TradingChart(stock_symbol, start_date, end_date)
trading_chart.plot_chart()
