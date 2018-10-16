# Load the party package. It will automatically load other
# dependent packages.
library(party)

# Create the input data frame.

data <- read.csv("Game_medal.csv")
input.dat <-data[c(1:05)]
# Give the chart file a name.
png(file = "decision_tree50.png")

# Create the tree.
output.tree <- ctree(City ~ Edition +	Sport +Discipline ,data = input.dat)

# Plot the tree.
plot(output.tree)

# Save the file.
dev.off()

