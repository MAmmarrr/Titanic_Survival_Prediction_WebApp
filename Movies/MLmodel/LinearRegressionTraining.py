import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.preprocessing import LabelEncoder
import joblib

classifierSVC = SVC(kernel = 'rbf')
classifierLR = LogisticRegression()
classifierTree = DecisionTreeClassifier()
classifierLinear = LinearRegression()
df = pd.read_csv(r'Movies\MLmodel\train.csv')

df['Fare'].fillna(df['Fare'].dropna().median(), inplace=True)
df['Age'].fillna(df['Age'].dropna().median(), inplace=True)

df.loc[df["Sex"]== "male", "Sex"] = 0
df.loc[df["Sex"]== "female", "Sex"] = 1
df.loc[df["Embarked"] == "S", "Embarked"] = 0
df.loc[df["Embarked"] == "C", "Embarked"] = 1
df.loc[df["Embarked"] == "Q", "Embarked"] = 2
df.dropna(subset = ["Embarked"], inplace =True)



df["Sex"].dropna(inplace=True)
df["Age"].dropna(inplace = True)
df['Embarked'].dropna(inplace=True)
df['Cabin'].dropna(inplace=True)

dftsting = pd.read_csv(r'Movies\MLmodel\test.csv')

dftsting['Fare'].fillna(dftsting['Fare'].dropna().median(), inplace=True)
dftsting['Age'].fillna(dftsting['Age'].dropna().median(), inplace=True)


dftsting.loc[dftsting["Sex"]== "male", "Sex"] = 0
dftsting.loc[dftsting["Sex"]== "female", "Sex"] = 1
dftsting.loc[dftsting["Embarked"] == "S", "Embarked"] = 0
dftsting.loc[dftsting["Embarked"] == "C", "Embarked"] = 1
dftsting.loc[dftsting["Embarked"] == "Q", "Embarked"] = 2

X_testing = dftsting.drop(['PassengerId','Name', 'Ticket','Cabin'],axis=1)

X = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin','Survived'], axis = 1)
y = df['Survived']

one_hot_cols = X.columns.tolist()
df_bin_enc = pd.get_dummies(X, columns = one_hot_cols)
df_bin_enc.head()

df_con_enc = X.apply(LabelEncoder().fit_transform)
df_con_enc.head()


X_train, X_test, y_train, y_test = train_test_split(
    df_con_enc,
    y,
    test_size = .20,
    random_state = 8
)


classifierTree.fit(X_train,y_train)
y_pred = classifierTree.predict(X_test)

joblib.dump(classifierTree,'DecisionTreeClassifier.pk1')
