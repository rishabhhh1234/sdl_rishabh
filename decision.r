#install.packages("party")
library(party)
print(head(cars))
png(file = "decision_tree2221.png")
# Create the input data frame.
input.dat <- cars[c(1:50),]

# Give the chart file a name.
png(file = "decision_tree.png")

# Create the tree.
output.tree <- ctree(
  dist ~ speed + dist , 
  data = input.dat)

# Plot the tree.
plot(output.tree)

# Save the file.
dev.off()

