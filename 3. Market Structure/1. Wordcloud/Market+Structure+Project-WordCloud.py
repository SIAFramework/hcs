
# # Introduction to Data Science - IRi

# ## Word Cloud


# Check python version
import sys
print(sys.version)


# ### SS Salad Dressing

# Import libraries and dataset
import pandas as pd
import wordcloud as wc
import numpy as np
import matplotlib.pyplot as mplt
import random
from os import path
from PIL import Image
pd.set_option('display.max_columns',500)

inputpath = 'D:/YASHWANTH/3. Market Structure/1. WordCloud/1. Input files/'
SS_Salad_dressing = pd.read_csv(inputpath +'WC_SS_Salad_dressing_Combine.csv')
SS_Salad_dressing['Trans_Share'] = SS_Salad_dressing['Trans_Share']*100
print(SS_Salad_dressing.head(5))

# Sort by Transaction Count
SS_Salad_dressing = SS_Salad_dressing.sort_values(by = 'Trans_Share',ascending=False)



# Seperate out data based on Quartiles as Small, Medium & High Transaction Share
SS_SD_df = SS_Salad_dressing
SS_SD_df_NZ = SS_SD_df.query('Trans_Share>0')
print(SS_SD_df_NZ.head(5))
#SS_SD_df_NZ['quan'] = pd.qcut(SS_SD_df_NZ.iloc[0:,2],q=3)
#print(SS_SD_df_NZ['quan'].head(5))
#print(SS_SD_df_NZ.shape)


P1=np.percentile(SS_SD_df_NZ.iloc[0:,2],1)
P33=np.percentile(SS_SD_df_NZ.iloc[0:,2],33)
P34=np.percentile(SS_SD_df_NZ.iloc[0:,2],34)
P66=np.percentile(SS_SD_df_NZ.iloc[0:,2],66)
P67=np.percentile(SS_SD_df_NZ.iloc[0:,2],67)
P100=np.percentile(SS_SD_df_NZ.iloc[0:,2],100)


SS_SD_df_Small = SS_SD_df_NZ[(SS_SD_df_NZ['Trans_Share']>=P1) &  (SS_SD_df_NZ['Trans_Share']<=P33)]
SS_SD_df_Medium = SS_SD_df_NZ[(SS_SD_df_NZ['Trans_Share']>=P34) &  (SS_SD_df_NZ['Trans_Share']<=P66)]
SS_SD_df_High = SS_SD_df_NZ[(SS_SD_df_NZ['Trans_Share']>=P67) &  (SS_SD_df_NZ['Trans_Share']<=P100)]

print(SS_SD_df_Small.head(5),SS_SD_df_Medium.head(5),SS_SD_df_High.head(5))

# ### Pareto Rule


# Cummulative sum 
SS_Salad_dressing['No_of_Trans_Cumsum'] = SS_Salad_dressing['No_of_Trans'].cumsum()
SS_Salad_dressing['Trans_Share_Cumsum'] = SS_Salad_dressing['Trans_Share'].cumsum()
SS_Salad_dressing = SS_Salad_dressing.sort_values(['Trans_Share'],ascending = False)

# Filter Cum Transaction Share of 80%
SS_SD_80_Trans_Share = SS_Salad_dressing[(SS_Salad_dressing['Trans_Share']>=0.8000)]
SS_SD_80_Trans_Share = SS_SD_80_Trans_Share.sort_values(by='Trans_Share_Cumsum',ascending=True)
print(SS_SD_80_Trans_Share.head(5))



# Concatenate words 
import string
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
import nltk
stopwords_file = open(inputpath+"stopwords.txt", "r")   
stop = stopwords_file.read().split('\n')
#stop = set(nltk.corpus.stopwords.words('english'))
WC_SS_SD_80_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                random_state=1,width=1600,height=1400).generate_from_frequencies(d)
mplt.imshow(WC_SS_SD_80_Trans_Share, interpolation='bilinear')
SS_SD_title = mplt.title('SS Salad Dressing with 80% Transaction Share')
mplt.setp(SS_SD_title,color = 'r')
mplt.axis("off")
mplt.show()
mplt.savefig('D:/3. Market Structure/1. WordCloud/6. Output/WC_SS_SD_Trans_Share_80_Trans_Share.jpeg')



# Filter Cum Transaction Share of 20% 
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
stopwords_file = open(inputpath+"stopwords.txt", "r")
stop = stopwords_file.read().split('\n')
#stopwords = set(nltk.corpus.stopwords.words('english'))
stop.append("8")
WC_SS_SD_20_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,random_state=1,
        width=1600,height=1400).generate_from_frequencies(d)

