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
    
data['nivel'] = data['promedio'].apply(clasificar_nivel)

st.set_page_config(page_title='Calificaciones de los estudiantes', layout='wide')
st.title('Dashboard de rendimiento estudiantil')

with st.sidebar:
    genero = st.selectbox(
        'Seleccionar el género:',
        options=['Todos', 'female', 'male'],
        index=0
    )
    st.markdown('[Fuente de datos](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)')

data_filtrada = data if genero == 'Todos' else data[data['gender'] == genero]

col1, col2, col3 = st.columns(3)
col1.metric('Promedio Matemáticas', f"{data_filtrada['math score'].mean():.2f}")
col2.metric('Promedio Lectura', f"{data_filtrada['reading score'].mean():.2f}")
col3.metric('Promedio Escritura', f"{data_filtrada['writing score'].mean():.2f}")

st.subheader('Calificaciones por nivel educativo de los padres')
nivel_promedio = data_filtrada.groupby('parental level of education')['promedio'].mean().reset_index()
st.bar_chart(nivel_promedio, x='parental level of education', y='promedio')

col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader('Correlación entre calificaciones')
    fig_scatter = scatter_matrix(
        data[['math score', 'reading score', 'writing score']],
        diagonal='hist',
        color='teal'
    )
    st.pyplot(plt.gcf())

with col_der:
    st.subheader('Distribución por niveles')
    niveles = data['nivel'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(niveles, labels=niveles.index, autopct='%1.1f%%')
    st.pyplot(fig)