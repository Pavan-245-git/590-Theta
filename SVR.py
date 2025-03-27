# -*- coding: utf-8 -*-
"""SVR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xZ32royZ8tp5E22ebAvr4UOl4K2t1hv-
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

filepath = r'/content/pima-indians-diabetes.data.csv'
column_names = ['Pregnancies', 'Glucosse', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv(filepath, header=None, names=column_names)

"""print(data.head())

"""

X = data.drop('Outcome', axis=1)
y = data['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svr = SVR()

param_grid = {
    'C': [0.1, 1, 10],
    'gamma': [ 0.01, 0.1, 1],
    'kernel': ['linear', 'rbf']
}

grid_search = GridSearchCV(estimator=svr, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best cross-validation score(negative MSE):", grid_search.best_score_)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error on test set:",mse)

