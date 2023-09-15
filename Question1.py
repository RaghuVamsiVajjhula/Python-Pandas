# Which 3 Countries have won the most medals in recent years from 1984 to 2008

import pandas as pd
oo=pd.read_csv('D:\CODING\PANDAS\data\olympics.csv',skiprows=4)
data1=oo[oo.Edition>=1984]
print(data1)
#From above we get the values of Edition which are Greater than 1984
data2=data1.NOC.value_counts()
print(data2)
#From above code we can get the data number of medals won by country because NOC is country

data3=data1.NOC.value_counts().head(3)
print(data3)
#From here we get the top three countries which won more no of medals.

