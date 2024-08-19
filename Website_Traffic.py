# -*- coding: utf-8 -*-
"""websiteTraffic.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rD-rwiBEJcZTJOkqTgcc0WFxZYywymFj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

df=pd.read_csv('/content/website_traffic.csv')

df.head()

df["Traffic Source"].unique()

df.info()

df.isnull().sum()

df.describe()

label=LabelEncoder()
df['Traffic Source']=label.fit_transform(df['Traffic Source'])

x=df.drop('Traffic Source',axis=1)
y=df['Traffic Source']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=45)

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print("Mean Squared Error",mean_squared_error(y_test,y_pred))
print("R2 Score",r2_score(y_test,y_pred))
print("RMSE",np.sqrt(mean_squared_error(y_test,y_pred)))

plt.scatter(y_test,y_pred)
plt.xlabel("Actual Traffic Source")
plt.ylabel("Predicted Traffic Source")

plt.figure(figsize=(10,5))
sns.heatmap(df.corr(),annot=True)

sns.pairplot(df)


