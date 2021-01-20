
def encode_input(X_move):

    X_move.dropna(axis = 1, inplace=True)
    X_move.loc[X_move["Sex"]== "male", "Sex"] = 0
    X_move.loc[X_move["Sex"]== "Male", "Sex"] = 0
    X_move.loc[X_move["Sex"]== "female", "Sex"] = 1
    X_move.loc[X_move["Sex"]== "Female", "Sex"] = 1
    X_move.loc[X_move["Embarked"] == 'S', "Embarked"] = 0
    X_move.loc[X_move["Embarked"] == 'C', "Embarked"] = 1
    X_move.loc[X_move["Embarked"] == 'Q', "Embarked"] = 2
    
    X_move['Sex'] = X_move['Sex'].astype(float)
    X_move['Parch'] = X_move['Parch'].astype(float)
    X_move['Fare'] = X_move['Fare'].astype(float)
    X_move['Embarked'] = X_move['Embarked'].astype(float)
    X_move['Pclass'] = X_move['Pclass'].astype(float)
    X_move['Age'] = X_move['Age'].astype(float)
    X_move['Fare'] = X_move['Fare'].astype(float)
    return X_move
