lines = []
while True:
    s = input("Nhập các dòng (nhập trống để kết thúc): ")
    if s:
        lines.append(s.upper())
    else:
        break
for line in lines:
    print(line)