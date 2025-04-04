import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create a sample dataset with some outlier
np.random.seed(10)
data =pd.DataFrame({
    "value":np.concatenate([np.random.normal(0,1,100), np.random.normal(10,1,10)])
})
#calculate the IQR for boc plot_based out
Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3 - Q1
#define utlier thresholds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

#identify outliers
outliers = data[(data['value']<lower_bound) | (data['value']>upper_bound)]
print(f"outliers based on box plot criteria:\n{outliers}")

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
sns.boxplot(x=data['value'])
plt.title("Box plot")