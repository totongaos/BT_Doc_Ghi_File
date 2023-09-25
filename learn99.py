f = open("ngay.inp","r")
data = f.readline()
f.close()

x = data.find(" ") #tách ngày và N
N = int(data[x:])
time = data[:x]
time = time.split("/")
time = list(map(int, time))

print("data",N,time)

D_day = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

for i in range(N):
    time[0] += 1
    num_day = D_day[time[1]]
    if time[1] == 2:
        if time[2] %400 == 0 or ( time[2]%4 == 0 and time[2]%100 != 0):
            num_day += 1
    if time[0] > num_day:
        time[0] = 1
        time[1] += 1
        if time[1] > 12:
            time[1] = 1
            time[2] +=1
print(time)
wf = open("ngay.out","w")
wf.writelines(f"{time[0]}/{time[1]}/{time[2]}")
wf.close()
print(time)