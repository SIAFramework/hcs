# -*- coding: utf-8 -*-

from __future__ import division

#import sys
import numpy as np
import pandas as pd
import time
import scipy.spatial.distance as sp
#import scipy.stats as stats
import json
import warnings
import matplot.lib as mplt

from matplotlib.collections import LineCollection

from sklearn import manifold
from sklearn.metrics import euclidean_distances
#from sklearn.decomposition import PCA

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
inputPath='D:/3. Market Structure/4. Switch Index/Old Avg Indices.csv'
#'E:\\MSD\\MSD_Trunk\\MDS\\89_2_4245_179_270916_163529\\Input\\Sweet_AffiliationMatrix.csv'
#sys.argv[1];

#outputPath = sys.argv[2]
outputPath = 'D:/3. Market Structure/4. Switch Index/'
#'E:\\MSD\\MSD_Trunk\\MDS\\89_2_4245_179_270916_163529\\Output\\'
#sys.argv[2];


# Import dataset
data = pd.read_csv(inputPath, index_col=0, sep=',')

#convert data to numeric data type
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    num_data = data.convert_objects(convert_numeric=True)


#fill NaN with -1
complete_data = num_data.fillna(-1)

# Divide elements by 100\
div_100_data = 100/complete_data

# rename columns & index
div_100_data.columns = num_data.columns
div_100_data.index = num_data.columns

# check values > 3.33 : final data : Method-2 : replace it by 100
final_data = pd.DataFrame(np.where(div_100_data>3.33,100,complete_data))
final_data = final_data.astype(float)

# rename columns & index
final_data.columns = num_data.columns
final_data.index = final_data.columns


#inverse data
inverse_data = 1/final_data


# Override or fill diagnols with zeros
np.fill_diagonal(inverse_data.values,0)


# convert to euclidean distance matrix
dist = sp.pdist(inverse_data)


# Replace NaN by zero
dist = np.nan_to_num(dist)


#calculate X Y Coordinates by calling function which does 'Classical multidimensional scaling'
Y,evals = cmdscale(sp.squareform(dist))


#Output data to CSV
Z = np.around( Y[:,:2],decimals=4)
pd.DataFrame(Z).to_csv(outputPath + 'Points.csv', header=False, index=False)
#print(Z)


new_dist = sp.pdist(Y[:,:2])

#r = np.corrcoef(dist, new_dist)[0, 1]

#r_squared = r*r
# https://stats.stackexchange.com/questions/22019/how-to-calculate-the-r-squared-value-and-assess-the-model-fit-in-multidimensiona
r_squared = sum(evals[0:2])/sum(abs(i) for i in evals)


freedom = len(new_dist) - 2


Fvalue = r_squared /((1 - r_squared)/freedom)



#pf = stats.f.sf(Fvalue, 1, freedom, loc=0, scale=1)

with open(outputPath + "Statistics.json","w") as outfile:
    json.dump({'rSquared' : r_squared, 'freedom' : freedom, 'fValue' : Fvalue}, outfile,)
outfile.close()

diff = (time.time() - start_time)*1000
#print(diff)


new_dist_MDS = euclidean_distances(inverse_data)
seed = np.random.RandomState(seed=3)
new_dist_MDS_mean = new_dist_MDS.mean()
mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=seed,
                   dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(new_dist_MDS).embedding_

nmds = manifold.MDS(n_components=2, metric=False, max_iter=3000, eps=1e-12,
                    dissimilarity="precomputed", random_state=seed, n_jobs=1,n_init=1)
npos = nmds.fit_transform(new_dist_MDS, init=pos)

fig = mplt.figure(1)
ax = mplt.axes([0., 0., 1., 1.])

s = 100
mplt.scatter(new_dist_MDS[:, 0], new_dist_MDS[:, 1], color='navy', s=s, lw=0,label='True Position')
mplt.scatter(pos[:, 0], pos[:, 1], color='turquoise', s=s, lw=0, label='MDS')
mplt.scatter(npos[:, 0], npos[:, 1], color='darkorange', s=s, lw=0, label='NMDS')
mplt.legend(scatterpoints=1, loc='best', shadow=False)

new_dist_MDS = new_dist_MDS.max() / new_dist_MDS * 100
new_dist_MDS[np.isinf(new_dist_MDS)] = 0

# Plot the edges
start_idx, end_idx = np.where(pos)
# a sequence of (*line0*, *line1*, *line2*), where::
#            linen = (x0, y0), (x1, y1), ... (xm, ym)
segments = [[new_dist_MDS[i, :], new_dist_MDS[j, :]]
            for i in range(len(pos)) for j in range(len(pos))]
values = np.abs(new_dist_MDS)
lc = LineCollection(segments, zorder=0, cmap=mplt.cm.Blues,norm=mplt.Normalize(0, values.max()))
lc.set_array(new_dist_MDS.flatten())
lc.set_linewidths(0.5 * np.ones(len(segments)))
ax.add_collection(lc)

mplt.show()
