# Một doanh nhân, sau khi thực hiện mua bán N (N ≤ 100) chuyến hàng,
# mỗi chuyến hàng có tổng giá trị mua M và tổng giá trị bán B (M, B có thể lên đến 20 chữ số) mới tính xem mình huề vốn, lời hay lỗ, bao nhiêu tiền.
# Hãy viết chương trình để giúp doanh nhân trên tính toán kết quả kinh doanh.
# File kinhdoanh.inp:
# - Dòng đầu tiên trong file chứa số N
# - N dòng tiếp theo, mỗi dòng chứa cặp số M và B, hai số này cách nhau một khoảng trắng
# Ghi ra file kinhdoanh.out số tiền lời (nếu lỗ in ra số âm)

f = open("kinhdoanh.inp","r")
N = int(f.readline())
data = f.readlines()
f.close()

ProfitLoss = 0

for i in range(len(data)):
    data[i] = data[i].split()
    data[i] = list(map(int,data[i]))

for j in data:
    ProfitLoss += (j[1]- j[0])

print('ProfitLoss',ProfitLoss)

wf = open("kinhdoanh.out","w")
wf.writelines(f"ProfitLoss {ProfitLoss}")
wf.close()

print('N',N)
print('data',data)