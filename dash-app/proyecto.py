import pandas as pd
import dash
import dash_bootstrap_components as dbc
import plotly.express as px

#Agregando base de datos
data = pd.read_csv('C:/Users/ale_v/OneDrive/Desktop/Nico/Proyectos/Examenes_estudiantes/Examenes_estudiantes/data/StudentsPerformance.csv')

#Añadiendo columna de promedios
data['promedio'] = data[['math score', 'reading score', 'writing score']].mean(axis=1).round(2)

#diseño con bootstrap 

###
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    brand = 'Dashboard de Estudiantes',
    children=[
        dash.html.A(
            'Fuente de datos',
            href='https://www.kaggle.com/datasets/spscientist/students-performance-in-exams',
            target='_blank',
            style={'color': 'white'}
        )
    ],
    fluid=True
)

#Creando Menu
menu = dash.html.Div(
    dash.dcc.Dropdown(
        id='menu',
        options=[
            {'label': 'Todos', 'value':'todos'},
            {'label': 'Mujer', 'value':'female'},
            {'label': 'Hombre', 'value':'male'}
        ],
        value='todos',
        clearable=False,
        searchable=False,
        style={'width': '95%', 'marginTop':'5px'}
    ),
    style={
        'display':'flex',
        'justify-content': 'center'
    }
)

cartas = dash.html.Div([
    dbc.Row([
        dbc.Col(
        dbc.Card([
            dash.html.H4('Matemáticas'),
            dash.html.H5(id='promedio_mat')
        ],body=True, id='card_mat')
        ),
        dbc.Col(
            dbc.Card([
                dash.html.H4('Lectura'),
                dash.html.H5(id='promedio_lec')
            ],body=True, id='card_lec')
        ),
        dbc.Col(
            dbc.Card([
                dash.html.H4('Escritura'),
                dash.html.H5(id='promedio_esc')
            ],body=True, id='card_esc')
        ),
    ]
        
    )
], style={'marginTop': '20px', 'marginLeft': '20px', 'marginRight': '20px'})



app.layout = dash.html.Div([
    dbc.Row(navbar),
    dbc.Row(menu),
])

if __name__ == '__main__':
    app.run(debug=True)
