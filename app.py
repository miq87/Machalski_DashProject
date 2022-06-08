# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from dash import Input, Output

from myfigures import (get_fig_genres, get_fig_movies_shows)
from mylayout import get_layout
from mydash import get_dash
from mytabs import get_tabs
from myutils import get_netflix_df
from mywordcloud import get_image

app = get_dash()

server = app.server

df = get_netflix_df()

app.layout = get_layout()  # Pobieranie layoutu


#   Callback generujący zakładki

@app.callback(Output('tabs-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    return get_tabs(tab, df)


#   Funkcja callback generująca wykres z gatunkami filmów/seriali w zakresie dat

@app.callback(Output('fig_genres', 'figure'), [Input('daterange-slider', 'value')])
def get_genres(rangedate):
    return get_fig_genres(df, rangedate)


@app.callback(Output('fig_movies_shows', 'figure'), [Input('daterange-slider', 'value')])
def get_genres(rangedate):
    return get_fig_movies_shows(df, rangedate)


#   Funkcja oraz callback generująca obiekt wordcloud

@app.callback(Output('image_wc', 'src'), [Input('image_wc', 'id')])
def make_image(b):
    return get_image(df)


if __name__ == '__main__':
    app.run_server(debug=True)
