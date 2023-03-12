import pandas as pd
import matplotlib.pyplot as plt

with open("c:/Git/data_1_checks/Assets/nba.csv") as fp : 
    df = pd.read_csv(fp)
    df['Salary'].round(8)
    print(df.head())
    print(df.describe())
   
    x = df["Age"]   
    y = df["Salary"]

    plt.xlabel ('Age', fontsize = 18)
    plt.ylabel('Salary($)', fontsize = 16)
    plt.bar(x,y)
    plt.ticklabel_format(style='plain')
    plt.show()
