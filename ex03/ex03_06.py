def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

# Tạo dictionary mẫu
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = input("Nhập key muốn xóa: ")

# Thực hiện xóa
if xoa_phan_tu(my_dict, key_to_delete):
    print(f"Phần tử đã được xóa. Dictionary hiện tại: {my_dict}")
else:
    print("Key không tồn tại trong Dictionary.")