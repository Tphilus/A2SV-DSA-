t = int(input())

for _ in range(t):
    data = input().split()
    
    nums = [int(data[0]), int(data[1]), int(data[2])]
    
    for i in range(5):
        nums.sort()
        nums[0] += 1
    
    ans = nums[0] * nums[1] * nums[2]
    print(ans)
    