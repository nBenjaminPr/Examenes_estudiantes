import pandas as pd

#Agregando base de datos
data = pd.read_csv('./data/StudentsPerformance.csv')

data['promedio'] = data[['math score', 'reading score', 'writing score']].mean(axis=1).round(2)

print (data)