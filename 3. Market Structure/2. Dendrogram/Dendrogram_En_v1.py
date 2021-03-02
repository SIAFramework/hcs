"""
Created on Thu Jan 10 15:08:30 2019

@author: YRamachandra
"""
#############################################################################################################################
#################################################### Dendrogram: Phase-2 ####################################################
#############################################################################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as mplt
import random
import scipy.spatial.distance as sd #squareform,pdist
from scipy.spatial.distance import squareform
from scipy.cluster import hierarchy
from sklearn.cluster import AgglomerativeClustering

pd.set_option('display.max_columns',500)

#############################################################################################################################
######################################################## Import data ########################################################
#############################################################################################################################

pydata = pd.read_csv('C:\\Users\\yramachandra\\Documents\\R\\Projects\\Shiny Apps\\Online_File_Conversion\\OL_File_Conv\\data\\data.csv')


dg_input = pd.read_csv("D:\\YASHWANTH\\3. Market Structure\\2. Dendrogram\\4. Phase 2\\CANDY\\test_input.csv")

filter_upc = ["(C) M&MS PEANUT SHARING SIZE-4000052274","HERSHEY COOKIE-N-CRM       1.55OZ-40000224884","HERSHEY KIT KAT BIG KAT KG SE 3OZ-40000981701","HERSHEY REESE P/B CUP D/CHOC1.5OZ-40000219155",
              "HERSHEY REESESTKS 15120     1.5OZ-40000249851","HERSHEY YORK PEPP 330       1.4OZ-40000224897",
              "HERSHEYS GOLD W/PNTS&PRTZEL 1.4OZ-40000828299","M&M PEANUT BUTTER 1244     1.63OZ-40000225025",
              "M&MS CRUNCHY MINT SHARE SZ 2.83OZ-40000711923","MARS M&M P/NUT CHOC CANDY  1.74OZ-40000224860",
              "MARS M&M PEANUT KING SIZE  3.27OZ-40000224849","MARS SNICKERS BAR 42431 1.86OZ-40000232873",
              "MARS TWIX CARAMEL          1.79OZ-40000281075","MARS TWIX DRK CHCL CRM SNG 1.79OZ-40000997159",
              "(C) SNICKERS TREES 2-TO-GO BARS-4000049383","(C)HOT TAMALES STKNG STFF T/B 5OZ-40000830879",
              "(H)M&M MINIS MC MEGATUBE   1.77OZ-40000996883","(S)AIRHEADS ASRTD FRUIT BITES 2OZ-40000352986",
              "100 GRAND NESTLE-64800020630","ADAMS BIG CHERRY CHCLT CPS 1.75OZ-40000981972"]

filter_upc = ["(C)HOT TAMALES STKNG STFF T/B 5OZ-40000830879",
              "(H)M&M MINIS MC MEGATUBE   1.77OZ-40000996883","(S)AIRHEADS ASRTD FRUIT BITES 2OZ-40000352986",
              "100 GRAND NESTLE-64800020630","ADAMS BIG CHERRY CHCLT CPS 1.75OZ-40000981972"]

filter_upc = ["(C) M&MS PEANUT SHARING SIZE-4000052274","HERSHEY COOKIE-N-CRM       1.55OZ-40000224884","HERSHEY KIT KAT BIG KAT KG SE 3OZ-40000981701","HERSHEY REESE P/B CUP D/CHOC1.5OZ-40000219155",
              "HERSHEY REESESTKS 15120     1.5OZ-40000249851","HERSHEY YORK PEPP 330       1.4OZ-40000224897",
              "HERSHEYS GOLD W/PNTS&PRTZEL 1.4OZ-40000828299","M&M PEANUT BUTTER 1244     1.63OZ-40000225025",
              "M&MS CRUNCHY MINT SHARE SZ 2.83OZ-40000711923","MARS M&M P/NUT CHOC CANDY  1.74OZ-40000224860",
              "MARS M&M PEANUT KING SIZE  3.27OZ-40000224849","MARS SNICKERS BAR 42431 1.86OZ-40000232873",
              "MARS TWIX CARAMEL          1.79OZ-40000281075","MARS TWIX DRK CHCL CRM SNG 1.79OZ-40000997159"]

