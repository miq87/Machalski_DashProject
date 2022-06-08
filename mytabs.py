from dash import html, dcc
import dash_bootstrap_components as dbc

from myfigures import get_fig_movies_shows, get_fig_countries_genres, \
    get_fig_countries, get_fig_countries_bar, get_fig_map, get_fig_genres, get_fig_age_ratings


def get_tabs(tab, df):
    year_added = df['year_added'].unique()
    if tab == 'tab_movies_shows':
        fig_movies_shows = get_fig_movies_shows(df, [2008, 2021])

        return html.Div([
            html.Div([
                html.H3('Filmy - Seriale')
            ], className='m-3'),
            html.Div([
                html.Div([
                    dcc.Graph(id='fig_movies_shows', figure=fig_movies_shows)
                ]),
                html.Div([
                    get_rangeslider(year_added, True)
                ], className='m-3')
            ], className='d-flex justify-content-center flex-row align-items-center')
        ], className='d-flex justify-content-center flex-column align-items-center')

    elif tab == 'tab_countries':
        fig_countries = get_fig_countries(df)
        fig_countries_bar = get_fig_countries_bar(df)
        return dbc.Container([
            dbc.Row([
                html.Div([
                    html.Div([
                        html.H3('Pochodzenie filmów / seriali')
                    ], className='m-3')
                ], className='d-flex justify-content-center flex-column align-items-center'),
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='fig_countries', figure=fig_countries)
                ], sm=12, md=12, lg=4),
                dbc.Col([
                    dcc.Graph(id='fig_countries_2', figure=fig_countries_bar)
                ], sm=12, md=12, lg=8)
            ])
        ], fluid=True)

    elif tab == 'tab_map':
        fig_map = get_fig_map(df)
        return html.Div([
            html.Div([
                html.H3('MAPA')
            ], className='m-3'),
            html.Div([
                dcc.Graph(id='fig_map', figure=fig_map)
            ], className='col-md-8')
        ], className='d-flex justify-content-center align-items-center flex-column')

    elif tab == 'tab_genres':
        fig_countries_genres = get_fig_countries_genres(df)
        fig_genres = get_fig_genres(df, [2008, 2021])
        return dbc.Container([
            dbc.Row([
                html.Div([
                    html.Div([
                        html.H3('Najczęściej występujące gatunki filmów / seriali')
                    ], className='m-3')
                ], className='d-flex justify-content-center flex-column align-items-center')
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div(dcc.Graph(id='fig_genres', figure=fig_genres)),
                    get_rangeslider(year_added, False)
                ], sm=12, md=12, lg=4),
                dbc.Col([
                    dcc.Graph(id='fig_countries_genres', figure=fig_countries_genres)
                ], sm=12, md=12, lg=8)
            ])
        ], fluid=True)

    elif tab == 'tab_age_ratings':
        fig_age_ratings = get_fig_age_ratings(df)
        return html.Div([
            html.Div([
                html.H3('Kategorie wiekowe w filmach / serialach')
            ], className='m-3'),
            html.Div([
                dcc.Graph(id='fig_age_ratings', figure=fig_age_ratings)
            ])
        ], className='d-flex justify-content-center flex-column align-items-center')

    elif tab == 'tab_wordcloud':
        return html.Div([
            html.Div([
                html.H3('Najczęściej występujące słowa w tytułach filmów / seriali')
            ], className='m-3'),
            html.Div([
                dcc.Loading(children=html.Div([html.Img(id='image_wc')]),
                            id='loading-1', type='dot', color='#b20710')
            ], className='m-3 mh-100')
        ], className='d-flex justify-content-center flex-column align-items-center')


def get_rangeslider(year_added, is_vertical):
    return html.Div(dcc.RangeSlider(min=year_added.min(), max=year_added.max(), vertical=is_vertical,
                                    step=1, value=[year_added.min(), year_added.max()], id='daterange-slider',
                                    marks={str(year): str(year) for year in year_added}))
