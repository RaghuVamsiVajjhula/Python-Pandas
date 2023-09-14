import pandas as pd
oo=pd.read_csv('D:\CODING\PANDAS\data\olympics.csv',skiprows=4)
print("Using value_counts()")
value=oo.Edition.value_counts()
print(value)
#The above code will help to count the number of Editions in the data set
print("THe value of gender count is:")
Gender_value=oo.Gender.value_counts()
print(Gender_value)
