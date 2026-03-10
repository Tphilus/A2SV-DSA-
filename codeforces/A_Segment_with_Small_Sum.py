# A. Segment with Small Sum
# time limit per test1 second
# memory limit per test1024 megabytes
# Given an array of 𝑛
#  integers 𝑎𝑖
# . Let's say that the segment of this array 𝑎[𝑙..𝑟]
#  (1≤𝑙≤𝑟≤𝑛
# ) is good if the sum of elements on this segment is at most 𝑠
# . Your task is to find the longest good segment.

# Input
# The first line contains integers 𝑛
#  and 𝑠
#  (1≤𝑛≤105
# , 1≤𝑠≤1018
# ). The second line contains integers 𝑎𝑖
#  (1≤𝑎𝑖≤109
# ).

# Output
# Print one integer, the length of the longest good segment. If there are no such segments, print 0
# .

# Example
# InputCopy
# 7 20
# 2 6 4 3 6 8 9
# OutputCopy
# 4

# == CODE ==
n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
curr_sum = 0
mx = 0

for right in range(n):
    curr_sum += arr[right]
    
    while curr_sum > s:
        curr_sum -= arr[left]
        left += 1
    
    mx = max(mx, right - left + 1)

print(mx)
    
