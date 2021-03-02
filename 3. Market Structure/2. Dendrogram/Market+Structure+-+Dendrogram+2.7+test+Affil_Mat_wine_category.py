
# coding: utf-8

# ## Market Structure: Dendrogram

# In[1]:

# Import libraries and dataset
import pandas as pd
import matplotlib.pyplot as mplt
import random
import scipy.spatial.distance as sp
import numpy as np
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist

data = pd.read_csv('D:/3. Market Structure/2. Dendrogram/walgreen_wine_3_affilliation_matrix.csv')
data_test = pd.read_csv('D:/3. Market Structure/2. Dendrogram/aff_matrix_04102017.csv')
del data_test['from']
del data_test['to']
data_test = squareform(data_test['AV'])
data_test = data_test.reshape(3,3)
data_test = np.array(data_test)
data_test = squareform(data_test)
data_test = data_test.as_matix(columns='from')

# Split the columns
data[['from_upc','to_upc','affiliation_value']] = data["'from_upc';'to_upc';'affiliation_value'"].str.split(';',expand=True)
del data["'from_upc';'to_upc';'affiliation_value'"]

data2 = data.iloc[0:8,]
data2=squareform(data2)

data = squareform(data)
data_label = data.iloc[0:53,0]
data_DD = data.iloc[0:54,1:54]
data_DD = np.array(data_DD)
np.fill_diagonal(data_DD,0)
#data_DD = data.iloc[:,1:]
#print(SS_Salad_dressing_DD.head(5))


# TRANSFORMATIONS
# Replace all values(upper or lower diagonal) zero values by 100
data_DD_repl_100 = np.array(data_DD)
data_DD_repl_100[data_DD_repl_100==0] = 100
np.fill_diagonal(data_DD_repl_100,0)


# Condtion : Divide 100/values & Replace values > 3.33 by 100
final_data = np.where((100/data_DD_repl_100) > 3.33,100, data_DD_repl_100)
np.fill_diagonal(final_data,0)

# 1/indicies
final_data = 1/final_data
np.fill_diagonal(final_data,0)

# Convert to square form : https://stackoverflow.com/questions/41416498/dendrogram-or-other-plot-from-distance-matrix
from scipy.spatial.distance import squareform
final_data = squareform(final_data)

# Replace values > 3.33 by 100
#final_data = pd.DataFrame(np.where(data_DD_repl_100_div>3.33,100,data_DD_repl_100_div))
#final_data = 1/data_DD
#final_data =np.array(final_data)
#np.fill_diagonal(final_data,0)

# Convert data into Class distance/array
from scipy.cluster import hierarchy
data_DD_Link = hierarchy.linkage(final_data,method = "average")

#from scipy.cluster.hierarchy import linkage
#Z = linkage(final_data, 'average')
#print(SS_Salad_dressing_DD_Link[0:5,:])

# Plot Dendrogam
Lable_list = data_label.tolist()

random.seed(1245)
hierarchy.dendrogram(data_DD_Link, show_contracted=True, labels=Lable_list)

mplt.close('close')
data_DD = mplt.title('Dendogram for Cereals data')
mplt.setp(data_DD,color = 'b')
mplt.xticks(rotation=90)
mplt.show()
