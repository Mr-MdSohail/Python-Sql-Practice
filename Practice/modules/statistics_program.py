# Imagine you are analyzing the exam scores of a small class. The scores are:
# [85, 90, 75, 90, 100, 60, 90, 80]

# Your Task:

# Import the statistics module.

# Create a list variable containing those 8 scores.

# Calculate the mean, median, and mode using the module's functions.

# Print out the results clearly.
import statistics
scores =  [85, 90, 75, 90, 100, 60, 90, 80]
print("Score are", scores)
print("Mean of the scores is",statistics.mean(scores))
print("Median of the scores is",statistics.median(scores))
print("Mode of the scores is",statistics.mode(scores))
