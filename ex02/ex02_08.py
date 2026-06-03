value = []
items = [x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
    int_p = int(p, 2)
    if not int_p % 5:
        value.append(p)
print(','.join(value))