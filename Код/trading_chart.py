import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from typing import Tuple, Optional, List

class TradingChart:
    """
    Клас TradingChart для візуалізації даних з акціями із використанням блоців ордерів за допомогою Plotly.
    """

    def __init__(self, stock_symbol: str, start_date: str, end_date: str, range_value: int = 15,
                 show_pd: bool = False, show_bearish_bos: bool = False, show_bullish_bos: bool = False,
                 bearish_ob_color: str = 'rgba(255, 0, 0, 0.9)', bullish_ob_color: str = 'rgba(0, 255, 0, 0.9)',
                 bos_candle_color: str = 'yellow', bullish_trend_color: str = 'lime', bearish_trend_color: str = 'red'):
        """
        Ініціалізує об'єкт TradingChart.

        Параметри:
        - `stock_symbol`: Символ акції (наприклад, 'AAPL').
        - `start_date`: Початкова дата для отримання даних про акцію у форматі 'YYYY-MM-DD'.
        - `end_date`: Кінцева дата для отримання даних про акцію у форматі 'YYYY-MM-DD'.
        - `range_value`: Значення для розрахунків (за замовчуванням - 15).
        - `show_pd`: Логічне значення для відображення чи приховання PD ліній на графіку (за замовчуванням - False).
        - ... (інші параметри)
        """
        self.stock_symbol = stock_symbol
        self.start_date = start_date
        self.end_date = end_date
        self.range_value = range_value
        self.show_pd = show_pd
        self.show_bearish_bos = show_bearish_bos
        self.show_bullish_bos = show_bullish_bos
        self.bearish_ob_color = bearish_ob_color
        self.bullish_ob_color = bullish_ob_color
        self.bos_candle_color = bos_candle_color
        self.bullish_trend_color = bullish_trend_color
        self.bearish_trend_color = bearish_trend_color

        self.last_down_index = 0
        self.last_down = 0
        self.last_low = 0
        self.last_up_index = 0
        self.last_up = 0
        self.last_up_low = 0
        self.last_up_open = 0
        self.last_high = 0
        self.last_bull_break_low = 0

        self.structure_low_index = 0
        self.structure_low = 1000000

        self.long_boxes: List[Tuple[float, float, float, float]] = []
        self.short_boxes: List[Tuple[float, float, float, float]] = []
        self.bos_lines: List[Tuple[float, float, float, float]] = []

        self.stock_data = yf.download(stock_symbol, start=start_date, end=end_date, interval='1d', timeout=30)
        self.fig = go.Figure()

    def structure_low_index_pointer(self, data: pd.DataFrame, length: int) -> Optional[pd.Timestamp]:
        """
        Розраховує та повертає індекс найменшої точки структури.

        Параметри:
        - `data`: Pandas DataFrame з даними про акцію.
        - `length`: Довжина вікна для розрахунку мінімуму.

        Повертає:
        - pd.Timestamp або None, якщо виникає помилка.
        """
        try:
            minValue = data['Low'].rolling(window=length).min().shift(1)
            minIndex = minValue.idxmin()
            return minIndex
        except pd.errors.IntCastingNaNError:
            return None

    def add_long_box(self, box: Tuple[float, float, float, float]) -> None:
        """
        Додає довгий блок на графік.

        Параметри:
        - `box`: Кортеж, який представляє координати блока (x0, x1, y0, y1).
        """
        self.fig.add_shape(type="rect",
                           x0=box[0], y0=box[2],
                           x1=box[1], y1=box[3],
                           line=dict(color=self.bullish_ob_color),
                           fillcolor=self.bullish_ob_color)

    def add_short_box(self, box: Tuple[float, float, float, float]) -> None:
        """
        Додає короткий блок на графік.

        Параметри:
        - `box`: Кортеж, який представляє координати блока (x0, x1, y0, y1).
        """
        self.fig.add_shape(type="rect",
                           x0=box[0], y0=box[2],
                           x1=box[1], y1=box[3],
                           line=dict(color=self.bearish_ob_color),
                           fillcolor=self.bearish_ob_color)

    def add_bos_line(self, line: Tuple[float, float, float, float], color: str) -> None:
        """
        Додає лінію Buy/Sell (BOS) на графік.

        Параметри:
        - `line`: Кортеж, який представляє координати лінії (x0, x1, y0, y1).
        - `color`: Колір лінії.
        """
        self.fig.add_trace(go.Scatter(x=[line[0], line[2]],
                                      y=[line[1], line[3]],
                                      mode='lines',
                                      line=dict(color=color, width=2)))

    def plot_chart(self) -> None:
        """
        Виводить графік торгів з блоками ордерів за допомогою Plotly.
        """
        self.fig.add_trace(go.Candlestick(x=self.stock_data.index,
                                          open=self.stock_data['Open'],
                                          high=self.stock_data['High'],
                                          low=self.stock_data['Low'],
                                          close=self.stock_data['Close'],
                                          name='Candlestick'))

        if self.show_bearish_bos or self.show_bullish_bos:
            for line in self.bos_lines:
                color = 'red' if self.show_bearish_bos else 'green'
                self.add_bos_line(line, color)

        for box in self.long_boxes:
            self.add_long_box(box)

        for box in self.short_boxes:
            self.add_short_box(box)

        if self.show_pd:
            PDH = 120
            PDL = 90

            self.fig.add_shape(type="line",
                               x0=self.stock_data.index.min(), y0=PDH,
                               x1=self.stock_data.index.max(), y1=PDH,
                               line=dict(color='blue', dash='dash'),
                               name='PDH')

            self.fig.add_shape(type="line",
                               x0=self.stock_data.index.min(), y0=PDL,
                               x1=self.stock_data.index.max(), y1=PDL,
                               line=dict(color='blue', dash='dash'),
                               name='PDL')

        self.fig.update_layout(title=f'Графік торгів з блоками ордерів - {self.stock_symbol}',
                               xaxis_title='Часовий штамп',
                               yaxis_title='Ціна',
                               xaxis_rangeslider_visible=False,
                               legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                               showlegend=True)

        self.fig.show()

# Приклад використання:
stock_symbol = 'AAPL'
start_date = '2023-06-03'
end_date = '2023-08-8'

trading_chart = TradingChart(stock_symbol, start_date, end_date)
trading_chart.plot_chart()
