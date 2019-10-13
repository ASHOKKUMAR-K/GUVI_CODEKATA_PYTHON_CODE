n = int(input())
l = [str(x) for x in input().split()]
for i in l:
    if i in ('1', '4', '78'):
        print("+")
    elif i[-1] == '5' and i[-2] == '3':
        print("-")
    elif i[:3] == '190':
        print("?")
    else:
        print("*")
