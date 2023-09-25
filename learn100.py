f = open("bieudienso.inp","r")
data = f.readline()
f.close()

N = int(data)
total = 0
lst = []
for i in range(1,N//2+1): # N//2 vì khi cộng N//2 + (N//2)+1  -> kqua sẽ lớn hơn N rồi, nên không cần xét
    result = str(i)
    total = i
    while total<N:
        i += 1
        total += i
        result += "+" + str(i)
    if total == N:
        lst.append(result)
        print(total,result)

print(lst)
len = str(len(lst))
wf = open("bieudienso.out","w")
wf.writelines(len + "\n")
for i in lst:
    wf.writelines(i + "\n")

wf.close()