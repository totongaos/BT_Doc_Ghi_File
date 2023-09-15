f = open("dayso.ipt", "r")
data = f.readlines()
f.close()

data = list(map(int,data)) #chuyển data trong file thành list chứa các số nguyên
print(data)

def num_series(k): #hàm fill dãy số theo quy luật
    lst = [1,1,1] #list chưa 3 số đầu tiên
    while len(lst)<k:  #khi len của list > k thì sẽ dừng ko append nữa
        lst.append(lst[-1]+lst[-3]) #append k vào list theo công thuc
    return lst #trả về list đã hoàn chỉnh

max_lst = num_series(max(data)) #dãy sô lơn nhất
print('max_lst',max_lst)
wf = open("dayso.out","w")
for i in data:
    wf.writelines(str(max_lst[i-1])+"\n") #fill số có thứ tự tỏng file .inp ở list max ra file .out
    print(max_lst[i-1])