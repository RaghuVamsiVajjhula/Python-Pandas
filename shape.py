import pandas as pd
oo=pd.read_csv('D:\CODING\PANDAS\data\olympics.csv',skiprows=4)
print("Now we can get the shape of the csv file:")
shape_of_file=oo.shape
print(shape_of_file)
