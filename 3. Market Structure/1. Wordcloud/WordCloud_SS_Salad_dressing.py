#######################################################################
## Attribute Grouping : Other groups
## Wordcloud code
## Author: Yashwanth M R (yashwanth.ramachandra@harman.com)
## Created on: 3/04/2017
## Latest Modified Date: 3/04/2017 by yashwanth.ramachandra@harman.com
## Version 1
#######################################################################

# Import libraries
import wordcloud as wc # http://www.lfd.uci.edu/~gohlke/pythonlibs/
import numpy as np
import pandas as pd
import matplotlib.pyplot as mplt
import random
from os import path
from PIL import Image

# Import dataset
SS_Salad_dressing = pd.read_csv('D:/3. Market Structure/1. WordCloud/1. Input files/WC_SS_Salad_dressing.csv')
print(SS_Salad_dressing.head(5))

# Aggregate data
SS_Salad_dressing_aggr = SS_Salad_dressing.groupby(['Attribute_values']).sum().reset_index()
SS_Salad_dressing_aggr = SS_Salad_dressing_aggr.sort_values(['No_of_Transactions'],ascending = False)
print(type(SS_Salad_dressing_aggr))
print(SS_Salad_dressing_aggr.head(5))

# Remove zero No_of_Transactionss # http://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
SS_Salad_dressing_aggr = SS_Salad_dressing_aggr.query('No_of_Transactions > 0')
SS_Salad_dressing_aggr = SS_Salad_dressing_aggr.sort_values(by = 'No_of_Transactions', ascending=False)
print(SS_Salad_dressing_aggr.tail(5))
print(SS_Salad_dressing_aggr.shape)

# Convert to class dict
# http://stackoverflow.com/questions/893417/item-frequency-count-in-python
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_dict.html
# http://stackoverflow.com/questions/18695605/python-pandas-dataframe-to-dictionary

d = path.dirname("D:/3. Market Structure/1. WordCloud/1. Input files/")

# read the mask image taken from http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
#alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))
#stormtrooper_mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))


from collections import defaultdict
SS_Salad_dressing_aggr_dict = SS_Salad_dressing_aggr.set_index('Attribute_values')['No_of_Transactions'].to_dict()
WC_SS_Salad_dressing = wc.WordCloud(background_color='white',max_words=1000,random_state=1,
                          width=1200,
                          height=1000
                         ).generate_from_frequencies(SS_Salad_dressing_aggr_dict)

# Save Wordcloud
WC_SS_Salad_dressing.to_file(path.join(d,"SS_Salad_Dressing.png"))

# Show
mplt.imshow(WC_SS_Salad_dressing, interpolation='bilinear')
mplt.axis("off")
mplt.show()


# https://amueller.github.io/word_cloud/auto_examples/a_new_hope.html
# read the mask image taken from http://www.stencilry.org/stencils/movies/star%20wars/storm-trooper.gif
#d = path.dirname("D:/3. Market Structure/1. WordCloud/1. Input files/")
#mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))
#def grey_color_func(word, font_size, position, orientation, random_state=None,
 #                   **kwargs):
 #   return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
