'''Given a number N and an array of N elements, print the number of lucky numbers in the array.
Lucky number: N*I is also present in the array then the number is lucky where N is the number of elements in the array and I is the position of the element.(1 based indexing)
'''
n = int(input())
l = input().split(" ")
l = [int(x) for x in l]
count = 0
for i in range(n):
    if (n*(i+1)) in l:
        count += 1
print(count)
