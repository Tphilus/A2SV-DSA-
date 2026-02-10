# B. Balance the Colonies
# time limit per test1 s.
# memory limit per test256 MB
# A large-scale simulation is being conducted with 𝑛
#  participants. Before the simulation begins, all participants must be divided into small groups, where each group contains either 2 or 3 people. Every participant must belong to exactly one group.

# After forming the groups, each group independently chooses one of two colonies to join: Colony A or Colony B. All members of a group always join the same colony.

# The organizers want the two colonies to be as balanced as possible. Your task is to determine the minimum possible difference between the number of people in Colony A and Colony B, assuming the groups are formed optimally and assigned to colonies in the best possible way.

# Input
# Each test consists of several test cases. The first line contains a single integer 𝑡
#  (1≤𝑡≤104)
#  — the number of test cases. The following lines describe the test cases.

# In the only line of each test case, there is an integer 𝑛
#  — the number of people participating in the simulation (2≤𝑛≤104)
# .

# Output
# For each number 𝑛
# , output the minimum possible difference between the number of participants assigned to the two colonies.

# Example
# InputCopy
# 3
# 2
# 5
# 12
# OutputCopy
# 2
# 1
# 0
# Note
# In the first test case, only one team can be formed, which will choose one of the colonies, while the other will have no one, so the answer is 2
# .

# In the second test case, two teams can be formed: one with two people and the other with three. These teams will choose different colonies; thus, the answer will be 1
# .

# In the third test case, four teams of three people will be formed, with the first two choosing Colony A and the remaining two choosing Colony B. The answer is 0.

# =============== Approach ==============
# We are given 𝑛
#  people who must be divided into teams of size 2 or 3.
# Each team then chooses one of two colonies, and all members of a team go to the same colony.

# Our goal is to minimize the absolute difference between the total number of people in the two colonies.

# Key Idea
# We try to evenly divide all people between the two colonies.

# Case Analysis
# If 𝑛≤3
# , all people must go to one colony → answer is 𝑛
# If 𝑛>3
#  and 𝑛
#  is even → answer is 0
# If 𝑛>3
#  and 𝑛
#  is odd → answer is 1

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 2:
        print(2)
    elif n == 3:
        print(3)
    else:
        print(n % 2)
    
