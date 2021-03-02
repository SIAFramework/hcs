
# coding: utf-8

# ## Market Structure: Dendrogram

# In[1]:

# Import libraries and dataset
import pandas as pd
import matplotlib.pyplot as mplt
import random
import scipy.spatial.distance as sp

SS_Salad_dressing_IP = pd.read_csv('D:/3. Market Structure/2. Dendrogram/Salad dressing2.csv')
#sp.squareform(dist)


SS_Salad_dressing_DD = SS_Salad_dressing_IP.iloc[:,1:]
#print(SS_Salad_dressing_DD.head(5))



# Convert data into Class distance/array
from scipy.cluster import hierarchy
SS_Salad_dressing_DD_Link = hierarchy.linkage(SS_Salad_dressing_DD,method = "average",)
#print(SS_Salad_dressing_DD_Link[0:5,:])

# Plot Dendrogam
Lable_list = SS_Salad_dressing_IP['Attribute_Value_Name'].tolist()

random.seed(1245)
hierarchy.dendrogram(SS_Salad_dressing_DD_Link, show_contracted=True, labels=Lable_list)

mplt.close('close')
SS_SD_DD = mplt.title('Dendogram for Salad dressing')
mplt.setp(SS_SD_DD,color = 'b')
mplt.xticks(rotation=90)
mplt.show()

