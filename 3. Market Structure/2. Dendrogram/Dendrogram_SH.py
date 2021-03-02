# ## Market Structure: Dendrogram


# Import libraries and dataset
import pandas as pd
import matplotlib.pyplot as mplt
import random
import scipy.spatial.distance as sp #squareform,pdist
import numpy as np


data = pd.read_csv('D:\\YASHWANTH\\3. Market Structure\\2. Dendrogram\\1. Input\\affiliation_matrix_test_transformation.csv')
#data = sp.squareform(data)
data_label = data.iloc[0:53,0]
data_DD = data.iloc[0:54,1:54]
data_DD = np.array(data_DD)
np.fill_diagonal(data_DD,0)


# TRANSFORMATIONS
# Replace all values(upper or lower diagonal) zero values by 100
data_DD_repl_100 = np.array(data_DD)
data_DD_repl_100[data_DD_repl_100==0] = 100
np.fill_diagonal(data_DD_repl_100,0)


# Condtion : Divide 100/values & Replace values > 3.33 by 100
final_data = np.where((100/data_DD_repl_100) > 3.33,100, data_DD_repl_100)
np.fill_diagonal(final_data,0)

# 1/indicies
final_data = data_DD_repl_100
final_data = 1/final_data
np.fill_diagonal(final_data,0)

# Convert to square form
from scipy.spatial.distance import squareform
final_data = squareform(final_data)


# Convert data into Class distance/array
from scipy.cluster import hierarchy
data_DD_Link = hierarchy.linkage(final_data,method = "average")

# Plot Dendrogam
Lable_list = data_label.tolist()

random.seed(1245)
hierarchy.dendrogram(data_DD_Link, show_contracted=True, labels=Lable_list)

mplt.close('close')
data_DD = mplt.title('Dendogram for Cereals data')
mplt.setp(data_DD,color = 'b')
mplt.xticks(rotation=90)
mplt.show()
