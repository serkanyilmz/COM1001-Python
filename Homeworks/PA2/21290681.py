num=int(input())

eng=[]
tr=[]
for x in range(num):
    inp=input().split(":")
    eng.append(inp[0])
    tr.append(inp[1])

last_inp=input().split()
lang=last_inp[0]
last_inp.pop(0)
last_inp=sorted(list(set(last_inp)))
eng.reverse()
tr.reverse()

not_found=[]
if lang=="EN":
    for word in last_inp:
        if word in tr:
            ind=tr.index(word)
            out=eng[ind]
            print(word+"="+out)
        else:
            not_found.append(word)
else:
    for word in last_inp:
        if word in eng:
            ind=eng.index(word)
            out=tr[ind]
            print(word+"="+out)
        else:
            not_found.append(word)

num_not_found=len(not_found)
if num_not_found!=0:
    print("{} word not found: {}".format(num_not_found," ".join(not_found)))
