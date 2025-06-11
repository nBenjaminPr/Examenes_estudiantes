import pandas as pd
import dash
import dash_bootstrap_components as dbc
import plotly.express as px

#Agregando base de datos
data = pd.read_csv('C:/Users/Usuario/Desktop/Escriotrio Nico/PROYECTOS/Examenes de alumnos/data/StudentsPerformance.csv')


#Añadiendo columna de promedios
data['promedio'] = data[['math score', 'reading score', 'writing score']].mean(axis=1).round(2)

#diseño con bootstrap 

###
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    brand= "Dashboard de estudiantes",
    children=[
        dash.html.A(
            'Fuente de datos',
            href='https://www.kaggle.com/datasets/spscientist/students-performance-in-exams',
            target= '_blank',
            style= {'color: white'}
        )
    ],
    fluid=True
)

app.layout = dash.html.Div([
    navbar,
])

if __name__ == '__main__':
    app.run(debug=True)
