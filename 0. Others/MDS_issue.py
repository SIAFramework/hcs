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

inputPath = sys.argv[1]
#'E:\\MSD\\MSD_Trunk\\MDS\\89_2_4245_179_270916_163529\\Input\\AffiliationMatrix.csv'
#sys.argv[1];

outputPath = sys.argv[2]
#'E:\\MSD\\MSD_Trunk\\MDS\\89_2_4245_179_270916_163529\\Output\\'
#sys.argv[2];

data = pd.read_csv(inputPath, index_col=0, sep='|')

#convert data to numeric data type
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    num_data = data.convert_objects(convert_numeric=True)

#fill NaN with -1
complete_data = num_data.fillna(-1)

#replace zeros with -1
replace_zero_data = complete_data.replace(to_replace=0.0, value=-1)

#inverse data
inverse_data = 1/replace_zero_data

#Override or fill diagnols with zeros
np.fill_diagonal(inverse_data.values,0)

#convert to euclidean distance matrix
dist = sp.pdist(inverse_data)

#calculate X Y Coordinates by calling function which does 'Classical multidimensional scaling'
Y,evals = cmdscale(sp.squareform(dist))

#Output data to CSV
Z = np.around( Y[:,:2],decimals=4)
pd.DataFrame(Z).to_csv(outputPath + 'Points.csv', header=False, index=False)

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
