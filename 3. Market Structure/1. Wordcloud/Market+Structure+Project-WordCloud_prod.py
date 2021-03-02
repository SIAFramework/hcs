# coding: utf-8

# # Introduction to Data Science - IRi

# ## Word Cloud


# Check python version
import sys
print(sys.version)

# ### SS Salad Dressing

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

inputpath = 'D:/3. Market Structure/1. WordCloud/1. Input files/'
outputPath = 'D:/3. Market Structure/1. WordCloud/6. Output/'
Stopword_inputpath = 'D:/MarketStructureOnDemand/'

Condition_file = pd.read_csv(inputpath +'Condition.csv',sep = '|')
Condition_1 = Condition_file.iloc[0,0]
Condition_2 = Condition_file.iloc[0,1]
SS_Salad_dressing = pd.read_csv(inputpath +'AttributeShare.csv')
SS_Salad_dressing['Trans_Share'] = SS_Salad_dressing['Trans_Share']*100

# Sort by Transaction Count
SS_Salad_dressing = SS_Salad_dressing.sort_values(by = 'Trans_Share',ascending=False)


# In[3]:

# Seperate out data based on Quartiles as Small, Medium & High Transaction Share
SS_SD_df = SS_Salad_dressing
SS_SD_df_NZ = SS_SD_df.query('Trans_Share>0')


P1=np.percentile(SS_SD_df_NZ.iloc[0:,2],1)
P33=np.percentile(SS_SD_df_NZ.iloc[0:,2],33)
P34=np.percentile(SS_SD_df_NZ.iloc[0:,2],34)
P66=np.percentile(SS_SD_df_NZ.iloc[0:,2],66)
P67=np.percentile(SS_SD_df_NZ.iloc[0:,2],67)
P100=np.percentile(SS_SD_df_NZ.iloc[0:,2],100)

# In[43]:

# Cummulative sum 
SS_Salad_dressing['No_of_Trans_Cumsum'] = SS_Salad_dressing['No_of_Trans'].cumsum()
SS_Salad_dressing['Trans_Share_Cumsum'] = SS_Salad_dressing['Trans_Share'].cumsum()
SS_Salad_dressing = SS_Salad_dressing.sort_values(['Trans_Share'],ascending = False)


# Filter Cum Transaction Share of 80%
if Condition_1=='TRANSACTION SHARE' and Condition_2 == 80:
    SS_SD_80_Trans_Share = SS_Salad_dressing[(SS_Salad_dressing['Trans_Share']>=0.8000)]

    # Concatenate words 
    SS_SD_80_Trans_Share_npA = np.array(SS_SD_80_Trans_Share.iloc[0:,0])
    SS_SD_80_Trans_Share_Jtxt = ' '.join(str(x) for x in SS_SD_80_Trans_Share_npA)
    SS_SD_80_Trans_Share_Jtxt = SS_SD_80_Trans_Share_Jtxt.replace("&","")
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for SS_SD_80_Trans_Share in SS_SD_80_Trans_Share_Jtxt.split():
       d[SS_SD_80_Trans_Share] += 1
    
    
    # In[41]:
    
    # Wordcloud 
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_SS_SD_80_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                    random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    mplt.imshow(WC_SS_SD_80_Trans_Share, interpolation='bilinear')
    SS_SD_title = mplt.title('SS Salad Dressing with 80% Transaction Share')
    mplt.setp(SS_SD_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+ 'WC_SS_SD_Trans_Share_80_Trans_Share.jpeg')

   
