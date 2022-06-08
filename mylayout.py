from dash import html, dcc


def get_layout():
    layout = html.Div([
        html.Div([
            html.Div([
                html.Img(src='assets/netflix_logo.png', width=300)
            ]),
            html.Div([
                html.H1(children='NETFLIX - Filmy / seriale'),
                html.H3(children='Analiza zawartości platformy streamingowej z filmami oraz serialami'),
                html.H6(
                    children='Interaktywna aplikacja webowa stworzona we frameworku Dash, napisana w języku Python.'),
            ], className='m-2')
        ], className='d-flex justify-content-start'),
        html.Hr(),
        dcc.Tabs(id="tabs", value='tab_movies_shows', children=[
            dcc.Tab(label='Seriale / Filmy', value='tab_movies_shows'),
            dcc.Tab(label='Kraje', value='tab_countries'),
            dcc.Tab(label='Mapa', value='tab_map'),
            dcc.Tab(label='Gatunki', value='tab_genres'),
            dcc.Tab(label='Kategorie wiekowe', value='tab_age_ratings'),
            dcc.Tab(label='Chmura słów', value='tab_wordcloud')
        ]),
        html.Div(id='tabs-content')], className='main')
    return layout
