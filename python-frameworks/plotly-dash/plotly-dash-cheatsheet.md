# Plotly Dash Cheat Sheet

## Installation

```bash
pip install dash plotly
```

## Basic Dash App

```python
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Hello, Dash!")
])

if __name__ == "__main__":
    app.run(debug=True)
```

## Common HTML Components

```python
from dash import html

html.Div()
html.H1("Heading")
html.P("Paragraph")
html.Button("Click")
html.Br()
html.Img(src="image.png")
```

## Input Components

```python
from dash import dcc

dcc.Input(id="input", type="text")

dcc.Dropdown(
    options=[
        {"label": "Python", "value": "python"},
        {"label": "Java", "value": "java"}
    ],
    value="python"
)

dcc.Checklist(
    options=["A", "B", "C"],
    value=["A"]
)

dcc.RadioItems(
    options=["Yes", "No"],
    value="Yes"
)

dcc.Slider(
    min=0,
    max=100,
    step=5,
    value=50
)

dcc.Textarea()

dcc.DatePickerSingle()

dcc.Upload()

dcc.Store(id="store")
```

## Graphs

```python
from dash import dcc
import plotly.express as px

fig = px.scatter(
    x=[1,2,3],
    y=[4,5,6]
)

dcc.Graph(
    figure=fig
)
```

## App Layout

```python
app.layout = html.Div([
    html.H2("Dashboard"),
    dcc.Dropdown(id="dropdown"),
    dcc.Graph(id="graph"),
    html.Div(id="output")
])
```

## Callback

```python
from dash import Input, Output, callback

@callback(
    Output("output", "children"),
    Input("input", "value")
)
def update(value):
    return f"You entered: {value}"
```

## Multiple Inputs

```python
@callback(
    Output("output", "children"),
    Input("name", "value"),
    Input("age", "value")
)
def update(name, age):
    return f"{name} ({age})"
```

## Multiple Outputs

```python
@callback(
    Output("text", "children"),
    Output("graph", "figure"),
    Input("dropdown", "value")
)
def update(value):
    return "Updated", fig
```

## State

```python
from dash import State

@callback(
    Output("output", "children"),
    Input("button", "n_clicks"),
    State("input", "value")
)
def submit(clicks, text):
    return text
```

## Plotly Express Charts

```python
import plotly.express as px

px.line(df, x="x", y="y")

px.scatter(df, x="x", y="y")

px.bar(df, x="category", y="value")

px.histogram(df, x="value")

px.box(df, x="group", y="value")

px.pie(df, names="category", values="value")
```

## Graph Update Example

```python
@callback(
    Output("graph", "figure"),
    Input("dropdown", "value")
)
def update_chart(value):
    fig = px.bar(df, x="Category", y=value)
    return fig
```

## Data Table

```python
from dash import dash_table

dash_table.DataTable(
    data=df.to_dict("records"),
    columns=[
        {"name": i, "id": i}
        for i in df.columns
    ]
)
```

## Styling

```python
html.Div(
    children=[
        html.H1("Dashboard")
    ],
    style={
        "textAlign": "center",
        "padding": "20px",
        "backgroundColor": "#f4f4f4"
    }
)
```

## Bootstrap Support

```bash
pip install dash-bootstrap-components
```

```python
import dash_bootstrap_components as dbc
from dash import Dash

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
```

## Common Callback Imports

```python
from dash import (
    Input,
    Output,
    State,
    callback
)
```

## Project Structure

```text
project/
│── app.py
│── assets/
│   ├── style.css
│   └── logo.png
│── data/
│── requirements.txt
```

## Assets Folder

Files in the `assets/` folder are automatically loaded:

```text
assets/
│── style.css
│── script.js
│── image.png
```

## Useful Commands

```bash
pip install dash
pip install plotly
pip freeze > requirements.txt
python app.py
```

## Common Components

| Component              | Purpose                |
| ---------------------- | ---------------------- |
| `html.Div`             | Container              |
| `html.H1`              | Heading                |
| `html.P`               | Paragraph              |
| `html.Button`          | Button                 |
| `dcc.Input`            | Text input             |
| `dcc.Dropdown`         | Dropdown menu          |
| `dcc.Graph`            | Plotly chart           |
| `dcc.Slider`           | Slider                 |
| `dcc.Checklist`        | Multiple selection     |
| `dcc.RadioItems`       | Single selection       |
| `dash_table.DataTable` | Interactive table      |
| `dcc.Store`            | Store client-side data |
