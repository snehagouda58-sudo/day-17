import math

# Example 1
mean1 = 70
sd1 = 15
n1 = 50

sample_mean1 = mean1
sample_sd1 = sd1 / math.sqrt(n1)

print("Example 1 Results")
print("Sample Mean =", sample_mean1)
print("Sample Standard Deviation =", round(sample_sd1, 2))


print("\n----------------------\n")

# Example 2
mean2 = 69
sd2 = 42
n2 = 80

sample_mean2 = mean2
sample_sd2 = sd2 / math.sqrt(n2)

print("Example 2 Results")
print("Sample Mean =", sample_mean2)
print("Sample Standard Deviation =", round(sample_sd2, 2))