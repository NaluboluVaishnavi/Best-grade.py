s=input()
p = int(input())
k = int(input())
s1 = list(s)
s = 0
e = len(s1)
mini = 999
if abs(p-k-1)>=0:
    s = abs(p-k-1)
if p+k<len(s1):
    e=p+k 
print(s,e)
for i in range(s,e):
    mini = min(ord(s1[i]),mini)

store = s1[p]
s1[p] = s1[s1.index(chr(mini))]
s1[s1.index(chr(mini))] = store 
print(mini)
print(''.join(s1))          