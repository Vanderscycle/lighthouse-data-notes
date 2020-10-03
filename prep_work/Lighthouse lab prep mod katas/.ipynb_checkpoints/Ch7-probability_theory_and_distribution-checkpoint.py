import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# set the plot style
plt.style.use('fivethirtyeight')

# generate 4 random numbers from the interval  <0,1)
#random_num = np.random.random(4)
#random_num

# this sets the seed to number 42
np.random.seed(42)
#python is a pseudorandomn number generator and so if given the same seed it will produce the same sequence of numbers every time

#! Binomial distribution
# n = the number of coin tosses
# p = the probability of getting heads
# size = the number of repeats 

n = 10
p = 0.5
size = 1000

samples = np.random.binomial(n, p, size)

# count the occurrence of each number
head_occu_count = Counter(samples) 

# calculate the probabilities as the number of occurences / size
head_proba = [val/size for val in head_occu_count.values()]

plt.scatter(x=head_occu_count.keys(), y=head_proba)
plt.xlabel('number of heads out of 10 tosses')
plt.ylabel('probability')

# show the plot
plt.show()

#! Normal/Gaussian distribution
# application of the theory seen so far. 


# loc = mean (“a centre”) of the distribution. (arithmetic mean)
# scale = standard deviation (a spread or “a width”) of the distribution.

samples = np.random.normal(loc=0, scale=1, size = 1000000)

plt.hist(samples, density=True, histtype="step", bins=100)

# show the plot
plt.show()

samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

# make histograms
plt.hist(samples_std1, density = True, histtype="step", bins=100)
plt.hist(samples_std3, density = True, histtype="step", bins=100)
plt.hist(samples_std10, density = True, histtype="step", bins=100)

# make a legend, set limits, and show the plot
plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()

samples_std1 = np.random.normal(10, 3, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(30, 3, size=100000)

# make histograms
plt.hist(samples_std1, density = True, histtype="step", bins=100)
plt.hist(samples_std3, density = True, histtype="step", bins=100)
plt.hist(samples_std10, density = True, histtype="step", bins=100)

# make a legend, set limits, and show the plot
plt.legend(('mean = 10', 'mean = 20', 'mean = 30'))
plt.ylim(-0.01, 0.42)
plt.show()