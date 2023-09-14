import pandas as pd
oo=pd.read_csv('D:\CODING\PANDAS\data\olympics.csv',skiprows=4)
print("The head of the file will be:") 
head_of_file=oo.head
print(head_of_file)
#We get the top 5 elements of data 

print("The tail of the file will be:") 
tail_of_file=oo.tail
print(tail_of_file)
#We get the bottom 5 elements of data

print("The information of the file is :")
info_file=oo.info
print(info_file)
