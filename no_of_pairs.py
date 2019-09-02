#Given an array A of integers , find two numbers such that they add up to a specific target number K.
#Example Input: numbers={2, 7, 11, 15}, K=9 Output yes (2,7 can be added to get 9) if there is no such pair print 'no'.

(n, k) = map(int, input().split(" "))
l = input().split(" ")
flag = False
for i in range(n):
    for j in range(i+1, n):
        if(int(l[i]) + int(l[j])) == k:
            flag = True
if flag:
    print("YES")
else:
    print("NO")
