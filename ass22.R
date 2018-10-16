library(party)

#data<-read.csv("Game_medal.csv")
input.dat<-cars_csv[c(1:50),]
png(file="decisionTree33.png")
print(head(cars_csv))
#data.frame(data)
output.tree<-ctree(dist ~ speed,data=input.dat)
plot(output.tree)
dev.off()

