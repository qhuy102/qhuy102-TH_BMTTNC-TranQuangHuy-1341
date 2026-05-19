# Nhập danh sách từ người dùng (cách nhau bởi dấu phẩy)
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(',')]

# Tính tổng số chẵn
tong_chan = sum(num for num in numbers if num % 2 == 0)

print(f"Tổng các số chẵn trong danh sách là: {tong_chan}")