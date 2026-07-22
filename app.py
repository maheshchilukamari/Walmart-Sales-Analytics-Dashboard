import pandas as pd
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Load dataset
df = pd.read_csv('data/Walmart.csv')
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Month'] = df['Date'].dt.to_period('M').astype(str)
df['Year'] = df['Date'].dt.year
df['Temp_Range'] = pd.cut(df['Temperature'], bins=5).astype(str)

# App setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Walmart Sales Dashboard"

server = app.server
app.title = "Walmart Sales Dashboard"
# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Walmart Sales Forecasting Dashboard", className="text-center text-primary mb-4"), width=12)
    ]),

    # 1. Store-wise Total Sales
    dbc.Row([
        dbc.Col([
            html.Label("Select Store:"),
            dcc.Dropdown(
                id='store-select',
                options=[{'label': f'Store {i}', 'value': i} for i in sorted(df['Store'].unique())],
                value=1,
                clearable=False
            ),
            dcc.Graph(id='store-sales-bar')
        ], width=6),

        # 2. Weekly Sales Trend with Holiday Toggle
        dbc.Col([
            html.Label("Show Holidays Only:"),
            dcc.Checklist(
                id='holiday-check',
                options=[{'label': 'Holiday Weeks', 'value': 1}],
                value=[]
            ),
            dcc.Graph(id='weekly-sales-line')
        ], width=6)
    ]),

    # 3. Fuel Price vs Weekly Sales (CPI color)
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='fuel-scatter',
                      figure=px.scatter(df, x='Fuel_Price', y='Weekly_Sales', color='CPI',
                                        hover_data=['Store', 'Date'],
                                        title='Fuel Price vs Weekly Sales'))
        ])
    ]),

    # 4. Monthly Average Sales Heatmap
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='monthly-sales-heatmap',
                      figure=px.density_heatmap(df.groupby(['Month', 'Store'])['Weekly_Sales']
                                                .mean().reset_index(),
                                                x='Month', y='Store', z='Weekly_Sales',
                                                color_continuous_scale='Viridis',
                                                title="Monthly Average Sales by Store"))
        ])
    ]),

    # 5. Unemployment Impact (Bubble Chart)
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='unemployment-bubble',
                      figure=px.scatter(df, x='Unemployment', y='Weekly_Sales',
                                        size='CPI', color='Store',
                                        hover_name='Date', title='Unemployment Impact on Weekly Sales'))
        ])
    ]),

    # 6. Sales Distribution by Temperature
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='temp-distribution',
                      figure=px.violin(df, y='Weekly_Sales', x='Temp_Range',
                                       box=True, points='all',
                                       title='Sales Distribution Across Temperature Ranges'))
        ])
    ]),

    #7 Sales shares by store Pie + Area Charts
    dbc.Row([
        dbc.Col(dcc.Graph(id='pie-chart',
                          figure=px.pie(df.groupby('Store', as_index=False)['Weekly_Sales'].sum(),
                                        values='Weekly_Sales', names='Store',
                                        title='Sales Share by Store'))),
        dbc.Col(dcc.Graph(id='area-chart',
                          figure=px.area(df.groupby('Date', as_index=False)['Weekly_Sales'].sum(),
                                         x='Date', y='Weekly_Sales',
                                         title='Weekly Sales Area Chart')))
    ]),

    #8 Store Sales using the Sunburst + Radial
    dbc.Row([
        dbc.Col(dcc.Graph(id='sunburst',
                          figure=px.sunburst(df, path=['Year', 'Store'], values='Weekly_Sales',
                                             title='Sunburst: Sales by Year > Store'))),
        dbc.Col(dcc.Graph(id='radial',
                          figure=px.bar_polar(df.groupby('Store')['Weekly_Sales'].sum().reset_index(),
                                              r='Weekly_Sales', theta='Store',
                                              title='Radial Bar Chart: Store Sales')))
    ]),

    #9 Sales by Temperature and HolidayPopulation Pyramid
    dbc.Row([
        dbc.Col(dcc.Graph(id='pyramid', figure=px.bar(
            df.groupby([pd.cut(df['Temperature'], bins=6).astype(str), 'Holiday_Flag'])['Weekly_Sales']
              .sum().reset_index()
              .rename(columns={'Temperature': 'Temp_Bin'}),
            x='Weekly_Sales', y='Temp_Bin', color='Holiday_Flag',
            orientation='h', title='Population Pyramid Style: Sales by Temperature and Holiday')))
    ])
], fluid=True)

# Callbacks
@app.callback(
    Output('store-sales-bar', 'figure'),
    Input('store-select', 'value')
)
def update_store_bar(store_id):
    dff = df[df['Store'] == store_id].groupby('Date')['Weekly_Sales'].sum().reset_index()
    fig = px.bar(dff, x='Date', y='Weekly_Sales', title=f'Total Weekly Sales for Store {store_id}')
    return fig

@app.callback(
    Output('weekly-sales-line', 'figure'),
    [Input('store-select', 'value'),
     Input('holiday-check', 'value')]
)
def update_line(store_id, holiday_only):
    dff = df[df['Store'] == store_id]
    if 1 in holiday_only:
        dff = dff[dff['Holiday_Flag'] == 1]
    fig = px.line(dff, x='Date', y='Weekly_Sales', markers=True,
                  title=f'Weekly Sales Trend{" on Holidays" if 1 in holiday_only else ""}')
    return fig

# Run server
if __name__ == '__main__':
    app.run(debug=True)

