>>> def search(b):
    global d
    global rlt
    for m in d[b]:
        rlt.add(m)
        if len(d[m]) == 0:
            rlt.add(m)
            continue
        else:
            search(m)

d = {}
i = int(input())
for j in range(i):
    a,*parent=input().replace(":", " ").split()
    d[a] = parent

i = int(input())
for i in range(i):
    rlt = set()
    a, b = input().split()
    if b not in d.keys():
        print('No')
        continue
    elif a == b:
        print('Yes')
        continue
    
    for m in d[b]:
        rlt.add(m)
        search(m)
        
    if a in rlt:
        print('Yes')
    else:
        print('No')
