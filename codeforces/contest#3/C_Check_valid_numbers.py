# C. Check valid numbers
# time limit per test1 s.
# memory limit per test256 MB
# Raphael is obsessed with the concept of "The Harmonic Constraint." To him, an array isn't just a list of numbers; it's a rhythm that must be perfectly balanced. He believes that if every segment of a fixed length 𝑝
#  sums to the exact same value 𝑞
# , the array achieves a state of "local resonance." However, he also needs the entire array of length 𝑛
#  to sum to a total value 𝑚
#  to satisfy the "global equilibrium."

# His friends think he’s overcomplicating things, but Raphael is convinced that such arrays are the key to understanding the universe. Can you help him determine if his dream array actually exists, or if he's chasing a mathematical ghost?

# Given four integers 𝑛
# , 𝑚
# , 𝑝
# , and 𝑞
# , determine whether there exists an integer array 𝑎1,𝑎2,…,𝑎𝑛
#  (elements may be negative) satisfying the following conditions:

# The sum of all elements in the array is equal to 𝑚
# :
# 𝑎1+𝑎2+…+𝑎𝑛=𝑚
# The sum of every 𝑝
#  consecutive elements is equal to 𝑞
# :
# 𝑎𝑖+𝑎𝑖+1+…+𝑎𝑖+𝑝−1=𝑞, for all 1≤𝑖≤𝑛−𝑝+1
# Input
# Each test contains multiple test cases. The first line contains the number of test cases 𝑡
#  (1≤𝑡≤104
# ). The description of the test cases follows.

# The first and only line of each test case contains four integers 𝑛
# , 𝑚
# , 𝑝
# , and 𝑞
#  (1≤𝑝≤𝑛≤100
# , 1≤𝑞,𝑚≤100
# ) — the length of the array, the sum of elements, the length of a segment, and the sum of a segment, respectively.

# Output
# For each test case, output "YES" (without quotes) if there exists an array satisfying the above conditions, and "NO" (without quotes) otherwise.

# You can output "YES" and "NO" in any case (for example, strings "yES", "yes", and "Yes" will all be recognized as valid responses).

# Example
# InputCopy
# 5
# 3 2 2 1
# 1 1 1 1
# 5 4 2 3
# 10 7 5 2
# 4 4 1 3
# OutputCopy
# YES
# YES
# YES
# NO
# NO
# Note
# In the first test case, an example of an array satisfying the condition is [1,0,1]
# . This is because:

# 𝑎1+𝑎2+𝑎3=1+0+1=2=𝑚
# 𝑎1+𝑎2=1+0=1=𝑞
# 𝑎2+𝑎3=0+1=1=𝑞
# In the second test case, the only array satisfying the condition is [1]
# .

# In the third test case, an example of an array satisfying the condition is [−2,5,−2,5,−2]
# .

# In the fourth test case, it can be proven that there is no array satisfying the condition.

t = int(input())

for _ in range(t):
    n, m, p, q = map(int, input().split())
    if n % p == 0 and (n // p) * q != m:
        print("NO")
    else:
        print("YES")
