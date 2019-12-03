s = "WELCOMETOGUVICORPORATIONS"
stg = input()
(s1, s2) = (s.index(stg)//5, s.index(stg)%5)
print(s1, s2)
(e1, e2) = ((s.index(stg)+len(stg)-1)//5, (s.index(stg)+len(stg)-1)%5)
print(e1, e2)
