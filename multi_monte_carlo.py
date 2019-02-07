# Monte Carlo Randomwalk price evolution

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas_datareader import data

# download Apple price data into DataFrame
apple = data.DataReader('AAPL', 'yahoo', start='1/1/2000')

# calculate the compound annual growth rate (CAGR) which
# will give us our mean return input (mu)
days = (apple.index[-1] - apple.index[0]).days
cagr = (((apple['Adj Close'][-1]) / apple['Adj Close'][1]) ** (365.0 / days)) - 1
print('CAGR =', str(round(cagr, 4)*100)+"%")
mu = cagr

# create a series of percentage returns and calculate
# the annual volatility of returns
apple['Returns'] = apple['Adj Close'].pct_change()
vol = apple['Returns'].std() * np.sqrt(252)
print("Annual Volatility =", str(round(vol, 4)*100)+"%")

# As of Wed 6th Feb 2019
# compound annual growth rate is : 25.0%
#  volatility is : 41.01%

# set up empty list to hold our ending values for each simulated price series
result = []

# Define Variables
S = apple['Adj Close'][-1]  # Starting stock price - last available real stock price
T = 252  # Number of Trading Days
mu = 0.25
vol = 0.4101  # Volatility

# choose number of runs to simulate - I have chosen 1000
for i in range(1000):
    # create list of daily returns using random normal distribution
    daily_returns = np.random.normal(mu/T, vol/math.sqrt(T), T)+1

    # set starting price and create price series generated by above random daily returns
    price_list = [S]

    for x in daily_returns:
        price_list.append(price_list[-1]*x)

    # plot data from each individual run which we will plot at the end
    plt.plot(price_list)

    # append the ending value of each simulated run to the empty list we created at the beginning
    result.append(price_list[-1])


# show the plot of multiple price series created above
plt.show()

# create Histogram of ending day stock value for the 10000 simulations run
plt.hist(result, bins=50)
plt.show()
