import base64
from io import BytesIO

import matplotlib
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from collections import Counter


colors = ['#0b090a', '#660708', '#a4161a', '#ba181b', '#e5383b', '#b1a7a6']  # paleta kolorów Netflix

netflix_logo_image = np.array(Image.open('assets/netflix_logo.png'))

nf_pallette = matplotlib.colors.LinearSegmentedColormap.from_list("", ['#221f1f', '#b20710'])

def plot_wordcloud(data):
    wc = WordCloud(max_words=200, background_color="white",
                   colormap=nf_pallette, mask=netflix_logo_image,
                   scale=0.3).generate(str(data))
    return wc.to_image()


def get_image(df):
    wordlist = get_wordlist(df)
    img = BytesIO()
    plot_wordcloud(wordlist).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())

# Funkcja generująca listę 'wordlist' zawierająca najczęściej występujące
# słowa w tytułach filmów oraz seriali
def get_wordlist(df):
    genres = list(df['title'])
    gen = []
    for i in genres:
        i = list(i.split(' '))
        for j in i:
            if len(j) > 3:
                gen.append(j.replace("'", '').replace(',', '').replace('.', ''))
    g = Counter(gen)
    wordlist = list(set(gen))
    return wordlist

