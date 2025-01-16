#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sample code of HW3 Problem 5
Monte Carlo estimate of the Euler Number
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from tqdm import tqdm

# Basic parameters
# N: number of 
N_trials = int(1e7)
n_list = []

#-------- Your code (~10 lines) ----------
for _ in tqdm(range(N_trials)):
    cumulative_sum = 0
    n = 0
    while cumulative_sum <= 1:  # Stop when S_n > 1
        cumulative_sum += np.random.uniform(0, 1)
        n += 1
    n_list.append(n)  

euler_number_est = np.mean(n_list)
#---------- End of your code -----------
# Optional: Print the Monte-Carlo estimates abnd visualize the empirical CDF
print(euler_number_est)
# print(n_list)
res = stats.ecdf(np.array(n_list))
ax = plt.subplot()
res.cdf.plot(ax)
ax.set_xlabel('Estimated Euler Number')
ax.set_ylabel('Empirical CDF')
plt.show()