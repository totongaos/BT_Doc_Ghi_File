# File 2to10.inp là file chứa các số nhị phân (mỗi dòng 1 số), hãy chuyển các số nhị phân đó sang số thập phân
# rồi lưu lại vào file  2to10.out (mỗi dòng 1 số)
#Đọc file và print liệu
with open("2to10.inp", "r") as f:
    line = f.readline().rstrip("\n")
    index = 1
    while line:
        print(line)
        Decimal=0
        lst =[]
        binary_num = line
        for j in binary_num:
            j=int(j)
            lst.append(int(j))
        lst.reverse()
        for i in range(0, len(binary_num)):
            Decimal += lst[i]*(2**i)
        Decimal=str(Decimal)
        with open('2to10.out', 'a') as wf: # Ghi file vào cuối
            wf.write(f'{line} -> {Decimal}\n')
        index += 1
        line = f.readline().rstrip("\n")
with open('2to10.out', 'a') as wf:
    wf.write('\n')