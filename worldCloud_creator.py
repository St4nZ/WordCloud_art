from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def couleur(*args, **kwargs):
    import random
    return "rgb(0, 100, {})".format(random.randint(100, 255))


def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,0%%, %d%%)" % np.random.randint(49,51))


# ----- TEXT FILE -----
text = open('****', 'r').read() #please repalce *** by the path to your file

# Word that you can exclude form your text in French or English --> please change the variable at next step
exclure_mots_FR = ['d','n', 'va','me', 'son', 'nous', 'nos', 'ai', 'dis', 'mon', 'prestataire', 'si',\
    'cela','qu', 'je', 'avec', 'du', 'de', 'la', 'des', 'le','ne', 'et', 'est', 'elle', 'une', 'en', \
    'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce',\
    'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
exclude_mots_EN = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]


# ----- PICTURE FILE -----
custom_mask = np.array(Image.open('****'))# replace **** by your jpeg or PNG blakand white for your custom template

#settings than can be modified like the max number of words you want
wordcloud = WordCloud(background_color = 'white', stopwords = exclure_mots_FR, max_words = 101,mask = custom_mask,
	contour_width = 0.5).generate(text)


# ------  color or grey pictures ------
wordcloud.recolor(color_func = couleur)
#wordcloud.recolor(color_func = grey_color_func)


# ---- DISPLAY IMAGE -----
plt.imshow(wordcloud)#, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0) #permet de mettre l'image a l'échelle car matplotible descend la qualité a 800x600
plt.show()

# ---- SAVE IMAGE ----
wordcloud.to_file('new_output.png')
