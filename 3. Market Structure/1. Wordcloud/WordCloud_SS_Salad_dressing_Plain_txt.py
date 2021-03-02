#######################################################################
## Attribute Grouping : Other groups
## Wordcloud code
## Author: Yashwanth M R (yashwanth.ramachandra@harman.com)
## Created on: 3/04/2017
## Latest Modified Date: 3/04/2017 by yashwanth.ramachandra@harman.com
## Version 1
#######################################################################

# Import libraries
exec('''import wordcloud as wc # http://www.lfd.uci.edu/~gohlke/pythonlibs/
import numpy as np
import pandas as pd
import matplotlib.pyplot as mplt
import random
from os import path
from PIL import Image''')

# Import dataset
exec('''SS_Salad_dressing = pd.read_csv('D:/3. Market Structure/1. WordCloud/1. Input files/WC_SS_Salad_dressing.csv')
print(SS_Salad_dressing.head(5))

# Sort by Transaction Count
SS_Salad_dressing = SS_Salad_dressing.sort_values(by = 'Transaction_Share',ascending=False)

# Cummulative sum # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.cumsum.html
SS_Salad_dressing['No_of_Transactions_Cumsum'] = SS_Salad_dressing['No_of_Transactions'].cumsum()
SS_Salad_dressing['Transaction_Share_Cumsum'] = SS_Salad_dressing['Transaction_Share'].cumsum()
SS_Salad_dressing = SS_Salad_dressing.sort_values(['Transaction_Share'],ascending = False)

# Filter Cum Transaction Share greater than 80% # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html
SS_Salad_dressing_20_Per = SS_Salad_dressing.query('Transaction_Share_Cumsum > .8021')
SS_Salad_dressing_20_Per = SS_Salad_dressing_20_Per.sort_values(by='Transaction_Share_Cumsum',
                                                                    ascending=True)''')

# Concatenate words # http://stackoverflow.com/questions/12309976/convert-list-into-string-with-spaces-in-python
exec('''import string
SS_Salad_dressing_20_Per_AV = np.array(SS_Salad_dressing_20_Per.iloc[0:,0])
print(len(SS_Salad_dressing_20_Per_AV))'''
)

exec('''SS_Salad_dressing_20_Per_AV_join_txt = ' '.join(str(x) for x in SS_Salad_dressing_20_Per_AV)
SS_Salad_dressing_20_Per_AV_replace = SS_Salad_dressing_20_Per_AV_join_txt.replace(" BALSAMIC VINAIGRETTE",
                                                                  "BALSAMIC VINAIGRETTES")
SS_Salad_dressing_20_Per_AV_Final = SS_Salad_dressing_20_Per_AV_replace''')


SS_Salad_dressing_20_Per_AV = str(" ".join(SS_Salad_dressing_20_Per_AV))

SS_Salad_dressing_20_Per_AV = SS_Salad_dressing_20_Per_AV.replace("&","")

SS_Salad_dressing_20_Per_AV_txt = ' '.join(str(x) for x in SS_Salad_dressing_20_Per_AV)
SS_Salad_dressing_20_Per_AV_split = SS_Salad_dressing_20_Per_AV_txt.split()
SS_Salad_dressing_20_Per_AV_join_txt = ' '.join(str(x) for x in SS_Salad_dressing_20_Per_AV_split)

#SS_Salad_dressing_20_Per_AV_Split = str(SS_Salad_dressing_20_Per_AV.rsplit("&",1))

#for SS_Salad_dressing_20_Per_AV_Split in SS_Salad_dressing_20_Per_AV:
#   print(SS_Salad_dressing_20_Per_AV_Split)


# Wordcloud
import wordcloud as wc
WC_SS_Salad_dressing_20_per_AV = wc.WordCloud(background_color='black',max_words=1000,
            random_state=1,width=1600,height=1400).generate(SS_Salad_dressing_20_Per_AV_Final)

# Show
exec('''mplt.imshow(WC_SS_Salad_dressing_20_per_AV, interpolation='bilinear')
mplt.axis("off")
mplt.show()
''')





# Filter Cum Transaction Share less than 80% # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html
SS_Salad_dressing_80_Per = SS_Salad_dressing.query('Transaction_Share_Cumsum <= .8021')
SS_Salad_dressing_80_Per = SS_Salad_dressing_80_Per.sort_values(by='Transaction_Share_Cumsum',
                                                                ascending=True)

# Concatenate words # http://stackoverflow.com/questions/12309976/convert-list-into-string-with-spaces-in-python
SS_Salad_dressing_80_Per_AV = np.array(SS_Salad_dressing_80_Per.iloc[0:,0])
SS_Salad_dressing_80_Per_AV = str(" ".join(SS_Salad_dressing_80_Per_AV))

# Wordcloud
import wordcloud as wc
#d = path.dirname("D:/3. Market Structure/1. WordCloud/1. Input files/")

WC_SS_Salad_dressing_80_per = wc.WordCloud(background_color='black',max_words=1000,random_state=1,
                          width=1200,
                          height=1000
                         ).generate(SS_Salad_dressing_80_Per_AV)

# Save Wordcloud
WC_SS_Salad_dressing.to_file(path.join(d,"SS_Salad_Dressing.png"))

# Show
mplt.imshow(WC_SS_Salad_dressing_80_per, interpolation='bilinear')
mplt.axis("off")
mplt.show()

##############################################################################################################################################
# ********************************************** END *****************************************************************************************
##############################################################################################################################################

# Convert to class dict
# http://stackoverflow.com/questions/893417/item-frequency-count-in-python
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_dict.html
# http://stackoverflow.com/questions/18695605/python-pandas-dataframe-to-dictionary

# read the mask image taken from http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
#alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))
#stormtrooper_mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))

# https://amueller.github.io/word_cloud/auto_examples/a_new_hope.html
# read the mask image taken from http://www.stencilry.org/stencils/movies/star%20wars/storm-trooper.gif
#d = path.dirname("D:/3. Market Structure/1. WordCloud/1. Input files/")
#mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))
#def grey_color_func(word, font_size, position, orientation, random_state=None,
 #                   **kwargs):
 #   return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

# Pareto chart
#from paretochart import pareto
#import matplotlib.pyplot as mplt
#fig, axes = mplt.subplots(2,2)

#pareto(SS_Salad_dressing.iloc[:,1], axes = axes[0,0])
#mplt.title('Basic chart without labels', fontsize=10)

# Renaming column names
#SS_Salad_dressing_Cumsum = SS_Salad_dressing_Cumsum.rename(index=str,
 #       columns = {"Attribute_Values":"Attribute_Values","No_of_Transactions":"No_of_Transactions_Cumsum",
  #                 "Transaction_Share":"Transaction_Share_Cumsum"})
# Convert dtype to numeric
#SS_Salad_dressing_Cumsum.iloc[0:,1:2] = SS_Salad_dressing_Cumsum.iloc[0:,1:2].apply(pd.to_numeric)

#d = path.dirname("D:/3. Market Structure/1. WordCloud/1. Input files/")

# adding stopwords
#stopwords = set(wc.STOPWORDS)
#stopwords.add(" '")
#   stopwords.add(",")

#def word_count(string):
    #my_string = string.lower().split()
    #my_dict = {}
    #for item in my_string:
      #  if item in my_dict:
      #      my_dict[item] += 1
     #   else:
    #        my_dict[item] = 1
    #print(my_dict)

# Save Wordcloud
# WC_SS_Salad_dressing.to_file(path.join(d,"SS_Salad_Dressing.png"))
