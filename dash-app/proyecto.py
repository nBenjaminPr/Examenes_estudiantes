import pandas as pd
import dash
import dash_bootstrap_components as dbc
import plotly.express as px

#Agregando base de datos
data = pd.read_csv('C:/Users/ale_v/OneDrive/Desktop/Nico/Proyectos/Examenes_estudiantes/Examenes_estudiantes/data/StudentsPerformance.csv')

#Añadiendo columna de promedios
data['promedio'] = data[['math score', 'reading score', 'writing score']].mean(axis=1).round(2)
print(data)
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

#Creando Menu
menu= dash.html.Div(
    dash.dcc.Dropdown(
        id= "Menu",
        options= [
            {"label": "Todos", "value": "todos"},
            {"label": "Mujer", "value": "mujer"},
            {"label": "Hombre", "value": "hombre"}
        ],
        value= "todos",
        style= {"width": "95%", "marginTop": "5px"} 
    ),
    style= {
        "display": "flex",
        "justify-content": "center"
    }
)

app.layout = dash.html.Div([
    dbc.Row(navbar),
    dbc.Row(menu)
])

if __name__ == '__main__':
    app.run(debug=True)
