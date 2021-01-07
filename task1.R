TASK SUBMITTED BY : AAYUSH JAIN SETHIA
library(readxl)
data=read.csv("C:/Users/sanjay/Desktop/student_scores.csv",header=T)
str(data)
plot(data)
cor(data$Hours,data$Scores)
y=data$Scores
x=data$Hours
model=lm(y~x)
summary(model)
h=9.25
(pred=2.4837+(9.7758*h))