filter_upc = ["(C) SNICKERS TREES 2-TO-GO BARS-4000049383","(C)HOT TAMALES STKNG STFF T/B 5OZ-40000830879",
              "(H)M&M MINIS MC MEGATUBE   1.77OZ-40000996883","(S)AIRHEADS ASRTD FRUIT BITES 2OZ-40000352986","100 GRAND NESTLE-64800020630"]

dg_input_sample = dg_input.loc[dg_input['from_upc'].isin(filter_upc) & dg_input['to_upc'].isin(filter_upc),]
dg_input_sample.index = range(0,len(dg_input_sample))
dg_input_sample = dg_input_sample.drop(['cond1'],axis=1)
dg_values = dg_input_sample['affiliation_value'].values
#dg_input_sample = dg_input

#############################################################################################################################
#################################################### Data Pre-Processing ####################################################
#############################################################################################################################

# Convert it into Symmetric-Matrix
dg_sym_mat = dg_input_sample.set_index(['from_upc','to_upc'])['affiliation_value'].unstack().values
dg_sym_mat = np.array(dg_sym_mat)
dg_sym_mat = np.nan_to_num(dg_sym_mat)

dg_sym_mat_df = pd.DataFrame(dg_sym_mat)

for i in range(0,len(dg_sym_mat_df)):
    dg_sym_mat_df[i] = np.where(dg_sym_mat_df[i]>0,1/dg_sym_mat_df[i],dg_sym_mat_df[i])
    dg_sym_mat_df[i] = np.where(dg_sym_mat_df[i]==0,1,dg_sym_mat_df[i])

dg_sym_mat_df = np.array(dg_sym_mat_df)
np.fill_diagonal(dg_sym_mat_df,0)
dg_sym_mat_df = pd.DataFrame(dg_sym_mat_df)

# Rename the columns & indicies
dg_columns = dg_input_sample.set_index(['from_upc','to_upc'])['affiliation_value'].unstack().columns
dg_indicies = dg_input_sample.set_index(['from_upc','to_upc'])['affiliation_value'].unstack().index

dg_sym_mat_df.columns = dg_columns
dg_sym_mat_df.index = dg_indicies



# Convert to square form : https://stackoverflow.com/questions/41416498/dendrogram-or-other-plot-from-distance-matrix
dg_input = pd.read_csv("D:\\YASHWANTH\\3. Market Structure\\2. Dendrogram\\4. Phase 2\\CANDY\\test_input.csv")

dg_sym_mat_df = dg_input
dg_sym_mat_df.drop(['from_upc'],axis=1,inplace=True)
dg_sym_mat_df.index = dg_sym_mat_df.columns
dg_columns = dg_sym_mat_df.columns

final_data = squareform(dg_sym_mat_df)
data_DD_Link = hierarchy.linkage(final_data,method = "average")


# Plot Dendrogam
Lable_list = dg_columns.tolist()

random.seed(1245)
mplt.figure(figsize=(12,4))
hierarchy.dendrogram(data_DD_Link, show_contracted=True, labels = Lable_list)

mplt.close('close')
data_DD = mplt.title('Dendogram for CANDY')
mplt.setp(data_DD,color = 'b')
mplt.xticks(rotation=90) #mplt.ylim(0,1.5)
mplt.plot()
#mplt.subplots_adjust(left=1,right=0.9,top=0.9,bottom=-1)


# Get the cluster information for each leaf-nodes
cluster = AgglomerativeClustering(n_clusters=2,affinity='euclidean',linkage='average')

dg_values = dg_input_sample['affiliation_value'].values
dg_values = dg_values.reshape(1,-1)

cluster.fit_predict(dg_sym_mat)
cluster.fit_predict([dg_values])
print(cluster.labels_)

mplt.figure(figsize=(10,7))
mplt.scatter(dg[:,0],dg[:,1],c=cluster.labels_, cmap = 'ranibow')


#############################################################################################################################
############# END ################################### Dendrogram: Phase-2 ########################## END ####################
#############################################################################################################################