mplt.imshow(WC_SS_SD_20_Trans_Share, interpolation='bilinear')
mplt.title('SS Salad Dressing with 20% Transaction Share')
SS_SD_title = mplt.title('SS Salad Dressing with 20% Transaction Share')
mplt.setp(SS_SD_title,color = 'r')
mplt.axis("off")
mplt.show()
mplt.savefig('D:/3. Market Structure/1. WordCloud/6. Output/WC_SS_SD_Trans_Share_20_Trans_Share.jpeg')


# ### WordCloud : Small Transaction Share


# Concatenate words 
SS_SD_df_Small_npA = np.array(SS_SD_df_Small.iloc[0:,0])
print(len(SS_SD_df_Small_npA))
SS_SD_df_Small_Jtxt = ' '.join(str(x) for x in SS_SD_df_Small_npA)
SS_SD_df_Small_Jtxt = SS_SD_df_Small_Jtxt.replace("&","")
print(SS_SD_df_Small_Jtxt)



# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for SS_SD_Trans_Share_Small in SS_SD_df_Small_Jtxt.split():
   d[SS_SD_Trans_Share_Small] += 1

# Import wordcloud libraries
stopwords_file = open(inputpath+"stopwords.txt", "r")   
stop = stopwords_file.read().split('\n')
#stop = set(nltk.corpus.stopwords.words('english'))
WC_SS_SD_Trans_Share_Small = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                       random_state=1,width=1600,height=1400).generate_from_frequencies(d)

mplt.imshow(WC_SS_SD_Trans_Share_Small, interpolation='bilinear')
SS_SD_title = mplt.title('SS Salad Dressing with Small Transaction Share')
mplt.setp(SS_SD_title,color = 'r')
mplt.axis("off")
mplt.show()
mplt.savefig('D:/3. Market Structure/1. WordCloud/6. Output/WC_SS_SD_Trans_Share_Small.jpeg')


# ### WordCloud : Medium Transaction Share


# Concatenate words 
SS_SD_df_Medium_npA = np.array(SS_SD_df_Medium.iloc[0:,0])
print(len(SS_SD_df_Medium_npA))
SS_SD_df_Medium_Jtxt = ' '.join(str(x) for x in SS_SD_df_Medium_npA)
SS_SD_df_Medium_Jtxt = SS_SD_df_Medium_Jtxt.replace("&","")
print(SS_SD_df_Medium_Jtxt)



# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for SS_SD_Trans_Share_Medium in SS_SD_df_Medium_Jtxt.split():
   d[SS_SD_Trans_Share_Medium] += 1

# Import wordcloud libraries
stopwords_file = open(inputpath+"stopwords.txt", "r")   
stop = stopwords_file.read().split('\n')
#stop = set(nltk.corpus.stopwords.words('english'))
WC_SS_SD_Trans_Share_Medium = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                       random_state=1,width=1600,height=1400).generate_from_frequencies(d)

mplt.imshow(WC_SS_SD_Trans_Share_Medium, interpolation='bilinear')
SS_SD_title = mplt.title('SS Salad Dressing with Medium Transaction Share')
mplt.setp(SS_SD_title,color = 'r')
mplt.axis("off")
mplt.show()
mplt.savefig('D:/3. Market Structure/1. WordCloud/6. Output/WC_SS_SD_Trans_Share_Medium.jpeg')


# ### WordCloud : High Transaction Share


# Concatenate words 
SS_SD_df_High_npA = np.array(SS_SD_df_High.iloc[0:,0])
print(len(SS_SD_df_High_npA))
SS_SD_df_High_Jtxt = ' '.join(str(x) for x in SS_SD_df_High_npA)
SS_SD_df_High_Jtxt = SS_SD_df_High_Jtxt.replace("&","")
print(SS_SD_df_High_Jtxt)



# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for SS_SD_Trans_Share_High in SS_SD_df_High_Jtxt.split():
   d[SS_SD_Trans_Share_High] += 1

# Import wordcloud libraries
stopwords_file = open(inputpath+"stopwords.txt", "r")   
stop = stopwords_file.read().split('\n')
#stop = set(nltk.corpus.stopwords.words('english'))
WC_SS_SD_Trans_Share_High = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                       random_state=1,width=1600,height=1400).generate_from_frequencies(d)

mplt.imshow(WC_SS_SD_Trans_Share_High, interpolation='bilinear')
SS_SD_title = mplt.title('SS Salad Dressing with High Transaction Share')
mplt.setp(SS_SD_title,color = 'r')
mplt.axis("off")
mplt.show()
mplt.savefig('D:/3. Market Structure/1. WordCloud/6. Output/WC_SS_SD_Trans_Share_High.jpeg')


