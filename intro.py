import pandas as pd
#oo=pd.read_csv('D:\CODING\PANDAS\data\olympics.csv')
#print(oo)
#In above we get in an un recognised form

oo=pd.read_csv('D:\CODING\PANDAS\data\olympics.csv',skiprows=4)
print(oo)
#Now we can read the data.

