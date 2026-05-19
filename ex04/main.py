from qlsv import QuanLySinhVien

def hien_thi_menu():
    print("\n" + "="*30)
    print(" HỆ THỐNG QUẢN LÝ SINH VIÊN ")
    print("="*30)
    print("1. Thêm sinh viên mới")
    print("2. Cập nhật thông tin qua ID")
    print("3. Xóa sinh viên qua ID")
    print("4. Tìm kiếm theo tên")
    print("5. Sắp xếp theo điểm trung bình")
    print("6. Sắp xếp theo chuyên ngành")
    print("7. Hiển thị toàn bộ danh sách")
    print("0. Thoát hệ thống")
    print("="*30)

def main():
    bo_quan_ly = QuanLySinhVien()
    
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn (0-7): ")

        if lua_chon == "1":
            bo_quan_ly.themSinhVien()
            print("=> Thông báo: Đã thêm sinh viên thành công.")

        elif lua_chon == "2":
            if bo_quan_ly.soLuongSinhVien() > 0:
                id_nhap = int(input("Nhập ID cần cập nhật: "))
                bo_quan_ly.updateSinhVien(id_nhap)
            else:
                print("=> Lỗi: Hiện tại danh sách đang trống.")

        elif lua_chon == "3":
            if bo_quan_ly.soLuongSinhVien() > 0:
                id_xoa = int(input("Nhập ID cần xóa: "))
                if bo_quan_ly.xoaSinhVien(id_xoa):
                    print(f"=> Thành công: Đã xóa sinh viên ID {id_xoa}.")
                else:
                    print(f"=> Thất bại: Không tìm thấy ID {id_xoa}.")
            else:
                print("=> Lỗi: Danh sách trống.")

        elif lua_chon == "4":
            if bo_quan_ly.soLuongSinhVien() > 0:
                ten_tim = input("Nhập tên sinh viên cần tìm: ")
                ket_qua = bo_quan_ly.timSinhVienByName(ten_tim)
                if ket_qua:
                    print(ket_qua)
                else:
                    print("=> Thông báo: Không tìm thấy kết quả phù hợp.")
            else:
                print("=> Lỗi: Danh sách trống.")

        elif lua_chon == "5":
            if bo_quan_ly.soLuongSinhVien() > 0:
                print("\n--- Sắp xếp theo điểm trung bình ---")
                bo_quan_ly.sortByDiemTB()
                bo_quan_ly.ShowSinhVien(bo_quan_ly.getListSv())
            else:
                print("=> Lỗi: Danh sách trống.")

        elif lua_chon == "6":
            if bo_quan_ly.soLuongSinhVien() > 0:
                print("\n--- Sắp xếp theo chuyên ngành ---")
                bo_quan_ly.sortByMajor()
                bo_quan_ly.ShowSinhVien(bo_quan_ly.getListSv())
            else:
                print("=> Lỗi: Danh sách trống.")

        elif lua_chon == "7":
            if bo_quan_ly.soLuongSinhVien() > 0:
                print("\n--- Danh sách sinh viên hiện có ---")
                bo_quan_ly.ShowSinhVien(bo_quan_ly.getListSv())
            else:
                print("=> Lỗi: Danh sách trống.")

        elif lua_chon == "0":
            print("Đang thoát chương trình... Tạm biệt!")
            break
            
        else:
            print("=> Lỗi: Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()