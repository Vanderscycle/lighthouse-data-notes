# import numpy
import numpy as np

# set a random seed to replicate the results
np.random.seed(42)

# import matplotlib to visualize the experiment
import matplotlib.pyplot as plt

# generate ten random numbers (0 or 1) with equal probabilities
coin_flips_10 = np.random.randint(0,2,10)

# how many heads in 10 coin flips
count_heads = sum(coin_flips_10 == 1)
print(count_heads)
''' 
# empty list used to store the results
heads_ratio_nflips = []

# generate integers from 5 to 10,000
n_flips = np.arange(5,10000)

for flips in n_flips:
    # how many heads / flips
    heads_ratio = sum(np.random.randint(0,2,flips) == 1) / flips

    # append ratios
    heads_ratio_nflips.append(heads_ratio)

    # set plot size
plt.figure(figsize=(10,8))

# number of flips on the x axe and heads ratio on y axe
plt.plot(n_flips, heads_ratio_nflips)

# expected ratio
plt.plot(n_flips, len(n_flips)*[0.5], 'r--')

# plot settings
plt.figure(figsize=(10,8))
plt.xlabel('Flips')
plt.ylabel('Heads ratio')
plt.show() '''

#multiple commenting is shift alt a
# the green section doesn't work for some reason