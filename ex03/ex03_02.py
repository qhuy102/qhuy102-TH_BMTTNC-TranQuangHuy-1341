# Nhập danh sách
input_list = input("Nhập danh sách các phần tử, cách nhau bằng dấu phẩy: ")
my_list = input_list.split(',')

# Đảo ngược danh sách
reversed_list = my_list[::-1]

print(f"Danh sách sau khi đảo ngược: {reversed_list}")