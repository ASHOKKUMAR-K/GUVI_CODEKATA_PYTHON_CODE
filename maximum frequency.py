n = int(input())
l = input().split(" ")
freq = l[0]
count = 0
for i in range(n):
    curr_freq = l.count(l[i])
    if curr_freq > count:
        count = curr_freq
        freq = l[i]
print(freq)
