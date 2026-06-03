so_gio_lam = float(input("Nhập số giờ làm việc mỗi tuần: "))
luong_gio = float(input("Nhập thù lao mỗi giờ làm việc tiêu chuẩn: "))
gio_tieu_chuan = 44
if so_gio_lam <= gio_tieu_chuan:
    tong_luong = so_gio_lam * luong_gio
else:
    tong_luong = (gio_tieu_chuan * luong_gio) + ((so_gio_lam - gio_tieu_chuan) * luong_gio * 1.5)
print(f"Số tiền thực nhận của nhân viên: {tong_luong}")