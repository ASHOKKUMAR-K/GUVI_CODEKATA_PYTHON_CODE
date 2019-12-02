bishop = tuple(map(int, input().split()))
pawn = tuple(map(int, input().split()))
def bishopPosition(b):
    a = []
    i = b[0]
    j = b[1]
    while True:
        if i == 7 or j == 0: break
        else:
            i += 1
            j -= 1
            a.append((i, j))
    i = b[0]
    j = b[1]
    while True:
        if i == 7 or j == 7: break
        else:
            i += 1
            j += 1
            a.append((i, j))
    i = b[0]
    j = b[1]
    while True:
        if i == 0 or j == 0: break
        else:
            i -= 1
            j -= 1
            a.append((i, j))
    i = b[0]
    j = b[1]
    while True:
        if i == 0 or j == 7: break
        else:
            i -= 1
            j += 1
            a.append((i, j))
    return a
lst = bishopPosition(bishop)
if pawn in lst: print("Yes")
else: print("No")
