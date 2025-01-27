import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = {
    'square_feet_area':[8500, 9600,np.nan,11250,np.nan,9950,14206,np.nan,13830,11500],
    'Year_built':[2003,1976,2001,np.nan,1998,2000,2006,2005,1950,np.nan],
    'over_all_condition':[5,4,3,5,np.nan,4,5,4,np.nan,3],
    'ready_to_move':['Yes','No','Yes','Yes','No',np.nan,'Yes','No',np.nan,'Yes'],
    'Sale_price':[200000,180000,210000,215000,89000,21999,89787,12345,89237,560000]
}
numeric_columns = SimpleImputer(strategy='mean')
d=SimpleImputer(strategy='most_frequent')
df = pd.DataFrame(data)
df['square_feet_area'] = numeric_columns.fit_transform(df[['square_feet_area']])
df['over_all_condition']=numeric_columns.fit_transform(df[['over_all_condition']])
df['Year_built']=numeric_columns.fit_transform(df[['Year_built']])
df['ready_to_move']=d.fit_transform(df[['ready_to_move']]).ravel()
print(df)




import pandas as pd
import numpy as np
data = {
    'square_feet_area':[8500, 9600,np.nan,11250,np.nan,9950,14206,np.nan,13830,11500],
    'Year_built':[2003,1976,2001,np.nan,1998,2000,2006,2005,1950,np.nan],
    'over_all_condition':[5,4,3,5,np.nan,4,5,4,np.nan,3],
    'ready_to_move':['Yes','No','Yes','Yes','No',np.nan,'Yes','No',np.nan,'Yes'],
    'Sale_price':[200000,180000,210000,215000,89000,21999,89787,12345,89237,560000]
}

df= pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nDataFrame after handling missing values:")

df['square_feet_area'].fillna(df['square_feet_area'].mean(),inplace=True )
df['Year_built'].fillna(df['Year_built'].median(),inplace=True)
df['over_all_condition'].fillna(df['over_all_condition'].mean(),inplace=True)
df['ready_to_move'].fillna(df['ready_to_move'].mode()[0],inplace=True)
print(df)



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(10)
data = pd.DataFrame({
    'value':np.concatenate([np.random.normal(0,1,100),np.random.normal(10,1,100)])
})

Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3-Q1
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
outliers = data[(data['value']<lower_bound) | (data['value']>upper_bound)]
print(outliers)

plt.figure(figsize=(12,6))
sns.boxplot(x=data['value'])
plt.title('Box Plot of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
