import dash
import dash_core_components as dcc
import dash_html_components as html
from index import plot1

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    children=[
        html.H1(children="Service Order Dashboard"),
        html.Div(),

        dcc.Graph(
            id = "graph 2",
            figure=plot1
        )
    ]
)






if __name__ == '__main__':
    app.run_server(debug=True)


