import pandas as pd
oo=pd.read_csv('D:\CODING\PANDAS\data\olympics.csv',skiprows=4)
data1=oo.Athlete.str.contains('Florence')
print(data1)
#Above is the string handling case where we check where we have the name
#  Florence in the athlete data shows TRUE and the remaining shows False
