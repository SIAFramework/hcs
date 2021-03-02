#######################################################################
## Attribute Grouping
## Clustering code
## Author: Yashwanth M R (yashwanth.ramachandra@harman.com)
## Created on: 23/03/2017
## Latest Modified Date: 07/10/2016 by yashwanth.ramachandra@harman.com
## Version 1
#######################################################################

###  Wordcloud [Reference](http://www.sthda.com/english/wiki/text-mining-and-word-cloud-fundamentals-in-r-5-simple-steps-you-should-know)

# Import termdocument matrix
rm(list=ls())
SS_Salad_dressing <- read.csv("D:/3. Market Structure/1. WordCloud/1. Input files/WC_SS_Salad_dressing.csv", header = TRUE)

# Cummulative sum 
library(plyr)
SS_Salad_dressing <- SS_Salad_dressing[order(SS_Salad_dressing$No_of_Transactions,decreasing = TRUE),]
SS_Salad_dressing <- mutate(SS_Salad_dressing,No_of_Transactions_cumsum=cumsum(No_of_Transactions))
SS_Salad_dressing <- mutate(SS_Salad_dressing,Transactions_Share_cumsum=cumsum(Transaction_Share))

# Pareto-rule
SS_Salad_dressing$per <- round((SS_Salad_dressing$Transaction_Share)*100,4)
SS_Salad_dressing <- mutate(SS_Salad_dressing,cum_per = cumsum(per))
SS_Salad_dressing$pareto <- ifelse(SS_Salad_dressing$cum_per>80.21,"20%_margin","80%_margin")

# Filter Cum Transaction Share less than 80% 
library(data.table)
SS_Salad_dressing <- data.table(SS_Salad_dressing)
SS_Salad_dressing_80_Per <- SS_Salad_dressing[pareto=="80%_margin"]

# Convert to text
SS_Salad_dressing_80_Per_Text <- as.character(SS_Salad_dressing_80_Per$Attribute_Values)
SS_Salad_dressing_80_Per_Text <- paste0(SS_Salad_dressing_80_Per_Text,collapse = " ")

# Convert to corpus
SS_Salad_dressing_80_Per_Text <- Corpus(VectorSource(SS_Salad_dressing_80_Per_Text))

# Convert the text to lower case
SS_Salad_dressing_80_Per_Text <- tm_map(SS_Salad_dressing_80_Per_Text, content_transformer(toupper))
inspect(SS_Salad_dressing_80_Per_Text)

# Build Term document matrix
SS_Salad_dressing_80_Per_Text_dtm <- TermDocumentMatrix(SS_Salad_dressing_80_Per_Text)
Eighty_m <- as.matrix(SS_Salad_dressing_80_Per_Text_dtm)
Eighty_v <- sort(rowSums(Eighty_m),decreasing=TRUE)
Eighty_d <- data.frame(Eighty_word = names(Eighty_v),freq=Eighty_v)
head(Eighty_d, 10)

# wordcloud
library(tm)
library(NLP)
library(wordcloud)
set.seed(1234)
wordcloud(words = Eighty_d$Eighty_word,freq = Eighty_d$freq, min.freq = 1,max.words=200, random.order=FALSE, rot.per=0.35,colors=brewer.pal(8, "Dark2"))






# Filter Cum Transaction Share less than 80% 
SS_Salad_dressing_20_Per <- SS_Salad_dressing[pareto=="20%_margin"]

# Convert to text
SS_Salad_dressing_20_Per_Text <- as.character(SS_Salad_dressing_20_Per$Attribute_Values)
SS_Salad_dressing_20_Per_Text <- paste0(SS_Salad_dressing_20_Per_Text,collapse = " ")

# Convert to corpus
SS_Salad_dressing_20_Per_Text <- Corpus(VectorSource(SS_Salad_dressing_20_Per_Text))

# Convert the text to lower case
SS_Salad_dressing_20_Per_Text <- tm_map(SS_Salad_dressing_20_Per_Text, toupper)
inspect(SS_Salad_dressing_20_Per_Text)

# Build Term document matrix

SS_Salad_dressing_20_Per_Text_dtm <- TermDocumentMatrix(SS_Salad_dressing_20_Per_Text, control = list(toupper))
Twenty_m <- as.matrix(SS_Salad_dressing_20_Per_Text_dtm)
Twenty_v <- sort(rowSums(Twenty_m),decreasing=TRUE)
Twenty_d <- data.frame(Twenty_word = names(Twenty_v),freq=Twenty_v)
head(Twenty_d, 10)

# wordcloud
library(tm)
library(NLP)
library(wordcloud)
set.seed(1234)
wordcloud(words = Twenty_d$Twenty_word,freq = Twenty_d$freq, min.freq = 1,max.words=2000, random.order=FALSE, rot.per=0.35,colors=brewer.pal(8, "Dark2"))


#####################################################################################################################################################################################################################
# -------------------------------------------------------------------- END ------------------------------------------------------------------------------------------------------------------------------------------
#####################################################################################################################################################################################################################





# Pareto chart




# Aggregate data
library(data.table)
Other_Groups <- data.table(Other_Groups)
Other_Groups_Aggr <- Other_Groups[,.(count.Sum=sum(count)), by = Attribute_values]

# Remove cases where count is Zero
#setDT(Other_Groups_Aggr)[, .SD[!any(.SD[, -1, with = F] == 0)], by = Attribute_values]
Other_Groups_Aggr <- data.frame(Other_Groups_Aggr)

# Sort data
Other_Groups_Aggr$Attribute_values <- as.character(Other_Groups_Aggr$Attribute_values)
Other_Groups_Aggr <- Other_Groups_Aggr[order(Other_Groups_Aggr$count.Sum, decreasing = TRUE),]

# wordcloud
library(wordcloud)
set.seed(1234)
wordcloud(words = Other_Groups_Aggr$Attribute_values, freq = Other_Groups_Aggr$count.Sum, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))


# https://www.analyticsvidhya.com/blog/2014/05/build-word-cloud-text-mining-tools/
library(wordcloud)
library(tm)
library(SnowballC)


# Load the text
text <- readLines("D:/3. Market Structure/1. WordCloud/WordCloud.txt")

# Load the data as corpus
docs <- Corpus(VectorSource(text))

# Inspect the content of the document
inspect(docs)

# Cleaning the text
toSpace <- content_transformer(function(x, pattern) gsub(pattern, " ",x))
docs <- tm_map(docs, toSpace, "/")
docs <- tm_map(docs, toSpace, "@")
docs <- tm_map(docs, toSpace, "\\|")

# Convert the text to lower case
docs <- tm_map(docs, content_transformer(tolower))

# Remove numbers
docs <- tm_map(docs, removeNumbers)

# Remove english common stopwords
docs <- tm_map(docs, removeWords, stopwords("english"))

# Remove your own stop word
# specify your stopwords as a character vector
docs <- tm_map(docs, removeWords, c("blabla1", "blabla2")) 

# Remove punctuations
docs <- tm_map(docs, removePunctuation)

# Eliminate extra white spaces
docs <- tm_map(docs, stripWhitespace)

# Text stemming
docs <- tm_map(docs, stemDocument)