# All attributes
# Concatenate words 
#SS_SD_df_NZ[(SS_SD_df_NZ['Trans_Share']>=P1) &  (SS_SD_df_NZ['Trans_Share']<=P33)]
SS_Salad_dressing = SS_Salad_dressing[SS_Salad_dressing['Trans_Share']>1]
SS_Salad_dressing_npA = np.array(SS_Salad_dressing.iloc[0:,0])
print(len(SS_Salad_dressing_npA))
SS_Salad_dressing_Jtxt = ' '.join(str(x) for x in SS_Salad_dressing_npA)
SS_Salad_dressing_Jtxt = SS_Salad_dressing_Jtxt.replace("&","")

# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for SS_Salad_dressing in SS_Salad_dressing_Jtxt.split():
   d[SS_Salad_dressing] += 1



# Wordcloud 
stopwords_file = open(inputpath+"stopwords.txt", "r")   
stop = stopwords_file.read().split('\n')
#stop = set(nltk.corpus.stopwords.words('english'))
WC_SS_Salad_dressing = wc.WordCloud(background_color='white',max_words=1000,stopwords=stop,
                random_state=1,width=1600,height=1400).generate_from_frequencies(d)
mplt.imshow(WC_SS_Salad_dressing, interpolation='bilinear')
SS_SD_title = mplt.title('SS Salad Dressing with Total Transaction Share')
mplt.setp(SS_SD_title,color = 'r')
mplt.axis("off")
mplt.show()
mplt.savefig('D:/3. Market Structure/1. WordCloud/6. Output/WC_SS_SD_Trans_Share_Total.jpeg')






# ### Rfg Salad Dressing

Rfg_Salad_dressing = pd.read_csv(inputpath+'WC_Rfg_Salad_dressing_Combine.csv')

# Sort by Transaction Count
Rfg_Salad_dressing['Trans_Share'] = Rfg_Salad_dressing['Trans_Share']*100
Rfg_Salad_dressing = Rfg_Salad_dressing.sort_values(by = 'Trans_Share',ascending=False)
Rfg_SD_df = Rfg_Salad_dressing
Rfg_SD_df_NZ = Rfg_SD_df.query('Trans_Share>0')
print(Rfg_SD_df_NZ.head(5))


P1=np.percentile(Rfg_SD_df_NZ.iloc[0:,2],1)
P33=np.percentile(Rfg_SD_df_NZ.iloc[0:,2],33)
P34=np.percentile(Rfg_SD_df_NZ.iloc[0:,2],34)
P66=np.percentile(Rfg_SD_df_NZ.iloc[0:,2],66)
P67=np.percentile(Rfg_SD_df_NZ.iloc[0:,2],67)
P100=np.percentile(Rfg_SD_df_NZ.iloc[0:,2],100)


Rfg_SD_df_Small = Rfg_SD_df_NZ[(Rfg_SD_df_NZ['Trans_Share']>=P1) &  (Rfg_SD_df_NZ['Trans_Share']<=P33)]
Rfg_SD_df_Medium = Rfg_SD_df_NZ[(Rfg_SD_df_NZ['Trans_Share']>=P34) &  (Rfg_SD_df_NZ['Trans_Share']<=P66)]
Rfg_SD_df_High = Rfg_SD_df_NZ[(Rfg_SD_df_NZ['Trans_Share']>=P67) &  (Rfg_SD_df_NZ['Trans_Share']<=P100)]


# Seperate out data based on Quartiles as Small, Medium & High Transaction Share
Rfg_SD_df = Rfg_Salad_dressing
Rfg_SD_df_NZ = Rfg_SD_df.query('Trans_Share>0')
Rfg_SD_df_NZ.index = range(0,len(Rfg_SD_df_NZ))
#print(Rfg_SD_df_NZ.head(5))
#Rfg_SD_df_NZ['quan'] = pd.qcut(Rfg_SD_df_NZ.iloc[0:,2],q=3)
#print(Rfg_SD_df_NZ['quan'].head(5))
#print(Rfg_SD_df_NZ.shape)

Rfg_SD_df_Small = pd.DataFrame(Rfg_SD_df_NZ.query('0.0001<=Trans_Share<=0.0003'))
Rfg_SD_df_Medium = pd.DataFrame(Rfg_SD_df_NZ.query('0.0004<=Trans_Share<=0.002'))
Rfg_SD_df_High = pd.DataFrame(Rfg_SD_df_NZ.query('0.003<=Trans_Share<=1'))

print(Rfg_SD_df_Small.head(5),Rfg_SD_df_Medium.head(5),Rfg_SD_df_High.head(5))


