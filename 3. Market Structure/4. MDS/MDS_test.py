# -*- coding: utf-8 -*-

# Import libraries
from __future__ import division

import sys
import numpy as np
import pandas as pd
import time
import scipy.spatial.distance as sp
import scipy.stats as stats
import json
import warnings
import sklearn

    
start_time = time.time()

inputPath = sys.argv[1]
#'E:\\MSD\\MSD_Trunk\\MDS\\89_2_4245_179_270916_163529\\Input\\AffiliationMatrix.csv'
#sys.argv[1];

outputPath = sys.argv[2]
#'E:\\MSD\\MSD_Trunk\\MDS\\89_2_4245_179_270916_163529\\Output\\'
#sys.argv[2];


# In[59]:

# Import dataset
data = pd.read_csv(inputPath, index_col=0, sep='|')

#convert data to numeric data type
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    num_data = data.convert_objects(convert_numeric=True)


# In[65]:

#fill NaN with -1
complete_data = num_data.fillna(-1)


#replace zeros with NaN
replace_zero_data = complete_data.replace(to_replace=0.0, value="NaN")
replace_zero_data = replace_zero_data.astype(float)


# Divide elements by 100\
div_100_data = 100/replace_zero_data

# rename columns & index
div_100_data.columns = num_data.columns
div_100_data.index = num_data.columns


# check values > 3.33 : final data
final_data = pd.DataFrame(np.where(div_100_data>3.33,"NaN",replace_zero_data))
final_data = final_data.astype(float)

# rename columns & index
final_data.columns = num_data.columns
final_data.index = final_data.columns


# In[118]:

#inverse data
inverse_data = 1/final_data


# Override or fill diagnols with zeros
np.fill_diagonal(inverse_data.values,0)


# convert to euclidean distance matrix
dist = sp.pdist(inverse_data)
dist = dist*100


# Replace NaN by zero
dist = np.nan_to_num(dist)


# In[119]:

# MDS using sklearn
from sklearn import manifold
mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=124,
                   dissimilarity="precomputed", n_jobs=1)

pos = mds.fit(sp.squareform(dist)).embedding_

nmds = manifold.MDS(n_components=2, metric=False, max_iter=3000, eps=1e-12, dissimilarity="precomputed", 
                    random_state=12656, n_jobs=1,n_init=1)
npos = nmds.fit_transform(sp.squareform(dist), init=pos)
Y=npos

# In[120]:

#Output data to CSV
Z = np.around( Y[:,:2],decimals=4)
pd.DataFrame(Z).to_csv(outputPath + 'Points.csv', header=False, index=False)
#print(Z)


# In[124]:

new_dist = sp.pdist(Y[:,:2])

r = np.corrcoef(dist, new_dist)[0, 1]

r_squared = r*r


freedom = len(new_dist) - 2


Fvalue = r_squared /((1 - r_squared)/freedom)



#pf = stats.f.sf(Fvalue, 1, freedom, loc=0, scale=1)

with open(outputPath + "Statistics.json","w") as outfile:
    json.dump({'rSquared' : r_squared, 'freedom' : freedom, 'fValue' : Fvalue}, outfile,)
outfile.close()

diff = (time.time() - start_time)*1000
#print(diff)
