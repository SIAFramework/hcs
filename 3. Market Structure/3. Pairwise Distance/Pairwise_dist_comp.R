set.seed(146)
x <- matrix(runif(9),3,3)

set.seed(782)
y <- matrix(runif(9),3,3)


x_dist<- dist(x)
x_dist

y_dist<- dist(y)
y_dist


x_final <- data.frame(as.matrix(x_dist))
y_final <- data.frame(as.matrix(y_dist))

x_final
y_final

library(pdist)
pdist <- pdist(x_final,y_final)
pdist


Pairwise_dist <- read.csv("D:/Pairwise_dist.csv", header = T)
pdist(Pairwise_dist)
