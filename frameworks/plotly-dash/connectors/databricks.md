# Databricks conector to Python

Connecting a local Python Dash application to Databricks is a great way to build powerful, interactive dashboards backed by heavy-duty cloud data processing.

The most robust and modern way to do this is using the **Databricks SQL Connector for Python** (`databricks-sql-python`), which is optimized for fast data retrieval.

Here is a step-by-step guide to getting it up and running.

## Get Your Databricks Connection Details

Before writing Python code, you need a few pieces of information from your Databricks workspace.

1. **Server Hostname & HTTP Path:** * Go to your Databricks Workspace.
   - Navigate to **Compute** (or **SQL Warehouses** if you are using SQL Pro/Serverless).
   - Click on your cluster or warehouse, open the **Advanced Options**, and select the **JDBC/ODBC** tab.
   - Copy the **Server Hostname** and **HTTP Path**.
2. **Personal Access Token (PAT):**
   - Go to **User Settings** -> **Developer** -> **Access tokens** and click **Generate new token**. Copy it immediately.

## Install Required Packages

In your local Python environment, install Dash, Pandas, and the Databricks SQL connector:

```bash
pip install dash pandas databricks-sql-python
```

## Write the Dash Application

Create a file named `app.py`. We will use a standard Dash layout and pull data from Databricks inside a callback (or at startup, depending on your needs).

Python

```python
import dash
from dash import dcc, html, Input, Output
import pandas as pd
from databricks import sql
import plotly.express as px

# --- DATABRICKS CONNECTION CONFIG ---
# In production, use environment variables (e.g., os.environ.get(...))
DATABRICKS_SERVER_HOSTNAME = "your-workspace.cloud.databricks.com"
DATABRICKS_HTTP_PATH = "/sql/1.0/warehouses/your-warehouse-id"
DATABRICKS_TOKEN = "dapiYourPersonalAccessTokenHere"

def query_databricks(query_string):
    """Helper function to connect, execute a query, and return a Pandas DataFrame"""
    with sql.connect(
        server_hostname=DATABRICKS_SERVER_HOSTNAME,
        http_path=DATABRICKS_HTTP_PATH,
        access_token=DATABRICKS_TOKEN
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query_string)
            result = cursor.fetchall()
            # Get column names from the cursor description
            columns = [desc[0] for desc in cursor.description]
            return pd.DataFrame(result, columns=columns)

# --- DASH APP SETUP ---
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Databricks + Dash Local Connection"),
    html.Button("Fetch Data from Databricks", id="fetch-btn", n_clicks=0),
    dcc.Loading(
        id="loading-output",
        type="default",
        children=dcc.Graph(id="databricks-graph")
    )
])

# --- CALLBACK TO REFRESH DATA ---
@app.callback(
    Output("databricks-graph", "figure"),
    Input("fetch-btn", "n_clicks"),
    prevent_initial_call=True
)
def update_graph(n_clicks):
    # Example Query: Replace with your actual catalog, schema, and table
    query = """
        SELECT category, SUM(sales) as total_sales 
        FROM samples.nyctaxi.trips 
        GROUP BY category 
        LIMIT 10
    """
    
    # Fetch data into a pandas DataFrame
    df = query_databricks(query)
    
    # Create a Plotly figure
    fig = px.bar(df, x="category", y="total_sales", title="Sales by Category from Databricks")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
```

## Run it Locally

Execute your script from your terminal:

```
python app.py
```

Open your browser and navigate to `http://127.0.0.1:8050/`. Click the button, and Dash will securely query Databricks, pull down the data, and render your chart.

### Pro-Tips for Local Development

- **Security:** Never hardcode your Databricks PAT token directly into `app.py` if you plan to push this to GitHub. Use a `.env` file and the `python-dotenv` package to keep it secret.
- **Performance / Caching:** If your Databricks query takes a few seconds to run, dragging sliders or clicking buttons in Dash will feel sluggish. Use `flask_caching` or Dash's built-in `dcc.Store` to cache the data locally so you aren't hitting Databricks on every single mouse click.
- **Unity Catalog:** Ensure your connection token has `SELECT` permissions on whatever catalog/schema/table you are trying to query.
