import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def WCLOUD(stpwrd, imgfname="wordcloud.png"):

    # Lecture des tweets
    file = open("res.csv", "r")
    text = ""
    for line in file.readlines():
        text += line.split(",")[2] + " "

    # Mots à ne pas prendre en compte par le systeme
    g_stopwords = stpwrd
    # optionally add: stopwords=STOPWORDS and change the arg below

    def generate_wordcloud(text):
        wordcloud = WordCloud(font_path='Roboto_Slab/RobotoSlab-Regular.ttf',  # la font utilisé
                              relative_scaling=1,
                              width=400,  # taille de l'image finale, prédit la résolution des mots aussi
                              height=400,
                              stopwords=g_stopwords).generate(text)
        plt.imsave(imgfname, wordcloud)

    generate_wordcloud(text)
