import statistics
import numpy as np

stock_prices = [100, 102, 98, 105, 101, 97, 99, 104, 100, 98]

variance = statistics.variance(stock_prices)
print(f"Variance of stock prices: {variance}")

numpy_variance = np.var(stock_prices, ddof=1)
print(f"Variance of stock prices: {numpy_variance} ")



import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

data = { 
    'Temperature':[22,25,20,18,21,19,24,26,23,27,38,30,31,32,34,35,23,15,1214,24,23,20,19,18,23,18,25,28,29],
    'Humidity': [65,60,72,78,70,75,80,68,69,73,59,64,79,75,62,68,66,71,73,70,62,65,64,63,65],
    'Wind Speed': [15,10,20,25,12,14,18,22,11,19],
    'Pressure': [1015,1012,1017,1014,1013,1016,1011,1018,1015,1013]
}

df = pd.DataFrame(data)

plt.figure(figsize(8,6))
plt.scatter(df['Stock_A_Returns'], df['Stock_B_Returns'], color'blue', label='Returns Comparison')

plt.title('Stock A vs Stock B Returns', fontsize=14)
plt.xlabel('Stock A Returns', fontsize=12)
plt.ylabel('Stock B Returns', fontsize=12)
plt.grid(True)
plt.legend()
sns.pairplot(df)

plt.show()