print("sinh vien : bui hin xu")

print("ma so sv :245751030110041")

print("#############################")
s = input("Nhập chuỗi: ")
kq = ""

for ch in s:
    if not ch.isdigit():   # nếu KHÔNG phải là số
        kq += ch

print(kq)

