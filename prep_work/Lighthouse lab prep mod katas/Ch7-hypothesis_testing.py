# import numpy
import numpy as np

# set a random seed to replicate results
np.random.seed(42)

# sales history in days
history = 365

# generate one-year sales for store A
mean_A = 20
std_A = 5
shop_A_sales = np.random.normal(mean_A, std_A, history)

# generate one-year sales for store B
mean_B = 19.5
std_B = 5
shop_B_sales = np.random.normal(mean_B, std_B, history)

# set the significance level
alpha = 0.05

# print the store A mean
print(shop_A_sales.mean())

# print the store B mean
print(shop_B_sales.mean())

# the differnce in the means
observed_means_diff = shop_A_sales.mean() - shop_B_sales.mean()
print(observed_means_diff)

both_sales = np.concatenate((shop_A_sales, shop_B_sales))

# permutation
sales_perm = np.random.permutation(both_sales)

# permutation replicates 
perm_shop_A_sales = sales_perm[:len(shop_A_sales)]
perm_shop_B_sales = sales_perm[len(shop_A_sales):]

print(perm_shop_A_sales.mean() - perm_shop_B_sales.mean())

# create an empty list to store the permutation replicates means
perm_repl_means = []

for _ in range(1000):
    # permutation 
    sales_perm = np.random.permutation(both_sales)

    # permutation replicates 
    perm_shop_A_sales = sales_perm[:len(shop_A_sales)]
    perm_shop_B_sales = sales_perm[len(shop_A_sales):]

    # permutation replicates mean
    perm_repl_mean = perm_shop_A_sales.mean() - perm_shop_B_sales.mean()

    # append perm_repl_mean to list
    perm_repl_means.append(perm_repl_mean)



# compute the p-value
p = np.sum(np.abs(perm_repl_means) >= observed_means_diff) / len(perm_repl_means)

# print the result
print('p-value =', p)

# final decision
if p < alpha:
    print('H0 is rejected.')
else:
    print('H0 is not rejected.')