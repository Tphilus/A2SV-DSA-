def swap_case(s):
    new_str = ""
    
    for char in s:
        if char.isupper():
            new_str += char.lower()
        else:
            new_str += char.upper()
    
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
