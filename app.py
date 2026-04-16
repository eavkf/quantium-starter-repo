from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('data/daily_sales_data.csv')

PINK = '#d63384'
LIGHT_PINK = '#ffb6d9'
BG = '#fff0f8'

app.layout = html.Div(style={
    'fontFamily': 'Quicksand, sans-serif',
    'maxWidth': '900px',
    'margin': '0 auto',
    'padding': '30px',
}, children=[

    html.H1('🌸 Sales of Pink Morsel Over Time 🌸', style={
        'color': PINK,
        'textAlign': 'center',
        'fontSize': '2.2rem',
        'textShadow': '2px 2px 8px rgba(214,51,132,0.15)',
    }),

    html.P('✨ Select a region to explore the data ✨', style={
        'textAlign': 'center',
        'color': '#e75480',
        'fontSize': '1rem',
        'marginBottom': '20px',
    }),

    html.Div(style={
        'background': 'rgba(255,255,255,0.7)',
        'borderRadius': '20px',
        'padding': '20px 30px',
        'boxShadow': '0 4px 20px rgba(214,51,132,0.15)',
        'marginBottom': '24px',
        'display': 'flex',
        'alignItems': 'center',
        'gap': '20px',
    }, children=[
        html.Label('🌷 Region:', style={
            'color': PINK,
            'fontWeight': '700',
            'fontSize': '1.1rem',
        }),
        dcc.RadioItems(
            ['south', 'east', 'north', 'west', 'all'],
            value='all',
            id='radio-items',
            inline=True,
            inputStyle={'marginRight': '5px', 'accentColor': PINK},
            labelStyle={'marginRight': '20px', 'fontWeight': '600', 'color': '#c2185b'},
        ),
    ]),

    html.Div(style={
        'background': 'rgba(255,255,255,0.8)',
        'borderRadius': '20px',
        'padding': '20px',
        'boxShadow': '0 4px 20px rgba(214,51,132,0.15)',
    }, children=[
        dcc.Graph(id='pinkmorsel-over-time')
    ])
])

@callback(
    Output('pinkmorsel-over-time', 'figure'),
    Input('radio-items', 'value'))
def update_figure(selected_region):
    if selected_region == 'all':
        fig = px.line(df, x='date', y='sales', color_discrete_sequence=[PINK])
    else:
        filtered_df = df[df['region'] == selected_region]
        fig = px.line(filtered_df, x='date', y='sales', color_discrete_sequence=[PINK])

    fig.update_layout(
        plot_bgcolor=BG,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Quicksand', color='#c2185b'),
        xaxis=dict(gridcolor=LIGHT_PINK),
        yaxis=dict(gridcolor=LIGHT_PINK),
    )
    return fig

if __name__ == '__main__':
    app.run()