#TASK1
#Aayush jain sethia
import pandas as pd
from sklearn.model_selection import train_test_split
Data = pd.read_csv("student_scores.csv")
X=Data.iloc[:,:-1].values
y=Data.iloc[:,1].values
X_train, X_test, y_train, y_test= train_test_split(X, y,train_size=0.80,test_size=0.20,random_state=0)
from sklearn.linear_model import LinearRegression
linearRegressor= LinearRegression()
linearRegressor.fit(X_train, y_train)
y_predict= linearRegressor.predict(X_train)
reg= LinearRegression()  
reg.fit(X_train, y_train)
pred= reg.predict([[9.25]])
print("prediction is ",pred)
