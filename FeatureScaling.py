#with min max scaler
import pandas as pandas
from sklearn.preprocessing import MinMaxScaler

# Sample dataset with multiple features 
data = {
    "age": [25, 30, 35, 40, 45],
    "height" : [150, 160, 170, 180, 190],
    "weight": [50, 60, 70, 80, 90],
    }

df=pd.DataFrame(data)
print(f"Original DataFrame: {df}")

scaler=MinMaxScaler()
normalized_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data,columns=df.columns)
print(f"Normalized DataFrame:\n {normalized_df}")


#StandardScaler
import pandas as pandas
from sklearn.preprocessing import StandardScaler

# Sample dataset with multiple features 
data = {
    "age": [25, 30, 35, 40, 45],
    "height" : [150, 160, 170, 180, 190],
    "weight": [50, 60, 70, 80, 90],
    }

df=pd.DataFrame(data)
print(f"Original DataFrame: {df}")

scaler=StandardScaler()
normalized_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data,columns=df.columns)
print(f"Normalized DataFrame:\n {normalized_df}")