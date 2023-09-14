import pandas as pd
oo=pd.read_csv('D:\CODING\PANDAS\data\olympics.csv',skiprows=4)
ath=oo.Athlete.sort_values()
print(ath)
new_ath=oo.sort_values(by=['Edition','Athlete'])
print(new_ath)