# ### WordCloud : Small Transaction Share


# Concatenate words 
Rfg_SD_df_Small_npA = np.array(Rfg_SD_df_Small.iloc[0:,0])
print(len(Rfg_SD_df_Small_npA))
Rfg_SD_df_Small_Jtxt = ' '.join(str(x) for x in Rfg_SD_df_Small_npA)
Rfg_SD_df_Small_Jtxt = Rfg_SD_df_Small_Jtxt.replace("&","")
print(Rfg_SD_df_Small_Jtxt)



# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for Rfg_SD_Trans_Share_Small in Rfg_SD_df_Small_Jtxt.split():
   d[Rfg_SD_Trans_Share_Small] += 1

# Import wordcloud libraries
stopwords_file = open(inputpath+"stopwords.txt", "r")
stop = stopwords_file.read().split('\n')
stop.append("english")

#stop = set(nltk.corpus.stopwords.words('english'))
WC_Rfg_SD_Trans_Share_Small = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                       random_state=1,width=1600,height=1400).generate_from_frequencies(d)

mplt.imshow(WC_Rfg_SD_Trans_Share_Small, interpolation='bilinear')
Rfg_SD_title = mplt.title('Rfg Salad Dressing with Small Transaction Share')
mplt.setp(Rfg_SD_title,color = 'r')
mplt.axis("off")
mplt.show()


# ### WordCloud : Medium Transaction Share


# Concatenate words 
Rfg_SD_df_Medium_npA = np.array(Rfg_SD_df_Medium.iloc[0:,0])
print(len(Rfg_SD_df_Medium_npA))
Rfg_SD_df_Medium_Jtxt = ' '.join(str(x) for x in Rfg_SD_df_Medium_npA)
Rfg_SD_df_Medium_Jtxt = Rfg_SD_df_Medium_Jtxt.replace("&","")
print(Rfg_SD_df_Medium_Jtxt)



# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for Rfg_SD_Trans_Share_Medium in Rfg_SD_df_Medium_Jtxt.split():
   d[Rfg_SD_Trans_Share_Medium] += 1

# Import wordcloud libraries
#stop = set(nltk.corpus.stopwords.words('english'))
WC_Rfg_SD_Trans_Share_Medium = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                       random_state=1,width=1600,height=1400).generate_from_frequencies(d)

mplt.imshow(WC_Rfg_SD_Trans_Share_Medium, interpolation='bilinear')
Rfg_SD_title = mplt.title('Rfg Salad Dressing with Medium Transaction Share')
mplt.setp(Rfg_SD_title,color = 'r')
mplt.axis("off")
mplt.show()


# ### WordCloud : High Transaction Share

# Concatenate words 
Rfg_SD_df_High_npA = np.array(Rfg_SD_df_High.iloc[0:,0])
print(len(Rfg_SD_df_High_npA))
Rfg_SD_df_High_Jtxt = ' '.join(str(x) for x in Rfg_SD_df_High_npA)
Rfg_SD_df_High_Jtxt = Rfg_SD_df_High_Jtxt.replace("&","")
print(Rfg_SD_df_High_Jtxt)




# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for Rfg_SD_Trans_Share_High in Rfg_SD_df_High_Jtxt.split():
   d[Rfg_SD_Trans_Share_High] += 1

# Import wordcloud libraries
#stop = set(nltk.corpus.stopwords.words('english'))
WC_Rfg_SD_Trans_Share_High = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                                       random_state=1,width=1600,height=1400).generate_from_frequencies(d)

mplt.imshow(WC_Rfg_SD_Trans_Share_High, interpolation='bilinear')
Rfg_SD_title = mplt.title('Rfg Salad Dressing with High Transaction Share')
mplt.setp(Rfg_SD_title,color = 'r')
mplt.axis("off")
mplt.show()


# ### Pareto Rule


# Cummulative sum 
Rfg_Salad_dressing['No_of_Trans_Cumsum'] = Rfg_Salad_dressing['No_of_Trans'].cumsum()
Rfg_Salad_dressing['Trans_Share_Cumsum'] = Rfg_Salad_dressing['Trans_Share'].cumsum()
Rfg_Salad_dressing = Rfg_Salad_dressing.sort_values(['Trans_Share'],ascending = False)

# Filter Cum Transaction Share of 80% 
Rfg_SD_80_Trans_Share = Rfg_Salad_dressing.query('Trans_Share_Cumsum >= .8021')
Rfg_SD_80_Trans_Share = Rfg_SD_80_Trans_Share.sort_values(by='Trans_Share_Cumsum',ascending=True)
print(Rfg_SD_80_Trans_Share.head(5))



