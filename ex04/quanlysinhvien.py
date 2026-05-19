from sinh_vien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        # Sử dụng biến instance (self.danh_sach) thay vì biến class để quản lý dữ liệu tốt hơn
        self.danh_sach = []

    def tao_ma_dinh_danh(self):
        """Tự động tạo ID tăng dần dựa trên phần tử cuối cùng"""
        ma_lon_nhat = 1
        if self.so_luong() > 0:
            ma_lon_nhat = self.danh_sach[-1].id + 1
        return ma_lon_nhat

    def so_luong(self):
        """Trả về số lượng sinh viên hiện có"""
        return len(self.danh_sach)

    def phan_loai_ket_qua(self, sv: SinhVien):
        """Cập nhật học lực dựa trên thang điểm chuẩn"""
        if sv.diemTB >= 8.0:
            sv.hocLuc = "Giỏi"
        elif sv.diemTB >= 6.5:
            sv.hocLuc = "Khá"
        elif sv.diemTB >= 5.0:
            sv.hocLuc = "Trung Bình"
        else:
            sv.hocLuc = "Yếu"

    def themSinhVien(self):
        """Nhập thông tin và thêm mới sinh viên vào danh sách"""
        ma_so = self.tao_ma_dinh_danh()
        ho_ten = input("Nhập tên sinh viên: ")
        phai = input("Nhập giới tính: ")
        nganh = input("Nhập chuyên ngành: ")
        diem = float(input("Nhập điểm trung bình: "))
        
        # Khởi tạo đối tượng từ lớp SinhVien
        moi = SinhVien(ma_so, ho_ten, phai, nganh, diem)
        self.phan_loai_ket_qua(moi)
        self.danh_sach.append(moi)

    def xoaSinhVien(self, ma_id):
        """Tìm và xóa sinh viên theo ID"""
        for index, sv in enumerate(self.danh_sach):
            if sv.id == ma_id:
                self.danh_sach.pop(index)
                return True
        return False

    def timSinhVienByName(self, ten_nhap):
        """Tìm kiếm sinh viên theo tên (trả về sinh viên đầu tiên tìm thấy)"""
        for sv in self.danh_sach:
            if sv.name.lower() == ten_nhap.lower(): # Tìm không phân biệt hoa thường
                return sv
        return None

    def timSinhVienByID(self, ma_id):
        """Tìm kiếm sinh viên theo mã số định danh"""
        for sv in self.danh_sach:
            if sv.id == ma_id:
                return sv
        return None

    def updateSinhVien(self, ma_id):
        """Cập nhật lại toàn bộ thông tin của sinh viên qua ID"""
        doi_tuong = self.timSinhVienByID(ma_id)
        if doi_tuong:
            doi_tuong.name = input("Cập nhật tên mới: ")
            doi_tuong.sex = input("Cập nhật giới tính: ")
            doi_tuong.major = input("Cập nhật chuyên ngành: ")
            doi_tuong.diemTB = float(input("Cập nhật điểm trung bình: "))
            self.phan_loai_ket_qua(doi_tuong)
            print(f"=> Đã cập nhật xong thông tin ID {ma_id}")
        else:
            print("=> Thông báo: Không tìm thấy sinh viên này.")

    # --- Các hàm sắp xếp ---
    def sortByID(self):
        self.danh_sach.sort(key=lambda x: x.id)

    def sortByMajor(self):
        self.danh_sach.sort(key=lambda x: x.major)

    def sortByDiemTB(self):
        self.danh_sach.sort(key=lambda x: x.diemTB)

    def ShowSinhVien(self, list_hien_thi):
        """Hiển thị danh sách theo bảng định dạng chuẩn"""
        tieu_de = "{:<5} {:<20} {:<10} {:<15} {:<10} {:<10}"
        print(tieu_de.format("ID", "Họ Tên", "G.Tính", "Chuyên Ngành", "Điểm TB", "Xếp Loại"))
        
        if len(list_hien_thi) > 0:
            for sv in list_hien_thi:
                print(tieu_de.format(sv.id, sv.name, sv.sex, sv.major, sv.diemTB, sv.hocLuc))
        print("-" * 70)

    def getListSv(self):
        return self.danh_sach

    def soLuongSinhVien(self):
        return self.so_luong()