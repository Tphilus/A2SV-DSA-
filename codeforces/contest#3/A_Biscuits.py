# A. Biscuits
# time limit per test1 s.
# memory limit per test256 MB
# There are two sisters Alice and Betty. You have 𝑛
#  biscuits. You want to distribute these 𝑛
#  biscuits between two sisters in such a way that:

# Alice will get 𝑎
#  (𝑎>0
# ) biscuits;
# Betty will get 𝑏
#  (𝑏>0
# ) biscuits;
# each sister will get some integer number of biscuits;
# Alice will get a greater amount of biscuits than Betty (i.e. 𝑎>𝑏
# );
# all the biscuits will be given to one of two sisters (i.e. 𝑎+𝑏=𝑛
# ).
# Your task is to calculate the number of ways to distribute exactly 𝑛
#  biscuits between sisters in a way described above. Biscuits are indistinguishable.

# Formally, find the number of ways to represent 𝑛
#  as the sum of 𝑛=𝑎+𝑏
# , where 𝑎
#  and 𝑏
#  are positive integers and 𝑎>𝑏
# .

# You have to answer 𝑡
#  independent test cases.

# Input
# The first line of the input contains one integer 𝑡
#  (1≤𝑡≤104
# ) — the number of test cases. Then 𝑡
#  test cases follow.

# The only line of a test case contains one integer 𝑛
#  (1≤𝑛≤2⋅109
# ) — the number of biscuits you have.

# Output
# For each test case, print the answer — the number of ways to distribute exactly 𝑛
#  biscuits between two sisters in a way described in the problem statement. If there is no way to satisfy all the conditions, print 0
# .

# Example
# InputCopy
# 6
# 7
# 1
# 2
# 3
# 2000000000
# 763243547
# OutputCopy
# 3
# 0
# 0
# 1
# 999999999
# 381621773
# Note
# For the test case of the example, the 3
#  possible ways to distribute biscuits are:

# 𝑎=6
# , 𝑏=1
# ;
# 𝑎=5
# , 𝑏=2
# ;
# 𝑎=4
# , 𝑏=3
# .

t = int(input())
# arr = [int(input()) for _ in range(t)]
# print(arr)
for _ in range(t):
    n = int(input())
    
    output = (n - 1) // 2
    print(output)
    