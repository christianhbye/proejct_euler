# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np


def sum_of_multiple(n):
    s_arr = n * np.arange(1000 // n + 1)
    s_arr = s_arr[s_arr < 1000]
    s = np.sum(s_arr)
    return s


ans = sum_of_multiple(3) + sum_of_multiple(5) - sum_of_multiple(3 * 5)
print(ans)
