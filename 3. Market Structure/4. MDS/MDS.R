# Computation of R-Squared

# Import data
MDS_data <-  read.csv("D:/3. Market Structure/3. MDS Map/Sweet_AffiliationMatrix.csv", header = T)
MDS_data <- MDS_data[-1]

# Convert to as.dist
MDS_dist <- dist(MDS_data)

# Compute cmdscale
MDS_cmdscale <- cmdscale(MDS_dist, k=2, eig = TRUE)

# Compute R-squared or GOF(Goodness of Fit)
MDS_cmdscale$GOF

# Compute points
dim(MDS_cmdscale$points)
MDS_cmdscale$points

sum(MDS_cmdscale$eig[seq_len(2)])/sum(abs(MDS_cmdscale$eig))
sum(MDS_cmdscale$eig[seq_len(2)])/sum(pmax(MDS_cmdscale$eig,0))