# D. Genome Substring
# time limit per test1 s.
# memory limit per test256 MB
# At a distinguished high school located in Addis Ababa, Ethiopia, a biology lesson was taking place. The topic of the lesson was the genomes. Let's call the genome the string "ACTG".

# Kidus was very bored to sit in his class, so the teacher came up with a task for him: on a given string 𝑠
#  consisting of uppercase letters and length of at least 4
# , you need to find the minimum number of operations that you need to apply, so that the genome appears in it as a substring. For one operation, you can replace any letter in the string 𝑠
#  with the next or previous in the alphabet. For example, for the letter "D" the previous one will be "C", and the next — "E". In this problem, we assume that for the letter "A", the previous one will be the letter "Z", and the next one will be "B", and for the letter "Z", the previous one is the letter "Y", and the next one is the letter "A".

# Help Kidus solve the problem that the teacher gave him.

# A string 𝑎
#  is a substring of a string 𝑏
#  if 𝑎
#  can be obtained from 𝑏
#  by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

# Input
# The first line contains a single integer 𝑛
#  (4≤𝑛≤50
# ) — the length of the string 𝑠
# .

# The second line contains the string 𝑠
# , consisting of exactly 𝑛
#  uppercase letters of the Latin alphabet.

# Output
# Output the minimum number of operations that need to be applied to the string 𝑠
#  so that the genome appears as a substring in it.

# Examples
# InputCopy
# 4
# ZCTH
# OutputCopy
# 2
# InputCopy
# 5
# ZDATG
# OutputCopy
# 5
# InputCopy
# 6
# AFBAKC
# OutputCopy
# 16
# Note
# In the first example, you should replace the letter "Z" with "A" for one operation, the letter "H" — with the letter "G" for one operation. You will get the string "ACTG", in which the genome is present as a substring.

# In the second example, we replace the letter "A" with "C" for two operations, the letter "D" — with the letter "A" for three operations. You will get the string "ZACTG", in which there is a genome.

n = int(input())
s = input()
target = "ACTG"

def dist(a, b):
    d = abs(ord(a) - ord(b))
    return min(d, 26 - d)

ans = float('inf')

for i in range(n - 3):
    cost = 0
    for j in range(4):
        cost += dist(s[i + j], target[j])
    ans = min(ans, cost)

print(ans)
