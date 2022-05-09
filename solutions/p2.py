"""
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

# every third number is even (since odd + even = odd, odd + odd = even)
# i.e., index 1, 4, 7 etc
# a4 = a3 + a2 = (a1 + a2) + a2 = a1 + 2a2 = 3a1 + 2a0


# brute force code
fib = [1, 2]
ans = 2
while fib[-1] < 4e6:
    next_val = fib[-2] + fib[-1]
    if next_val % 2 == 0:
        ans += next_val
    fib.append(next_val)
print(ans)

# there's definiteley an analytical answer that would be col to find and prove by induction
