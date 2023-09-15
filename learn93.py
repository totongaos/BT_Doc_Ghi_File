def check_Prime(b): #hàm check số b có phải số nguyên tố ko?
    for j in range(2,(b//2)+1):
        if b%j == 0 :
            return False
    if b >1: # để chắc rằng số 2&3 ko bị sót
        # print('b')
        return True
    return False
def secession(a): #hàm tách thua so nguyen to
    result = ""
    i=2 #so 1 & 0: ko phai so nguyen to
    while a != 1: #khi a =1 dung vong lap
        if (check_Prime(i)) and (a%i == 0): #check i có phải so nguyen to ko & a chia het cho i ko?
            a = a/i
            result += str(i) + " "
        else:
            i+=1
    return result

f = open("thuaso.inp","r") #mo phai & doc file
data = f.readlines() #doc tưng dong
f.close() #dong file
wf = open("thuaso.out","w") #mơ file & viet

data = list(map(int,data)) #map data là int
print(data)

for ii in data:
    print(secession(ii))
    ii = str(secession(ii)) #chuyen sang str trc khi viet vào file
    wf.writelines(f'{ii}\n')

