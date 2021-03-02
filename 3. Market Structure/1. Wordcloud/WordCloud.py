# coding: utf-8

# # Introduction to Data Science - IRi

# ## Word Cloud


# Check python version
import sys
print(sys.version)

# ### Wordcloud

# In[1]:

# Import libraries and dataset
import pandas as pd
import wordcloud as wc
import numpy as np
import matplotlib.pyplot as mplt
import random
from os import path
from PIL import Image
import string
import nltk
import pyparsing

inputpath = sys.arg[1]
outputPath = sys.arg[2]
Stopword_inputpath = 'D:/MarketStructureOnDemand/'

Condition_file = pd.read_csv(inputpath +'Condition.csv',sep = '|')
Condition_1 = Condition_file.iloc[0,0]
Condition_2 = Condition_file.iloc[0,1]
data = pd.read_csv(inputpath +'AttributeShare.csv')
data['Trans_Share'] = data['Trans_Share']*100

# Sort by Transaction Count
data = data.sort_values(by = 'Trans_Share',ascending=False)


# In[3]:

# Seperate out data based on Quartiles as Small, Medium & High Transaction Share
data_df = data
data_df_NZ = data_df.query('Trans_Share>0')


P1=np.percentile(data_df_NZ.iloc[0:,2],1)
P33=np.percentile(data_df_NZ.iloc[0:,2],33)
P34=np.percentile(data_df_NZ.iloc[0:,2],34)
P66=np.percentile(data_df_NZ.iloc[0:,2],66)
P67=np.percentile(data_df_NZ.iloc[0:,2],67)
P100=np.percentile(data_df_NZ.iloc[0:,2],100)

# In[43]:

# Cummulative sum 
data['No_of_Trans_Cumsum'] = data['No_of_Trans'].cumsum()
data['Trans_Share_Cumsum'] = data['Trans_Share'].cumsum()
data = data.sort_values(['Trans_Share'],ascending = False)


# Filter Cum Transaction Share of 80%
if Condition_1=='TRANSACTION SHARE' and Condition_2 == 80:
    data_80_Trans_Share = data[(data['Trans_Share']>=0.8000)]

    # Concatenate words 
    data_80_Trans_Share_npA = np.array(data_80_Trans_Share.iloc[0:,0])
    data_80_Trans_Share_Jtxt = ' '.join(str(x) for x in data_80_Trans_Share_npA)
    data_80_Trans_Share_Jtxt = data_80_Trans_Share_Jtxt.replace("&","")
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for data_80_Trans_Share in data_80_Trans_Share_Jtxt.split():
       d[data_80_Trans_Share] += 1
    
    
    # In[41]:
    
    # Wordcloud 
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_data_80_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                    random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    mplt.imshow(WC_data_80_Trans_Share, interpolation='bilinear')
    data_title = mplt.title('Wordcloud with 80% Transaction Share')
    mplt.setp(data_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+ 'WordCloud.jpeg')

   
elif Condition_1=='TRANSACTION SHARE' and Condition_2 == 20:
    data_20_Trans_Share = data[(data['Trans_Share']<0.8000)]

    # Concatenate words 
    data_20_Trans_Share_npA = np.array(data_20_Trans_Share.iloc[0:,0])
    data_20_Trans_Share_Jtxt = ' '.join(str(x) for x in data_20_Trans_Share_npA)
    data_20_Trans_Share_Jtxt = data_20_Trans_Share_Jtxt.replace("&","")
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for data_20_Trans_Share in data_20_Trans_Share_Jtxt.split():
       d[data_20_Trans_Share] += 1
    
    
    # In[47]:
    
    # Wordcloud 
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    stop.add("8")
    WC_data_20_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,random_state=1,
            width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_data_20_Trans_Share, interpolation='bilinear')
    mplt.title('Wordcloud with 20% Transaction Share')
    data_title = mplt.title('Wordcloud with 20% Transaction Share')
    mplt.setp(data_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WC_data_Trans_Share_20_Trans_Share.jpeg')
    
elif Condition_1=='TRANSACTION SIZE' and Condition_2 == 'Small':
    data_df_Small = data_df_NZ[(data_df_NZ['Trans_Share']>=P1) &  (data_df_NZ['Trans_Share']<=P33)]

    # Concatenate words 
    data_df_Small_npA = np.array(data_df_Small.iloc[0:,0])
    data_df_Small_Jtxt = ' '.join(str(x) for x in data_df_Small_npA)
    data_df_Small_Jtxt = data_df_Small_Jtxt.replace("&","")
    
    
    # In[9]:
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for data_Trans_Share_Small in data_df_Small_Jtxt.split():
       d[data_Trans_Share_Small] += 1
    
    # Import wordcloud libraries
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_data_Trans_Share_Small = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                           random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_data_Trans_Share_Small, interpolation='bilinear')
    data_title = mplt.title('Wordcloud with Small Transaction Share')
    mplt.setp(data_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WordCloud.jpeg')
    
elif Condition_1=='TRANSACTION SIZE' and Condition_2 == 'Medium':
    data_df_Medium = data_df_NZ[(data_df_NZ['Trans_Share']>=P34) &  (data_df_NZ['Trans_Share']<=P66)]
    
    # Concatenate words 
    data_df_Medium_npA = np.array(data_df_Medium.iloc[0:,0])
    data_df_Medium_Jtxt = ' '.join(str(x) for x in data_df_Medium_npA)
    data_df_Medium_Jtxt = data_df_Medium_Jtxt.replace("&","")
    
    
    # In[14]:
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for data_Trans_Share_Medium in data_df_Medium_Jtxt.split():
       d[data_Trans_Share_Medium] += 1
    
    # Import wordcloud libraries
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_data_Trans_Share_Medium = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                           random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_data_Trans_Share_Medium, interpolation='bilinear')
    data_title = mplt.title('Wordcloud with Medium Transaction Share')
    mplt.setp(data_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WordCloud.jpeg')
    
elif Condition_1=='TRANSACTION SIZE' and Condition_2 == 'High':
    data_df_High = data_df_NZ[(data_df_NZ['Trans_Share']>=P67) &  (data_df_NZ['Trans_Share']<=P100)]
    
    # Concatenate words 
    data_df_High_npA = np.array(data_df_High.iloc[0:,0])
    data_df_High_Jtxt = ' '.join(str(x) for x in data_df_High_npA)
    data_df_High_Jtxt = data_df_High_Jtxt.replace("&","")
    
    
    # In[17]:
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for data_Trans_Share_High in data_df_High_Jtxt.split():
       d[data_Trans_Share_High] += 1
    
    # Import wordcloud libraries
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_data_Trans_Share_High = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                           random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_data_Trans_Share_High, interpolation='bilinear')
    data_title = mplt.title('Wordcloud with High Transaction Share')
    mplt.setp(data_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WordCloud.jpeg')
    
else:
    data_df_NZ_npA = np.array(data_df_NZ.iloc[0:,0])
    data_df_NZ_Jtxt = ' '.join(str(x) for x in data_df_NZ_npA)
    data_df_NZ_Jtxt = data_df_NZ_Jtxt.replace("&","")
    
    
    # In[17]:
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for data_Trans_Share_High in data_df_NZ_Jtxt.split():
       d[data_Trans_Share_High] += 1
    
    # Import wordcloud libraries
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_data_Trans_Share_High = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                           random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_data_Trans_Share_High, interpolation='bilinear')
    data_title = mplt.title('Wordcloud with Total Transaction Share')
    mplt.setp(data_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WordCloud.jpeg')

############################################################################# END ################################################################################################