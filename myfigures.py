import plotly.express as px

from age_ratings import get_age_ratings
from myutils import colors, get_genres, group_by_country, \
    get_countries_genres, get_map_countries, get_by_rangedate


def get_fig_movies_shows(df, rangedate):
    df = get_by_rangedate(df, rangedate)
    fig = px.pie(df['type'].value_counts().reset_index(),
                 values='type', names='index', width=600, height=600)
    fig.update_traces(textposition='inside', textinfo='percent + label',
                      hole=0.4, marker=dict(colors=['#b20710', '#221f1f'],
                                            line=dict(color='white', width=4)))
    fig.update_layout(font_size=22, showlegend=False)
    return fig


def get_fig_countries(df):
    df = group_by_country(df).head(8)
    fig = px.pie(df, values='counts', names='country', width=600, height=600)
    return get_colored_pie(fig)


def get_fig_countries_bar(df):
    df = group_by_country(df).head(8)
    fig = px.bar(df, x='country', y='counts', color='country',
                 labels={'country': 'Kraj', 'counts': 'Liczba'})
    return fig


def get_fig_genres(df, rangedate):
    df = get_genres(df, rangedate).head(8)
    fig = px.pie(df, names='listed_in', values='counts', width=600, height=600)
    return get_colored_pie(fig)


def get_fig_countries_genres(df):
    df = get_countries_genres(df)
    fig = px.bar(df, x='country', y='counts', color='listed_in',
                 labels={'country': 'Kraj', 'counts': 'Liczba', 'listed_in': 'Gatunek'})
    return fig


def get_fig_map(df):
    return px.scatter_geo(get_map_countries(df), locations='iso_alpha', color='country',
                          hover_name='country', size='size', labels={'country': 'Kraj'},
                          projection="natural earth")


def get_fig_age_ratings(df):
    df = get_age_ratings(df)
    fig = px.pie(df, names='age_group', values='counts', width=600, height=600)
    return get_colored_pie(fig)


def get_colored_pie(fig):
    fig.update_traces(textposition='outside', textinfo='percent + label', hole=0.1,
                      marker=dict(colors=colors, line=dict(color='white', width=2)))
    fig.update_layout(font_size=16, showlegend=False)
    return fig
