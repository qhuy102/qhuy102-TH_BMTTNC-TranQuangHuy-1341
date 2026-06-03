def dao_nguoc_chuoi(s):
    return s[::-1]

input_string = input("Nhập chuỗi cần đảo ngược: ")
print(f"Chuỗi đảo ngược: {dao_nguoc_chuoi(input_string)}")