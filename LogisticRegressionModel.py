import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load or create your dataset
# for simplicity, let's create a sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Smoker': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'Outcome': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Split the dataset into features (X) and target variable (y)
X = df[['Age', 'Smoker']]
y = df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Calculate odds ratio for each feature
odds_ratio = np.exp(model.coef_)
print(f'Odds Ratio: {odds_ratio}')
