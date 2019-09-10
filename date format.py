date = input().split("/")
if int(date[0]) <= 31 and int(date[1]) <= 12 and len(date[2]) == 4:
    print("yes")
else:
    print("no")
