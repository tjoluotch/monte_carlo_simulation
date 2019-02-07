## Monte-Carlo Simulation in Python

### Description

A Random walk Monte-carlo simulation executed in python giving data insights on Apples stock price in the future. Results are adjusted for Annual volatility and annual growth rate.

### Insights from Data calculated using - `pandas_datareader`
- compound annual growth rate: 24.92% (both)
- Anual volatility: 41% (both)
- mean: $221.12 (`multi_monte_carlo.py`)
- 5% Quantile: $106.164 (`multi_monte_carlo.py`)
- 95% Quantile: $384.1995 (`multi_monte_carlo.py`)

#### Am I willing to risk  a 5% chance of ending up with a stock worth less than $106.16, in order to chase an expected return of 25%, giving an expected stock price of around $221.12

### Features
#### `monte_carlo.py`
- Calculated Compound annual growth rate using historical Apple Data from `pandas_datareader`-  24.92%: `monte_carlo.py` & `multi_monte_carlo.py`.
- Calculated annual volatility using historical Apple Data from `pandas_datareader` library-  41%:  `monte_carlo.py` & `multi_monte_carlo.py`.
- Implemented potential price series evolution over Trading year (252 days):
`monte_carlo.py` & `multi_monte_carlo.py`.
- Created a series of daily returns using random normal distribution from `numpy` library 
- Plotted these returns on a Chart and Histogram using `matplotlib.pyplot`
- #### Images generated in Graph_Charts/single simulation

#### `multi_monte_carlo.py`
- Calculated Compound annual growth rate using historical Apple Data from `pandas_datareader`-  24.92%: `monte_carlo.py` & `multi_monte_carlo.py`.
- Calculated annual volatility using historical Apple Data from `pandas_datareader` library-  41%:  `monte_carlo.py` & `multi_monte_carlo.py`.
- Implemented potential price series evolution over Trading year (252 days):
`monte_carlo.py` & `multi_monte_carlo.py`.
- plotted 10,000 random normal simulations using the `matplotlib.pyplot` 
- Created histogram representing end of day price simulation  `matplotlib.pyplot`
- Calculated and added quantile to Histogram using `numpy`.
- #### Images generated in Graph_Charts/single simulation/10000 simulations
