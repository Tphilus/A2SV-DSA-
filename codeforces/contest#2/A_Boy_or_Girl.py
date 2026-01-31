words = input()

unique_words = set(words)

if len(unique_words) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")