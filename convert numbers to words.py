f = open("file.txt", "w+")
data = input()
f.write(data)
f.seek(0)
read_data = f.read()
temp = int(read_data)
l = []
while(temp > 0):
    digit = temp % 10
    l.append(digit)
    temp = temp//10
#print(l)
l.reverse()
#print(l)
length = len(l)

ones_digit = {1:"one", 2:"two", 3:"three", 4:"four", 5: "five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 0:""}
tens_digit = {1:"ten", 2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety", 0:""}

two_digit = {1:"eleven", 2: "twelve", 3: "thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen", 0:"ten"}

#print(l[0])
#print(l[1])
if length == 3:
    if (l[1] == 0 and l[2] == 0):
        wr = str(ones_digit[l[0]]) + " hundred"
    elif (l[1] == 0 and l[2] != 0):
        wr = str(ones_digit[l[0]]) + " hundred and " + str(ones_digit[l[2]])
    elif (l[1] != 0 and l[2] == 0):
        wr = str(ones_digit[l[0]]) + " hundred and " + str(tens_digit[l[1]])
    else:
        wr = str(ones_digit[l[0]]) + " hundred and " + str(tens_digit[l[1]]) + " " + str(ones_digit[l[2]])

elif length == 2:
    if l[0] == 1:
        wr = two_digit[l[1]]
    else:
        if l[1] == 0:
            wr = tens_digit[l[0]]
        else:
            wr = tens_digit[l[0]] + " " + ones_digit[l[1]]
elif length == 1:
    wr = ones_digit[l[0]]
else:
    wr = ""

f.writelines(wr)
f.seek(3)
last = f.readlines()
print(last)
f.close()
