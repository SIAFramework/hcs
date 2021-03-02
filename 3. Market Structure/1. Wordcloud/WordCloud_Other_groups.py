#######################################################################
## Attribute Grouping : Other groups
## Wordcloud code
## Author: Yashwanth M R (yashwanth.ramachandra@harman.com)
## Created on: 24/03/2017
## Latest Modified Date: 30/03/2017 by yashwanth.ramachandra@harman.com
## Version 1
#######################################################################

# Import libraries
import wordcloud as wc # http://www.lfd.uci.edu/~gohlke/pythonlibs/
import numpy as np
import pandas as pd
import matplotlib.pyplot as mplt

# Import dataset
Other_groups = pd.read_csv('D:/3. Market Structure/1. WordCloud/WC_OtherGroups.csv')
print(Other_groups.head(5))

# Aggregate data
Other_groups_aggr = Other_groups.groupby(['Attribute_values']).sum().reset_index()
Other_groups_aggr = Other_groups_aggr.sort_values(['buyers_count'],ascending = False)
print(type(Other_groups_aggr))
print(Other_groups_aggr.head(5))

# Remove zero buyers_counts # http://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
Other_groups_aggr = Other_groups_aggr.query('buyers_count > 0')
Other_groups_aggr = Other_groups_aggr.sort_values(by = 'buyers_count', ascending=False)
print(Other_groups_aggr.tail(5))
print(Other_groups_aggr.shape)

# Convert to class dict
# http://stackoverflow.com/questions/893417/item-frequency-count-in-python
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_dict.html
# http://stackoverflow.com/questions/18695605/python-pandas-dataframe-to-dictionary

from collections import defaultdict
Other_groups_aggr_dict = Other_groups_aggr.set_index('Attribute_values')['buyers_count'].to_dict()
word_cloud = wc.WordCloud(background_color='white',
                          width=1200,
                          height=1000
                         ).generate_from_frequencies(Other_groups_aggr_dict)
mplt.figure()
mplt.imshow(word_cloud)
mplt.axis("off")
mplt.show()
    

# Wordcloud 
#subset = Other_groups_aggr[['Attribute_values','buyers_count']]
#tuples = tuple(tuple(x) for x in subset.values)
#tuples = tuple([tuple(x) for x in Other_groups_aggr.buyers_count.value_counts().reset_index().values])
#Other_groups_aggr_WC = WC.WordCloud.generate_from_frequencies(tuples)

# Test # https://amueller.github.io/word_cloud/auto_examples/a_new_hope.html
#from wordcloud import STOPWORDS
#stopwords = set(STOPWORDS)
#stopwords.add("work")
#stopwords.add("connected")
#stopwords.add("services")
#text = 'Myself Yashwanth. I work as Senior Data Scientist in Harman Connected Services'
#wordcloud_samp=wc.WordCloud(background_color='white',stopwords = stopwords,
#                          width=1200,
 #                         height=1000
  #                       ).generate(text)
#mplt.figure()
#mplt.imshow(wordcloud_samp)
#mplt.axis("off")
#mplt.show()

# Test with generate_from_frequencies()
#from collections import defaultdict
#words = "apple banana apple strawberry banana lemon"
#d = defaultdict(int)
#for word in words.split():
#    d[word] += 1
#word_cloud = wc.WordCloud(background_color='white',stopwords = stopwords,
                          width=1200,
                          height=1000
                         ).generate_from_frequencies(d)
mplt.figure()
mplt.imshow(word_cloud)
mplt.axis("off")
mplt.show()
