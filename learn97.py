f = open("tgcan.inp","r")
data = f.readlines() #doc toan bo DB thanh list
f.close()

num_poin = int(data[0]) #lay dong dau tien ra
data.pop(0)

for i in range(len(data)):
    data[i] = data[i].split() #chuyen toa do cac diem thanh list con
    data[i] = list(map(int,data[i]))#chuyen toa do cac diem thanh int

def length(poinA,poinB): #ham tinh khoang cach vector AB
    return ((poinB[0]-poinA[0])**2 + (poinB[1]-poinA[1])**2)**0.5 #**2 la mu 2;**0.5 can bac 2

count = 0

for poin1 in range(len(data)-2): #tổ hợp 3 điểm trong data
    for poin2 in range(poin1+1,len(data)-1): #tổ hợp 3 điểm trong data
        for poin3 in range(poin2+1,len(data)): #tổ hợp 3 điểm trong data

            #tính độ dài vector
            length12 = length(data[poin1],data[poin2])
            length23 = length(data[poin2],data[poin3])
            length13 = length(data[poin1],data[poin3])

            #check 3 canh có tạo thành tam giác không?
            if length12 + length23 > length13 and length12 + length13 > length23 and length13 + length23 > length13:
                if length12 == length13 or length23 == length13 or length23 == length12: #check có phải là tam giác đều không?
                    if not (length13 == length12 == length23):
                        count += 1

            # print(length12,length23,length13) #debug
            # print(poin1,poin2,poin3) #debug

print('count',count)
# count = str(count)
wf = open("tgcan.out","w")
wf.writelines(f'count {count}')
wf.close()
# print('num_poin',num_poin) #debug
# print('data', data) #debug