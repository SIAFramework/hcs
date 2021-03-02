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

Condition_file = pd.read_csv(inputpath +'Condition.csv',sep = '|')
Condition_1 = Condition_file.iloc[0,0]
Condition_2 = Condition_file.iloc[0,1]
SS_Salad_dressing = pd.read_csv(inputpath +'WC_SS_Salad_dressing.csv')
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

    # Filter Cum Transaction Share of 80%
    SS_SD_80_Trans_Share = SS_Salad_dressing[(SS_Salad_dressing['Trans_Share']>=0.8000)]
    SS_SD_80_Trans_Share = SS_SD_80_Trans_Share.sort_values(by='Trans_Share_Cumsum',ascending=True)
    print(SS_SD_80_Trans_Share.head(5))
    
    
    # Concatenate words 
    SS_SD_80_Trans_Share_npA = np.array(SS_SD_80_Trans_Share.iloc[0:,0])
    print(len(SS_SD_80_Trans_Share_npA))
    SS_SD_80_Trans_Share_Jtxt = ' '.join(str(x) for x in SS_SD_80_Trans_Share_npA)
    SS_SD_80_Trans_Share_Jtxt = SS_SD_80_Trans_Share_Jtxt.replace("&","")
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for SS_SD_80_Trans_Share in SS_SD_80_Trans_Share_Jtxt.split():
       d[SS_SD_80_Trans_Share] += 1
    
    
    # Wordcloud 
    stop = set(nltk.corpus.stopwords.words('english'))
    WC_SS_SD_80_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                    random_state=1,width=1600,height=1400).generate_from_frequencies(d)
    mplt.imshow(WC_SS_SD_80_Trans_Share, interpolation='bilinear')
    SS_SD_title = mplt.title('SS Salad Dressing with 80% Transaction Share')
    mplt.setp(SS_SD_title,color = 'r')
    mplt.axis("off")
    mplt.savefig('D:/3. Market Structure/1. WordCloud/6. Output/WC_SS_SD_Trans_Share_80_Trans_Share.jpeg')

   
else:
    SS_SD_20_Trans_Share = SS_Salad_dressing[(SS_Salad_dressing['Trans_Share']<0.8000)]
    SS_SD_20_Trans_Share = SS_SD_20_Trans_Share.sort_values(by='Trans_Share_Cumsum',ascending=True)
    
    # Concatenate words 
    SS_SD_20_Trans_Share_npA = np.array(SS_SD_20_Trans_Share.iloc[0:,0])
    print(len(SS_SD_20_Trans_Share_npA))
    SS_SD_20_Trans_Share_Jtxt = ' '.join(str(x) for x in SS_SD_20_Trans_Share_npA)
    SS_SD_20_Trans_Share_Jtxt = SS_SD_20_Trans_Share_Jtxt.replace("&","")
    
    # Function to create TermDocumentMatrix
    from collections import defaultdict
    d = defaultdict(int)
    for SS_SD_20_Trans_Share in SS_SD_20_Trans_Share_Jtxt.split():
       d[SS_SD_20_Trans_Share] += 1
    
    
    # Wordcloud 
    import wordcloud as wc
    import nltk
    stopwords = set(nltk.corpus.stopwords.words('english'))
    stopwords.add("8")
    WC_SS_SD_20_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stopwords,random_state=1,
            width=1600,height=1400).generate_from_frequencies(d)
    
    mplt.imshow(WC_SS_SD_20_Trans_Share, interpolation='bilinear')
    mplt.title('SS Salad Dressing with 20% Transaction Share')
    SS_SD_title = mplt.title('SS Salad Dressing with 20% Transaction Share')
    mplt.setp(SS_SD_title,color = 'r')
    mplt.axis("off")
    mplt.savefig('D:/3. Market Structure/1. WordCloud/6. Output/WC_SS_SD_Trans_Share_20_Trans_Share.jpeg')

# In[47]:
    
#Condition_1 = Condition_file.iloc[0,0]
#Condition_2 = Condition_file.iloc[0,1]
#if Condition_1 =='TRANSACTION SHARE' and Condition_2==80:
#    print("Yes")
#else:
 #   print("No")
    
############################################################################# END ################################################################################################