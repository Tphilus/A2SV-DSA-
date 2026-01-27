if __name__ == '__main__':
    mylist = []
    N = int(input())
    
    for _ in range(N):
        comman_line = input().split()
        comman = comman_line[0]
        
        if comman == "insert":
            mylist.insert(int(comman_line[1]), int(comman_line[2]))
        elif comman == "print":
            print(mylist)
        elif comman == "remove":
            mylist.remove(int(comman_line[1]))
        elif comman == "append":
            mylist.append(int(comman_line[1]))
        elif comman == "sort":
            mylist.sort()
        elif comman == "pop":
            mylist.pop()
        elif comman == "reverse":
            mylist.reverse()
        else:
            print("invalid")
