n = int(input())

for _ in range(n):
    words = input()
    
    if len(words) > 10:
        first_char = words[0]
        last_char = words[-1]
        char_btn = len(words) - 2
        print(f"{first_char}{char_btn}{last_char}")
    else:
        print(words)