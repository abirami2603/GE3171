from scipy.special import perm

# Find the permutation of 5, 2 using perm(n, k) function
per = perm(5, 2, exact=True)
print(per)