elif Condition_1=='TRANSACTION SHARE' and Condition_2 == 20:
    SS_SD_20_Trans_Share = SS_Salad_dressing[(SS_Salad_dressing['Trans_Share']<0.8000)]

    # Concatenate words 
    SS_SD_20_Trans_Share_npA = np.array(SS_SD_20_Trans_Share.iloc[0:,0])
    SS_SD_20_Trans_Share_Jtxt = ' '.join(str(x) for x in SS_SD_20_Trans_Share_npA)
    SS_SD_20_Trans_Share_Jtxt = SS_SD_20_Trans_Share_Jtxt.replace("&","")
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for SS_SD_20_Trans_Share in SS_SD_20_Trans_Share_Jtxt.split():
       d[SS_SD_20_Trans_Share] += 1
    
    
    # In[47]:
    
    # Wordcloud 
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    stop.add("8")
    WC_SS_SD_20_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,random_state=1,
            width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_SS_SD_20_Trans_Share, interpolation='bilinear')
    mplt.title('SS Salad Dressing with 20% Transaction Share')
    SS_SD_title = mplt.title('SS Salad Dressing with 20% Transaction Share')
    mplt.setp(SS_SD_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WC_SS_SD_Trans_Share_20_Trans_Share.jpeg')
    
elif Condition_1=='TRANSACTION SIZE' and Condition_2 == 'Small':
    SS_SD_df_Small = SS_SD_df_NZ[(SS_SD_df_NZ['Trans_Share']>=P1) &  (SS_SD_df_NZ['Trans_Share']<=P33)]

    # Concatenate words 
    SS_SD_df_Small_npA = np.array(SS_SD_df_Small.iloc[0:,0])
    SS_SD_df_Small_Jtxt = ' '.join(str(x) for x in SS_SD_df_Small_npA)
    SS_SD_df_Small_Jtxt = SS_SD_df_Small_Jtxt.replace("&","")
    
    
    # In[9]:
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for SS_SD_Trans_Share_Small in SS_SD_df_Small_Jtxt.split():
       d[SS_SD_Trans_Share_Small] += 1
    
    # Import wordcloud libraries
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_SS_SD_Trans_Share_Small = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                           random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_SS_SD_Trans_Share_Small, interpolation='bilinear')
    SS_SD_title = mplt.title('SS Salad Dressing with Small Transaction Share')
    mplt.setp(SS_SD_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WC_SS_SD_Trans_Share_Small.jpeg')
    
elif Condition_1=='TRANSACTION SIZE' and Condition_2 == 'Medium':
    SS_SD_df_Medium = SS_SD_df_NZ[(SS_SD_df_NZ['Trans_Share']>=P34) &  (SS_SD_df_NZ['Trans_Share']<=P66)]
    
    # Concatenate words 
    SS_SD_df_Medium_npA = np.array(SS_SD_df_Medium.iloc[0:,0])
    SS_SD_df_Medium_Jtxt = ' '.join(str(x) for x in SS_SD_df_Medium_npA)
    SS_SD_df_Medium_Jtxt = SS_SD_df_Medium_Jtxt.replace("&","")
    
    
    # In[14]:
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for SS_SD_Trans_Share_Medium in SS_SD_df_Medium_Jtxt.split():
       d[SS_SD_Trans_Share_Medium] += 1
    
    # Import wordcloud libraries
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_SS_SD_Trans_Share_Medium = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                           random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_SS_SD_Trans_Share_Medium, interpolation='bilinear')
    SS_SD_title = mplt.title('SS Salad Dressing with Medium Transaction Share')
    mplt.setp(SS_SD_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WC_SS_SD_Trans_Share_Medium.jpeg')
    
elif Condition_1=='TRANSACTION SIZE' and Condition_2 == 'High':
    SS_SD_df_High = SS_SD_df_NZ[(SS_SD_df_NZ['Trans_Share']>=P67) &  (SS_SD_df_NZ['Trans_Share']<=P100)]
    
    # Concatenate words 
    SS_SD_df_High_npA = np.array(SS_SD_df_High.iloc[0:,0])
    SS_SD_df_High_Jtxt = ' '.join(str(x) for x in SS_SD_df_High_npA)
    SS_SD_df_High_Jtxt = SS_SD_df_High_Jtxt.replace("&","")
    
    
    # In[17]:
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for SS_SD_Trans_Share_High in SS_SD_df_High_Jtxt.split():
       d[SS_SD_Trans_Share_High] += 1
    
    # Import wordcloud libraries
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_SS_SD_Trans_Share_High = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                           random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_SS_SD_Trans_Share_High, interpolation='bilinear')
    SS_SD_title = mplt.title('SS Salad Dressing with High Transaction Share')
    mplt.setp(SS_SD_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WC_SS_SD_Trans_Share_High.jpeg')
    
else:
    SS_SD_df_NZ_npA = np.array(SS_SD_df_NZ.iloc[0:,0])
    SS_SD_df_NZ_Jtxt = ' '.join(str(x) for x in SS_SD_df_NZ_npA)
    SS_SD_df_NZ_Jtxt = SS_SD_df_NZ_Jtxt.replace("&","")
    
    
    # In[17]:
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for SS_SD_Trans_Share_High in SS_SD_df_NZ_Jtxt.split():
       d[SS_SD_Trans_Share_High] += 1
    
    # Import wordcloud libraries
    stopwords_file = open(Stopword_inputpath+"stopwords.txt", "r")   
    stop = stopwords_file.read().split('\n')
    WC_SS_SD_Trans_Share_High = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                           random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_SS_SD_Trans_Share_High, interpolation='bilinear')
    SS_SD_title = mplt.title('SS Salad Dressing with Total Transaction Share')
    mplt.setp(SS_SD_title,color = 'r')
    mplt.axis("off")
    mplt.savefig(outputPath+'WC_SS_SD_Trans_Share_Total.jpeg')

############################################################################# END ################################################################################################