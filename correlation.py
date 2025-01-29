import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
data = {
    "Study Hours":np.random.randint(1,10,50),
    "Test Score":np.random.randint(30,100,50),
    "Screen Time":np.random.randint(1,10,50),
    "Sleep Hours":np.random.randint(1,10,50),
    "Travelling":np.random.randint(1,10,50),
    "Exercise":np.random.randint(1,10,50)
}
df = pd.DataFrame(data)
df.head()

corr = df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr,annot=True,cmap='coolwarm',fmt=".2f",linewidths=0.5)
plt.show()