# -*- coding: utf-8 -*-
"""WarrantyClaim-Proj.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ae3_z-srRm689M5fV7pmdfOjHebYNzoJ
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import pickle

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
from google.colab import files
uploaded=files.upload()
file_name = list(uploaded.keys())[0]
df=pd.read_csv(file_name)
print(df.head(20))

df.head()

df.info()

print(df.describe())
print("Missing Values:\n", df.isnull().sum())

pd.isnull(df)

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
df['State'] = LE.fit_transform(df['State'])
df['Consumer_profile'] = LE.fit_transform(df['Consumer_profile'])
df

df=pd.get_dummies(df)
df

df.corr(numeric_only=True)

import statsmodels.formula.api as smf
model=smf.ols('Claim_Value~State+AC_1001_Issue++Service_Centre+Consumer_profile+Product_Age+Product_type_Microwave+Call_details',data=df).fit()

import matplotlib.pyplot as plt
plt.scatter(df['State'],df['Claim_Value'])
plt.scatter(df['AC_1001_Issue'],df['Claim_Value'])
plt.scatter(df['Service_Centre'],df['Claim_Value'])
plt.scatter(df['Consumer_profile'],df['Claim_Value'])
plt.scatter(df['Product_Age'],df['Claim_Value'])
plt.scatter(df['Product_type_Microwave'],df['Claim_Value'])
plt.scatter(df['Call_details'],df['Claim_Value'])
plt.show()

pd.isnull(df).sum()

import pandas as pd
from sklearn.preprocessing import StandardScaler

# ... (other code)

# Define num_features before using it
num_features = ['Product_Age', 'Claim_Value', 'AC_1001_Issue', 'AC_1002_Issue',
                'TV_2001_Issue', 'TV_2002_Issue', 'TV_2003_Issue']

# Assuming data_encoded is a copy of df or created from df
data_encoded = df.copy()  # If data_encoded is not already created

# Now you can use num_features for scaling
scaler = StandardScaler()
data_encoded[num_features] = scaler.fit_transform(df[num_features])

Claim_value = [col for col in data_encoded.columns if 'Claim_Value' in col][0]

X = data_encoded.drop(columns=[Claim_value])
y = data_encoded[Claim_value]

print(data_encoded.columns)

print(data_encoded)

Claim_Value = [col for col in data_encoded.columns if 'Claim_Value' in col][0]
X = data_encoded.drop(columns=[Claim_Value])
y = data_encoded[Claim_Value].astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {'Logistic Regression': LogisticRegression(max_iter=1000000, solver='saga'),}

Claim_Value= [col for col in data_encoded.columns if 'Claim_Value' in col]
if Claim_Value:
    Claim_Value =Claim_Value[0]
    X_scaled = scaler.fit_transform(data_encoded.drop(columns=[Claim_Value]))
    data_encoded = pd.DataFrame(X_scaled, columns=data_encoded.drop(columns=[Claim_Value]).columns)
else:
    print("Claim Value not found in data_encoded!")

import pandas as pd
from sklearn.preprocessing import StandardScaler

# ... (other code)

# Define num_features, excluding 'Region'
num_features = ['Product_Age', 'Claim_Value', 'AC_1001_Issue', 'AC_1002_Issue',
                'TV_2001_Issue', 'TV_2002_Issue', 'TV_2003_Issue']

# Assuming data_encoded is a copy of df or created from df
data_encoded = df.copy()  # If data_encoded is not already created

# Now you can use num_features for scaling
# Select only numerical features for scaling
numerical_data = data_encoded[num_features]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_data)

# Update the original DataFrame with the scaled values
data_encoded[num_features] = scaled_data

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
file_path = "/content/Warranty_Claim_Dataset.csv"
data = pd.read_csv(file_path)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
for col in data.columns:
    if data[col].dtype == 'object':
        if not data[col].mode().empty:
            data[col].fillna(data[col].mode()[0], inplace=True)
    else:
        data[col].fillna(data[col].median(), inplace=True)

plt.figure(figsize=(12, 6))
sns.violinplot(data=data.select_dtypes(include=[np.number]), palette="coolwarm", inner=None)
sns.stripplot(data=data.select_dtypes(include=[np.number]), color='black', alpha=0.5, size=3, jitter=True)

plt.xticks(rotation=90)
plt.title("Data Distribution and Outlier Detection")
plt.show()

pd.isnull(df).sum()

for col in data.select_dtypes(include=[np.number]).columns:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]

print("Cleaned Dataset Shape:", data.shape)

plt.figure(figsize=(5, 5))
sns.boxplot(data=data.select_dtypes(include=[np.number]))
plt.xticks(rotation=90)
plt.title("Outlier Detection")
plt.show()

correlation = df['Claim_Value'].corr(df['Fraud'])
correlation

import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(x='Claim_Value',y='Fraud',data=df)

plt.title("correlation between CLAIM VALUE and FRAUD")
plt.xlabel("Claim Value")
plt.ylabel("Fraud")
plt.show()

correlation = df['Claim_Value'].corr(df['Product_Age'])
correlation

import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x='Claim_Value',y='Product_Age',data=df)
plt.title("correlation between CLAIM VALUE and PRODUCT AGE")
plt.xlabel("Claim Value")
plt.ylabel("Product Age")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file_path = "/content/Warranty_Claim_Dataset.csv"
df = pd.read_csv(file_path)

numerical_cols = df.select_dtypes(include=[np.number]).columns


correlation_matrix = df[numerical_cols].corr()


plt.figure(figsize=(6, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix of Numerical Features")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
file_path = "/content/Warranty_Claim_Dataset.csv"
df = pd.read_csv(file_path)

num_features = ['Product_Age', 'Fraud', 'AC_1001_Issue', 'AC_1002_Issue', 'TV_2001_Issue', 'TV_2002_Issue', 'TV_2003_Issue']
sns.pairplot(df[num_features])
plt.suptitle('Pair Plot of Warranty Claims Data', y=1, fontsize=16)
plt.show()

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

file_path = "/content/Warranty_Claim_Dataset.csv"
df = pd.read_csv(file_path)
# Select numerical features for scaling
num_features = ['Product_Age', 'Claim_Value', 'AC_1002_Issue', 'AC_1001_Issue', 'TV_2003_Issue', 'TV_2002_Issue', 'TV_2001_Issue']

# Handling missing values (Optional: Fill missing values with median)
df[num_features] = df[num_features].fillna(df[num_features].median())

df_standardized = df.copy()
df_normalized = df.copy()

# --- 1️⃣ Standardization (Z-score) ---
scaler_standard = StandardScaler()
df_standardized[num_features] = scaler_standard.fit_transform(df[num_features])

# --- 2️⃣ Min-Max Scaling (Normalization) ---
scaler_minmax = MinMaxScaler()
df_normalized[num_features] = scaler_minmax.fit_transform(df[num_features])

print("Original Data (First 5 rows):\n", df[num_features].head())
print("\nStandardized Data (First 5 rows):\n", df_standardized[num_features].head())
print("\nMin-Max Scaled Data (First 5 rows):\n", df_normalized[num_features].head())

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()


df['Claim_Value_Scaled'] = scaler.fit_transform(df_normalized[['Claim_Value']]) #df_normalized[num_features] # Assign back to DataFrame


print("\nBefore Scaling:")
print(df['Claim_Value'].describe())

print("\nAfter Scaling:")
print(df['Claim_Value_Scaled'].describe())

print("Before Scaling:")
print(df['Claim_Value'].describe())

print("\nAfter Scaling:")
print(df_normalized['Claim_Value'].describe())

print(df['Claim_Value'].nunique())
print(df['Claim_Value'].value_counts())

Claim_value = [col for col in data_encoded.columns if 'Claim_Value' in col][0]


X = data_encoded.drop(columns=[Claim_value])
y = data_encoded[Claim_value]

from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

file_path = "/content/Warranty_Claim_Dataset.csv"
df = pd.read_csv(file_path)

scaler = StandardScaler()

df["Claim_Value"]

from sklearn.metrics import mean_squared_error, r2_score
print("Mean Squared Error (MSE):", mse)
print("R-squared (r²):", r2)

import matplotlib.pyplot as plt
import statsmodels.api as sm
fig = plt.figure(figsize=(12,6))
fig = sm.graphics.plot_regress_exog(model, "AC_1001_Issue", fig=fig)
plt.show()

def get_standardized_values(vals):
  return (vals-vals.mean())/vals.std()

plt.scatter(get_standardized_values(model.fittedvalues),get_standardized_values(model.resid))

plt.title('Residual Plot')
plt.xlabel('Standardized Fitted Values')
plt.ylabel('Standardized Residuals values')
plt.show()

import matplotlib.pyplot as plot
import numpy as np
np.random.seed(60)
data= np.random.randint(20,88,100)
plt.hist(data, bins=15, edgecolor='brown', color='pink')
plt.title('Histograam of AC_1001_Issue')
plt.xlabel('State')
plt.ylabel('Product_type_AC')

plt.show()

import seaborn as sns
sns.distplot(df['AC_1001_Issue'])

print(dataframe[categorical_features].dtypes)

for column in categorical_features:
       dataframe[column] = dataframe[column].astype(str)

numerical_data = numerical_data.reset_index(drop=True)
encoded_data = encoded_data.reset_index(drop=True)

final_df = pd.concat([numerical_df, encoded_df], axis=1)

from sklearn.preprocessing import OneHotEncoder

# Assuming 'dataframe' is your Pandas DataFrame
categorical_features = dataframe.select_dtypes(include=['object']).columns
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')  # handle_unknown='ignore' for unseen values in test data
encoded_data = encoder.fit_transform(dataframe[categorical_features])

encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_features))
numerical_df = dataframe.select_dtypes(exclude=['object'])

# Combine numerical and encoded categorical features
final_df = pd.concat([numerical_df, encoded_df], axis=1)

X_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=40)

from pandas import read_csv
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

filename = r'/content/Warranty_Claim_Dataset.csv'
names = ['TV_2001_Issue', 'Service_Centre', 'Product_Age', 'AC_1002_Issue', 'TV_2002_Issue', 'Claim_Value', 'Call_details	', 'Fraud']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:, 0:6]
Y = array[:,4]

model=LogisticRegression(max_iter=400)
rfe = RFE(model,n_features_to_select=4)
fit = rfe.fit(X, Y)

# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd
# load data
filename = '/content/Warranty_Claim_Dataset.csv'
names = ['TV_2001_Issue', 'Service_Centre', 'Product_Age', 'AC_1002_Issue', 'TV_2002_Issue', 'Claim_Value', 'Call_details	', 'Fraud']
print(names)
#df = pd.read_csv(r"/content/Warranty_Claim_Dataset.csv")

dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:5]
Y = array[:,4]
# feature extraction
test = SelectKBest (score_func=chi2, k=4)
fit=test.fit(X, Y)
# summarize scores
print(fit.scores_)
features = fit.transform(X)
# summarize selected features
print(features[0:5,:])
set_printoptions (precision=3)
print(fit.scores_)
features = fit.transform(X)

from google.colab import drive
drive.mount('/content/drive')

file_name='/content/Warranty_Claim_Dataset.csv'

import pandas as pd
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
Warranty_Claim_Dataset=pd.read_csv(file_name)

Warranty_Claim_Dataset.info()

label_encoder=preprocessing.LabelEncoder()
Warranty_Claim_Dataset['product_category']=label_encoder.fit_transform(Warranty_Claim_Dataset['Product_category'])
Warranty_Claim_Dataset['Claim_Value']=label_encoder.fit_transform(Warranty_Claim_Dataset['Claim_Value'])

Warranty_Claim_Dataset['Claim_Value']
Warranty_Claim_Dataset['product_category']

label_encoder=preprocessing.LabelEncoder()
Warranty_Claim_Dataset['Claim_Value']=label_encoder.fit_transform(Warranty_Claim_Dataset['Claim_Value'])
Warranty_Claim_Dataset['Claim_Value']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=40)

model=DecisionTreeClassifier(criterion='entropy',max_depth=3)
model.fit(x_train,y_train)

tree.plot_tree(model);

x = Warranty_Claim_Dataset[['Claim_Value']]
y = Warranty_Claim_Dataset['AC_1001_Issue']
model=DecisionTreeClassifier(criterion='entropy',max_depth=3)
model.fit(x_train,y_train)

tree.plot_tree(model);

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

X_train.shape, y_train.shape

#linear Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

file_path = "/content/Warranty_Claim_Dataset.csv"
df = pd.read_csv(file_path)
print(df.head())

X = df[['Claim_Value']]
y = df['Product_type']
encoder = LabelEncoder()
X['Claim_Value'] = encoder.fit_transform(X['Claim_Value'])
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=38)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")
plt.scatter(X_test, y_test, color='blue', label="Actual Data")
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Regression Line")
plt.xlabel("Claim_Value (Encoded)")
plt.ylabel("Product_type (Encoded)")
plt.legend()
plt.title("Linear Regression Model")
plt.show()

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {
    "Purchased_from": ["Online Store", "Manufacturer", "Dealer", "Dealer"],
    "TV_2003_Issue": [1, 0, 0, 1],
    "Product_type": ["Refrigerator", "TV", "Microwave", "TV"],
    "State": ["Tamil Nadu", "Jharkhand", "Karnataka", "Haryana"],
    "Claim_Value": [18706, 46245, 12096, 9147 ]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

one_hot_encoder = OneHotEncoder(sparse_output=False)
columns_to_encode = ["Purchased_from", "TV_2003_Issue", "Product_type", "Claim_Value"]
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])
encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

print("\nOne_Hot Encoded DataFrame:")
print(encoded_df)

# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.feature_selection import chi2
import pandas as pd
from sklearn.model_selection import train_test_split

filename = '/content/Warranty_Claim_Dataset.csv'
names = ['Service_Centre', 'Product_Age', 'AC_1002_Issue', 'TV_2002_Issue', 'Claim_Value', 'Call_details	', 'Fraud']
print(names)

dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,4]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

test = SelectKBest (score_func=chi2, k=4)
fit=test.fit(X, Y)
print(fit.scores_)
features = fit.transform(X)

print(features[0:5,:])
set_printoptions (precision=3)
print(fit.scores_)
features = fit.transform(X)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

csv_file = '/content/Warranty_Claim_Dataset.csv'
df = pd.read_csv(csv_file)
print(df)
df.fillna(df.median(numeric_only=True), inplace=True)

X = df.drop(columns=['Claim_Value'])
y = df['Claim_Value']

categorical_features = X.select_dtypes(include=['object']).columns.tolist()
numerical_features = X.select_dtypes(include=[np.number]).columns.tolist()

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ])

X_processed = preprocessor.fit_transform(X)

selector = SelectKBest(score_func=f_regression, k='all')  # Select all features for now
X_selected = selector.fit_transform(X_processed, y)

selected_features = np.concatenate([numerical_features,preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features)])
selected_features = selected_features[selector.get_support()]

print("Selected Features:\n", selected_features)
print("Feature Scores:\n", selector.scores_)

final_df = pd.DataFrame(X_selected, columns=selected_features)
print("Final DataFrame with Selected Features:\n", final_df.head())

X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R² Score:", r2)

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy as np
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

filename = '/content/Warranty_Claim_Dataset.csv'
dataframe = read_csv(filename)

for col in dataframe.columns:
    if dataframe[col].dtype == 'object':

        mode_value = dataframe[col].mode()[0]
        dataframe[col] = dataframe[col].fillna(mode_value)
    else:

        median_value = dataframe[col].median()
        dataframe[col] = dataframe[col].fillna(median_value)

bagging_model = BaggingRegressor(estimator=DecisionTreeRegressor(), n_estimators=100, random_state=42)

seed = 7
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

results = cross_val_score(bagging_model, X_processed, y, cv=kfold, scoring='neg_mean_squared_error')
mean_mse = -results.mean()
print("Mean Squared Error from Cross-Validation:", mean_mse)

filename = '/content/Warranty_Claim_Dataset.csv'
dataframe = read_csv(filename)

import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score

model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) and R-squared (r²)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (r²):", r2)

from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

model = AdaBoostRegressor(estimator=DecisionTreeRegressor(max_depth=3), n_estimators=50, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) and R-squared (r²)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (r²):", r2)

from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

model = RandomForestRegressor()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) and R-squared (r²)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (r²):", r2)

import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
import xgboost as xgb
import numpy as np

csv_file = '/content/Warranty_Claim_Dataset.csv'
df = pd.read_csv(csv_file)

df.to_csv(csv_file, index=False)

# Flask App Deployment Code
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        claim_amount = float(request.form['claim_amount'])
        product_age = int(request.form['product_age'])
        customer_history = int(request.form['customer_history'])
        purchase_date = request.form['purchase_date']
        claim_date = request.form['claim_date']
        claim_reason = request.form['claim_reason']
        repair_cost = float(request.form['repair_cost'])
        warranty_validity = int(request.form['warranty_validity'])

        # Dummy prediction logic (Replace with actual ML model)
        prediction = "Fraudulent" if claim_amount > 5000 else "Genuine"

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '_main_':
    app.run(debug=True)

