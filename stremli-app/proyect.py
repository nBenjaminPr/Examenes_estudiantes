import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = pd.read_csv('C:/Users/ale_v/OneDrive/Desktop/Nico/Proyectos/Examenes_estudiantes/Examenes_estudiantes/data/StudentsPerformance.csv')
data['promedio'] = data[['math score', 'reading score', 'writing score']].mean(axis=1).round(2)

def clasificar_nivel(promedio):
    if promedio >= 90:
        return 'Alto'
    elif promedio >= 70:
        return 'Medio'
    else:
        return 'Bajo'
    
print(data)