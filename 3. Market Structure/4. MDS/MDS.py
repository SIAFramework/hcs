# -*- coding: utf-8 -*-

from __future__ import division

import sys
import numpy as np
import pandas as pd
import time
import scipy.spatial.distance as sp
#import scipy.stats as stats
import json
import warnings

def cmdscale(D):
    """                                                                                       
    Classical multidimensional scaling (MDS)                                                  
                                                                                               
    Parameters                                                                                
    ----------                                                                                
    D : (n, n) array                                                                          
        Symmetric distance matrix.                                                            
                                                                                               
    Returns                                                                                   
    -------                                                                                   
    Y : (n, p) array                                                                          
        Configuration matrix. Each column represents a dimension. Only the                    
        p dimensions corresponding to positive eigenvalues of B are returned.                 
        Note that each dimension is only determined up to an overall sign,                    
        corresponding to a reflection.                                                        
                                                                                               
    e : (n,) array                                                                            
        Eigenvalues of B.                                                                     
                                                                                               
    """
    # Number of points                                                                        
    n = len(D)
 
    # Centering matrix                                                                        
    H = np.eye(n) - np.ones((n, n))/n
 
    # YY^T                                                                                    
    B = -H.dot(D**2).dot(H)/2
 
    # Diagonalize                                                                             
    evals, evecs = np.linalg.eigh(B)
 
    # Sort by eigenvalue in descending order                                                  
    idx   = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:,idx]
 
    # Compute the coordinates using positive-eigenvalued components only                      
    w, = np.where(evals > 0)
    L  = np.diag(np.sqrt(evals[w]))
    V  = evecs[:,w]
    Y  = V.dot(L)
 
    return Y, evals
    
start_time = time.time()

#inputPath = sys.argv[1]
inputPath='D:\\MarketStructureOnDemand\\Sweet_AffiliationMatrix.csv'
#'E:\\MSD\\MSD_Trunk\\MDS\\89_2_4245_179_270916_163529\\Input\\Sweet_AffiliationMatrix.csv'
#sys.argv[1];

#outputPath = sys.argv[2]
outputPath = 'D:\\MarketStructureOnDemand\\'
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

# Divide elements by 100\
div_100_data = 100/complete_data

# rename columns & index
div_100_data.columns = num_data.columns
div_100_data.index = num_data.columns

# check values > 3.33 : final data : Method-1 : replace it by 31
final_data = pd.DataFrame(np.where(div_100_data>3.33,31,complete_data))
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


# Replace NaN by zero
dist = np.nan_to_num(dist)


# In[119]:

#calculate X Y Coordinates by calling function which does 'Classical multidimensional scaling'
Y,evals = cmdscale(sp.squareform(dist))


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
