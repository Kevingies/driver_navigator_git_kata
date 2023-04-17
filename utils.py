import pandas as pd
def pulltitanic():
    df = pd.read_csv("/Users/kevingiesen/Desktop/venv/driver_navigator_git_kata/data/titanic.csv")
    df['Sex'] = "Female"
    return df               
