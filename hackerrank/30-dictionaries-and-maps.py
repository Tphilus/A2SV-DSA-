import sys
n = int(sys.stdin.readline())

# Build the book
phone_book = {}
for _ in range(n):
    entry = sys.stdin.readline().split()
    phone_book[entry[0]] = entry[1]

# Query until the end of input
while True:
    line = sys.stdin.readline().strip()
    if not line: # End of input
        break
    if line in phone_book:
        print(f"{line}={phone_book[line]}")
    else:
        print("Not found")
