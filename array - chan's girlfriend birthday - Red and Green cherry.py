(m, n) = map(int, input().split())
l = [list(input()) for _ in range(m)]
cost = 0
for i in range(m):
    for j in range(n):
        if j == 0:
            if l[i][j] == 'R':
                if l[i][j+1] == 'G': continue
                else:
                    if l[i][j+2] == 'G' :
                        l[i][j] = 'G'
                        cost += 5
                    else:
                        l[i][j+1] = 'G'
                        cost += 5
            else:
                if l[i][j+1] == 'R': continue
                else:
                    if l[i][j+2] == 'R' :
                        l[i][j] = 'R'
                        cost += 3
                    else:
                        l[i][j+1] = 'R'
                        cost += 3
        elif j == n-1:
            if l[i][j] == 'G':
                if l[i][j-1] == 'R': continue
                else:
                    if l[i][j-2] == 'R' :
                        l[i][j] == 'R'
                        cost +=3
                    else:
                        l[i][j-1] = 'R'
                        cost += 3
            else:
                if l[i][j-1] == 'G': continue
                else:
                    if l[i][j-2] == 'G' :
                        l[i][j] == 'G'
                        cost += 5
                    else:
                        l[i][j-1] = 'G'
                        cost += 5
        else:
            if l[i][j] == 'R':
                if l[i][j-1] == 'R' and l[i][j+1] == 'R':
                    l[i][j] = 'G'
                    cost += 5
                elif l[i][j-1] == 'R' and l[i][j+1] == 'G':
                    l[i][j-1] = 'G'
                    cost += 5
                elif l[i][j-1] == 'G' and l[i][j+1] == 'R':
                    l[i][j+1] = 'G'
                    cost += 5
                else: continue
            else:
                if l[i][j-1] == 'G' and l[i][j+1] == 'G':
                    l[i][j] = 'R'
                    cost += 3
                elif l[i][j-1] == 'G' and l[i][j+1] == 'R':
                    l[i][j-1] = 'R'
                    cost += 3
                elif l[i][j-1] == 'R' and l[i][j+1] == 'G':
                    l[i][j+1] = 'R'
                    cost += 3
                else: continue
print(cost)
