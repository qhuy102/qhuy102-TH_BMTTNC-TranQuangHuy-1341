# Nhập danh sách
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = [int(x) for x in input_list.split(',')]

# Chuyển List thành Tuple
my_tuple = tuple(numbers)

print(f"List: {numbers}")
print(f"Tuple được tạo từ List: {my_tuple}")