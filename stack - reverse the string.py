s = input()
word = ""
stack = []
l = []
for i in s:
    if i == " ":
        stack.append(word)
        word = ""
    else:
        word += i
stack.append(word)
for i in  range(len(stack)):
    l.append(stack.pop())
print(" ".join(l))
