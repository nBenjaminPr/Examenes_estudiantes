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

#Creando Cartas
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

#Creando Graficos
grafico = dash.html.Div(dash.dcc.Graph(id="grafico_barras"))

@app.callback(
    dash.Output('promedio_mat', 'children'),
    dash.Output('promedio_lec', 'children'),
    dash.Output('promedio_esc', 'children'),
    dash.Output('promedio_esc', 'grafico_barras'),
    dash.Input('menu', 'value')
)

def update_dashboard(value):
    data_filtrada = data if value == 'todos' else data[data['gender'] == value]

    promedio_mat = data_filtrada['math score'].mean().round(2)
    promedio_lec = data_filtrada['reading score'].mean().round(2)
    promedio_esc = data_filtrada['writing score'].mean().round(2)

    promedio_por_nivel = data_filtrada.groupby('parental level of education', as_index=False)[['math score', 'reading score', 'writing score']].mean()
    promedio_por_nivel['promedio_general'] = promedio_por_nivel[['math score', 'reading score', 'writing score']].mean(axis=1).round(2)

    grafico_barras = px.bar(
        promedio_por_nivel,
        x='parental level of education',
        y='promedio_general',
        title='Promedio por nivel educativo de los padres',
        labels={
            'parental level of education': 'Nivel educativo de los padres',
            'promedio_general':'Promedio de los examenes'
        }
    )
        

    return promedio_mat, promedio_lec, promedio_esc, grafico_barras


app.layout = dash.html.Div([
    dbc.Row(navbar),
    dbc.Row(menu),
    dbc.Row(cartas),
    dbc.Row(grafico)
])

if __name__ == '__main__':
    app.run(debug=True)
