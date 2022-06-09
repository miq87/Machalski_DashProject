import pandas as pd
import pycountry


def get_netflix_df():
    ##################################
    # Załadowanie pliku csv do ramki danych
    #
    df = pd.read_csv('./assets/netflix_titles.csv')
    ##################################
    # Usunięcie wierszy, które nie posiadają informacji o dacie dodania (date_added) -> 10 wierszy
    # Dodanie nowych pól 'year_added' oraz 'month_added'
    #
    df.drop(df.index[df['date_added'].isna()], inplace=True)
    df['year_added'] = df['date_added'].apply(lambda x: int(x[-4:len(x)]))
    df['month_added'] = df['date_added'].apply(lambda x: x.split(' ')[0])

    return df


# Funkcja, która zwraca ramkę w przedziale czasowym
def get_genres(df, rangedate):
    df = get_by_rangedate(df, rangedate)
    df = split_genres(df)
    return group_by_genre(df)


# Funkcja, która grupuje po krajach oraz gatunkach i zlicza ich ilości
def get_countries_genres(df):
    countries_top_list = get_top_countries(df, 6)
    genres_top_list = get_top_genres(df, 6)

    df = split_countries(df)
    df = split_genres(df)

    df = df[df['country'].isin(countries_top_list) & df['listed_in'].isin(genres_top_list)]
    df = df.groupby(['country', 'listed_in'])['listed_in'].count().sort_values(ascending=False).reset_index(name='counts')
    return df


# Funkcja, która grupuje po krajach oraz zlicza ich ilość
def group_by_country(df):
    return split_countries(df).groupby(['country'])['country'].count().sort_values(ascending=False).reset_index(name='counts')


# Funkcja, która grupuje po gatunkach oraz zlicza ich ilość
def group_by_genre(df):
    return split_genres(df).groupby(['listed_in'])['listed_in'].count().sort_values(ascending=False).reset_index(name='counts')


# Funkcja, która grupuje po obsadzie oraz zlicza ich ilość
def group_by_cast(df):
    return split_casts(df).groupby(['cast'])['cast'].count().sort_values(ascending=False).reset_index(name='counts')


# Funkcja, która zwraca najczęściej występujące kraje w formie listy
def get_top_countries(df, size):
    return group_by_country(df).head(size)['country'].tolist()


# Funkcja, która zwraca najczęściej występujące gatunki w formie listy
def get_top_genres(df, size):
    return group_by_genre(df).head(size)['listed_in'].tolist()


# Funkcja, która zwraca najczęściej występujących aktorów/aktorki w formie listy
def get_top_casts(df, size):
    return group_by_cast(df).head(size)['cast'].tolist()


# Funkcja rozdzielająca zawartość kolumny country zawierającej
# wiele pozycji oddzielonych po przecinku na oddzielne wiersze
def split_countries(df):
    return df.drop('country', axis=1).join(
        df['country'].str.split(', ?', expand=True).stack().reset_index(level=1, drop=True).rename('country'))


# Funkcja rozdzielająca zawartość kolumny listed_in zawierającej
# wiele pozycji oddzielonych po przecinku na oddzielne wiersze
def split_genres(df):
    return df.drop('listed_in', axis=1).join(
        df['listed_in'].str.split(', ?', expand=True).stack().reset_index(level=1, drop=True).rename('listed_in'))


# Funkcja rozdzielająca zawartość kolumny cast zawierającej
# wiele pozycji oddzielonych po przecinku na oddzielne wiersze
def split_casts(df):
    return df.drop('cast', axis=1).join(
        df['cast'].str.split(', ?', expand=True).stack().reset_index(level=1, drop=True).rename('cast'))


def get_by_rangedate(df, rangedate):
    return df.query("year_added >= @rangedate[0] & year_added <= @rangedate[1]")


# Funkcja przygotowująca ramkę danych do figury mapy
# Dodaje do ramki kolumnę iso_alpha (3 znakowy kod kraju),
# który jest potrzebny do umiejscowienia państwa na mapie
def get_map_countries(df):
    df = split_countries(df)
    df = group_by_country(df)
    df['size'] = df['counts']

    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_3
    codes = [countries.get(country, 'Unknown Code') for country in df['country']]
    df['iso_alpha'] = codes

    df.loc[df.country == 'South Korea', 'iso_alpha'] = 'KOR'
    df.loc[df.country == 'Taiwan', 'iso_alpha'] = 'TWN'
    df.loc[df.country == 'Russia', 'iso_alpha'] = 'RUS'
    df.loc[df.country == 'Czech Republic', 'iso_alpha'] = 'CZE'
    df.loc[df.country == 'Vietnam', 'iso_alpha'] = 'VNM'
    return df
