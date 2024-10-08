# -*- coding: utf-8 -*-
"""RandomForestRegressor.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rD-rwiBEJcZTJOkqTgcc0WFxZYywymFj
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score

# Define features and target
x = df.drop('Salary', axis=1)
y = df['Salary']

# Feature Scaling
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

# Train the model
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(x_train, y_train)

# Predict the test set results
y_pred = rf_model.predict(x_test)

# Calculate and print performance metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
accuracy_score = accuracy_score(y_test, y_pred)
print("Random Forest Regressor Mean Squared Error:", mse)
print("Random Forest Regressor R^2 Score:", r2)
print(accuracy_score )

# Plot the predictions vs the actual values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted (Random Forest Regressor)')
plt.show()