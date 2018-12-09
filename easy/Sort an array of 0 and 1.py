#Question: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    list1.sort()
    for i in range(n):
        print(list1[i],end=' ')
    print()