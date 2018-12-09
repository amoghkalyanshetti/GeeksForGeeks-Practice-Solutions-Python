#Question: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
t = int(input())
for i in range(t):
    list1 = list(map(str, input().split('.')))
    for i in range(len(list1) - 1, -1, -1):
        if (i == 0):
            print(list1[i])
        else:
            print(list1[i], end='.')
