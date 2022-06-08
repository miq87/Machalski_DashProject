def get_age_ratings(df):
    df['age_group'] = df['rating']

    MR_age = {'TV-MA': 'Dorośli',
              'R': 'Dorośli',
              'PG-13': 'Nastolatkowie',
              'TV-14': 'Nastolatkowie',
              'TV-PG': 'Starsze dzieci',
              'NR': 'Nieocenione',
              'TV-G': 'Dzieci',
              'TV-Y': 'Dzieci',
              'TV-Y7': 'Starsze dzieci',
              'PG': 'Nastolatkowie',
              'G': 'Dzieci',
              'NC-17': 'Dorośli',
              'TV-Y7-FV': 'Starsze dzieci',
              'UR': 'Dorośli'}
    df['age_group'] = df['age_group'].map(MR_age)

    return df.groupby(['age_group'])['age_group'].count().sort_values(ascending=False).reset_index(name='counts')

