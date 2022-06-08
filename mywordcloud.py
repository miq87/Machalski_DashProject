import base64
from io import BytesIO
from wordcloud import WordCloud

from myutils import nf_pallette, netflix_logo_image, get_wordlist


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
