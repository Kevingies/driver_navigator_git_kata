import pandas as pd
def pulltitanic():
    df = pd.read_csv("/Users/richardsihombing/driver_navigator_git_kata/data/titanic.csv")
    df['Sex'] = "male"
    return df               
