import pandas as pd
oo=pd.read_csv('D:\CODING\PANDAS\data\olympics.csv',skiprows=4)
print("The head of the file is:")
head_file=oo.head()
print(head_file)
#We get the top 5 elements of data.

print(oo.Medal=='Gold')
#We get True for all the medal list where we have Gold.

#We get Falso for all the medal where they get remaining medals other than Gold.

#Inorder to check the athletes who got gold we can follow the following steps.
list_data=oo[oo.Medal=='Gold']
print(list_data)

#In order to add another condition where we need information only about women:
new_list_Data=oo[(oo.Medal=='Gold')&(oo.Gender=='Women')]
print(new_list_Data)
#in the above code we can get the data of women who got their Gold medal.
