f = open("num_friend.inp","r")
data = f.readlines()
f.close()

data = list(map(int,data))
print(data)

def divisor(a):
    global totalDivisor
    totalDivisor = 0
    for i in range(1,a):
        if a%i == 0:
            totalDivisor += i
    return totalDivisor

def checkFriend(K):
    for M in range(1,K):
        N = divisor(M)
        if M<N<K and divisor(N) == M:
            print(f'{N} and {M} is friend')
            wf.write(f'{N} and {M} is friend\n')

wf = open("num_friend.out","w")

for j in data:
    checkFriend(j)
