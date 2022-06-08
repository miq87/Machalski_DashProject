from dash import Dash
import dash_bootstrap_components as dbc


def get_dash():
    return Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, './styles.css'],
                suppress_callback_exceptions=True)
