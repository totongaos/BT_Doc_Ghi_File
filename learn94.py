f = open("chuoi.inp","r")
data = f.readline()
f.close()
str_num = ''
str_text = ''

for i in data:
    if i.isnumeric():
        str_num += i
    else:
        str_text += i
print(str_num, str_text)

wf = open("chuoi.out", "w")
wf.writelines((str_text if len(str_text) != 0 else "-" ) +'\n'+ (str_num if len(str_num) != 0 else "-"))