# Concatenate words 
Rfg_SD_80_Trans_Share_npA = np.array(Rfg_SD_80_Trans_Share.iloc[0:,0])
print(len(Rfg_SD_80_Trans_Share_npA))
Rfg_SD_80_Trans_Share_Jtxt = ' '.join(str(x) for x in Rfg_SD_80_Trans_Share_npA)
Rfg_SD_80_Trans_Share_Jtxt = Rfg_SD_80_Trans_Share_Jtxt.replace("&","")

# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for Rfg_SD_80_Trans_Share in Rfg_SD_80_Trans_Share_Jtxt.split():
   d[Rfg_SD_80_Trans_Share] += 1



# Wordcloud 
stop = set(nltk.corpus.stopwords.words('english'))
WC_Rfg_SD_80_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                random_state=1,width=1600,height=1400).generate_from_frequencies(d)

mplt.imshow(WC_Rfg_SD_80_Trans_Share, interpolation='bilinear')
Rfg_SD_title = mplt.title('Rfg Salad Dressing with 80% Transaction Share')
mplt.setp(Rfg_SD_title,color = 'r')
mplt.axis("off")
mplt.show()



# Filter Cum Transaction Share of 80% 
Rfg_SD_20_Trans_Share = Rfg_Salad_dressing.query('Trans_Share_Cumsum < .8021')
Rfg_SD_20_Trans_Share = Rfg_SD_20_Trans_Share.sort_values(by='Trans_Share_Cumsum',ascending=True)

# Concatenate words 
Rfg_SD_20_Trans_Share_npA = np.array(Rfg_SD_20_Trans_Share.iloc[0:,0])
print(len(Rfg_SD_20_Trans_Share_npA))
Rfg_SD_20_Trans_Share_Jtxt = ' '.join(str(x) for x in Rfg_SD_20_Trans_Share_npA)
Rfg_SD_20_Trans_Share_Jtxt = Rfg_SD_20_Trans_Share_Jtxt.replace("&","")

# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for Rfg_SD_20_Trans_Share in Rfg_SD_20_Trans_Share_Jtxt.split():
   d[Rfg_SD_20_Trans_Share] += 1



# Wordcloud 
stop = set(nltk.corpus.stopwords.words('english'))
WC_Rfg_SD_20_Trans_Share = wc.WordCloud(background_color='black',max_words=1000,stopwords=stop,
                random_state=1,width=1600,height=1400).generate_from_frequencies(d)

mplt.imshow(WC_Rfg_SD_20_Trans_Share, interpolation='bilinear')
Rfg_SD_title = mplt.title('Rfg Salad Dressing with 20% Transaction Share')
mplt.setp(Rfg_SD_title,color = 'r')
mplt.axis("off")
mplt.show()


# All attributes
# Concatenate words 
#SS_SD_df_NZ[(SS_SD_df_NZ['Trans_Share']>=P1) &  (SS_SD_df_NZ['Trans_Share']<=P33)]
Rfg_Salad_dressing = Rfg_Salad_dressing[Rfg_Salad_dressing['Trans_Share']>1]
Rfg_Salad_dressing_npA = np.array(Rfg_Salad_dressing.iloc[0:,0])
print(len(Rfg_Salad_dressing_npA))
Rfg_Salad_dressing_Jtxt = ' '.join(str(x) for x in Rfg_Salad_dressing_npA)
Rfg_Salad_dressing_Jtxt = Rfg_Salad_dressing_Jtxt.replace("&","")

# Function to create TermDocumentMatrix
from collections import defaultdict
d = defaultdict(int)
for Rfg_Salad_dressing in Rfg_Salad_dressing_Jtxt.split():
   d[Rfg_Salad_dressing] += 1



# Wordcloud
stopwords_file = open(inputpath+"stopwords.txt", "r")   
stop = stopwords_file.read().split('\n')
#stop = set(nltk.corpus.stopwords.words('english'))
WC_Rfg_Salad_dressing = wc.WordCloud(background_color='white',max_words=1000,stopwords=stop,
                random_state=1,width=1600,height=1400).generate_from_frequencies(d)
mplt.imshow(WC_Rfg_Salad_dressing, interpolation='bilinear')
SS_SD_title = mplt.title('Rfg Salad Dressing with Total Transaction Share')
mplt.setp(SS_SD_title,color = 'r')
mplt.axis("off")
mplt.show()
mplt.savefig('D:/3. Market Structure/1. WordCloud/6. Output/WC_SS_SD_Trans_Share_Total.jpeg')

############################################################################# END ################################################################################################