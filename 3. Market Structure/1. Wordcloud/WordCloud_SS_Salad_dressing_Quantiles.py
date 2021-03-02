#######################################################################
## Attribute Grouping : Other groups
## Wordcloud code
## Author: Yashwanth M R (yashwanth.ramachandra@harman.com)
## Created on: 3/04/2017
## Latest Modified Date: 3/04/2017 by yashwanth.ramachandra@harman.com
## Version 1
#######################################################################

#import sys
#sys.modules[__name__].__dict__.clear()

# Import libraries
exec('''
import wordcloud as wc # http://www.lfd.uci.edu/~gohlke/pythonlibs/
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

# Quantiles
SS_Salad_dressing_Trans_Share_Quan = pd.qcut(SS_Salad_dressing.iloc[0:,2],q=3)
SS_Salad_dressing_Trans_Share_G0 = SS_Salad_dressing_Trans_Share.query('Transaction_Share > 0')

SS_Salad_dressing_Trans_Share_Small = SS_Salad_dressing_Trans_Share_G0.query('Transaction_Share >= 0.0001 & Transaction_Share <= 0.0002')


np.where(SS_Salad_dressing_Trans_Share_G0['Transaction_Share>=0.0001 & Transaction_Share<=0.0002'],'Small',np.where(SS_Salad_dressing_Trans_Share_G0['Transaction_Share>0.0002 & Transaction_Share<=0.000667']),'Medium','High')



# Cummulative sum # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.cumsum.html
SS_Salad_dressing['No_of_Transactions_Cumsum'] = SS_Salad_dressing['No_of_Transactions'].cumsum()
SS_Salad_dressing['Transaction_Share_Cumsum'] = SS_Salad_dressing['Transaction_Share'].cumsum()
SS_Salad_dressing = SS_Salad_dressing.sort_values(['Transaction_Share'],ascending = False)

# Filter Cum Transaction Share of 80% # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html
SS_SD_80_Trans_Share = SS_Salad_dressing.query('Transaction_Share_Cumsum >= .8021')
SS_SD_80_Trans_Share = SS_SD_80_Trans_Share.sort_values(by='Transaction_Share_Cumsum',
                                                                       ascending=True)''')

# Concatenate words # http://stackoverflow.com/questions/12309976/convert-list-into-string-with-spaces-in-python
exec('''import string
SS_SD_80_Trans_Share_npA = np.array(SS_SD_80_Trans_Share.iloc[0:,0])
print(len(SS_SD_80_Trans_Share_npA))
SS_SD_80_Trans_Share_Jtxt = ' '.join(str(x) for x in SS_SD_80_Trans_Share_npA)
SS_SD_80_Trans_Share_Jtxt = SS_SD_80_Trans_Share_Jtxt.replace("&","")
''')

# Function to create TermDocumentMatrix
exec('''from collections import defaultdict
d = defaultdict(int)
for SS_SD_80_Trans_Share in SS_SD_80_Trans_Share_Jtxt.split():
   d[SS_SD_80_Trans_Share] += 1''')

# Wordcloud # http://stackoverflow.com/questions/19130512/stopword-removal-with-nltk
# https://amueller.github.io/word_cloud/auto_examples/a_new_hope.html   
exec('''import wordcloud as wc
import nltk
stop = set(nltk.corpus.stopwords.words('english'))
WC_SS_SD_80_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,random_state=1,width=1600,height=1400).generate_from_frequencies(d)
''')
    
# Show
exec('''
mplt.imshow(WC_SS_SD_80_Trans_Share, interpolation='bilinear')
SS_SD_title = mplt.title('SS Salad Dressing with 80% Transaction Share')
mplt.setp(SS_SD_title,color = 'r')
mplt.axis("off")
mplt.show()
''')


# Filter Cum Transaction Share of 80% # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html
exec('''SS_SD_20_Trans_Share = SS_Salad_dressing.query('Transaction_Share_Cumsum < .8021')
SS_SD_20_Trans_Share = SS_SD_20_Trans_Share.sort_values(by='Transaction_Share_Cumsum',
                                                                       ascending=True)''')

# Concatenate words # http://stackoverflow.com/questions/12309976/convert-list-into-string-with-spaces-in-python
exec('''import string
SS_SD_20_Trans_Share_npA = np.array(SS_SD_20_Trans_Share.iloc[0:,0])
print(len(SS_SD_20_Trans_Share_npA))
SS_SD_20_Trans_Share_Jtxt = ' '.join(str(x) for x in SS_SD_20_Trans_Share_npA)
SS_SD_20_Trans_Share_Jtxt = SS_SD_20_Trans_Share_Jtxt.replace("&","")
''')

# Function to create TermDocumentMatrix
exec('''from collections import defaultdict
d = defaultdict(int)
for SS_SD_20_Trans_Share in SS_SD_20_Trans_Share_Jtxt.split():
   d[SS_SD_20_Trans_Share] += 1''')

# Wordcloud # http://stackoverflow.com/questions/19130512/stopword-removal-with-nltk
exec('''import wordcloud as wc
import nltk
stopwords = set(nltk.corpus.stopwords.words('english'))
stopwords.add("8")
WC_SS_SD_20_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stopwords,random_state=1,width=1600,height=1400).generate_from_frequencies(d)
''')

# Show
exec('''mplt.imshow(WC_SS_SD_20_Trans_Share, interpolation='bilinear')
mplt.title('SS Salad Dressing with 20% Transaction Share')
SS_SD_title = mplt.title('SS Salad Dressing with 20% Transaction Share')
mplt.setp(SS_SD_title,color = 'r')
mplt.axis("off")
mplt.show()
''')

##############################################################################################################################################
# ********************************************** END *****************************************************************************************
##############################################################################################################################################
