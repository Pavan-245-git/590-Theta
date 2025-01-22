#Task 1
import matplaotlib.pyplot as plt

data = [5, 7, 7, 8, 9, 10, 10, 10, 11, 12,11,11]

plt.hist(data, bins=10, edgecolor='black')

plt,title('Simple Histogram Example')
plt.xlabel('Numbers')
plt.ylable('Count')
plt.show()


#Task 2
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
datf = pd.DataFrame({"Season 4": [5, 7, 4, 6, 3],
                     "Season 6": [8, 12, 3, 45, 5],
                     "Season 7": [12, 7, 4, 5, 6]})
p = sns.histplot(data=datf)
p.set(xlabel="X Label Value", ylabel = "Y Label Value")
plt.show()


#Task 3
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2)
data = np.random.randint(20, 81, 1000)

plt.hist(data, bins=15, edgecolor='black', color='skyblue')

plt.title('Histogram of Cancer Patience Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Patients')