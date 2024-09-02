# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:03:15 2024

@author: Administrator
"""

import random

class SinhVien:
    def __init__(self, ma_sv, ho_ten, gpa):
        """
        Khởi tạo một đối tượng SinhVien với mã sinh viên, họ tên và GPA.
        """
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.gpa = gpa
        self.xep_loai = self.cap_nhat_xep_loai()
        
    def xuat_thong_tin(self):
        """
        Trả về chuỗi mô tả thông tin sinh viên.
        """
        return f"Mã SV: {self.ma_sv}, Họ tên: {self.ho_ten}, GPA: {self.gpa}, Xếp loại: {self.xep_loai}"
    
    def cap_nhat_xep_loai(self):
        """
        Cập nhật xếp loại học lực dựa trên GPA.
        """
        if self.gpa > 0 and self.gpa < 3.5:
            return "Kém"
        elif 3.5 <= self.gpa < 5.0:
            return "Yếu"
        elif 5.0 <= self.gpa < 7.0:
            return "Trung bình"
        elif 7.0 <= self.gpa < 8.0:
            return "Khá"
        elif 8.0 <= self.gpa < 9.0:
            return "Giỏi"
        elif 9.0 <= self.gpa <= 10:
            return "Xuất sắc"
        else:
            return "Không có xếp loại"


class QuanLySinhVien:
    def __init__(self):
        """
        Khởi tạo danh sách sinh viên.
        """
        self.danh_sach_sv = []

    def them_sv(self, ds_sv):
        """
        Thêm các sinh viên theo danh sách GVTH cung cấp.
        """
        for sv in ds_sv:
            sinhvien = SinhVien(*sv)
            self.danh_sach_sv.append(sinhvien)
            
    def xuat_thong_tin_sv(self):
        """
        Xuất thông tin tất cả sinh viên.
        """
        for sv in self.danh_sach_sv:
            print(sv.xuat_thong_tin())
            
    def khoi_tao_ngau_nhien(self, so_sv):
        """
        Khởi tạo ngẫu nhiên các sinh viên.
        """
        for _ in range(so_sv):
            ma_sv = ''.join(["SV" , str(random.randint(4, 1000))])
            ho_ten = random.choice(['Nguyen Van E', 'Nguyen Thi F', 'Tran Van G']) 
            gpa = round(random.uniform(0, 10), 1)
            self.danh_sach_sv.append(SinhVien(ma_sv, ho_ten, gpa))
            
    def xuat_sv_gpa_max(self):
        """
        Xuất thông tin sinh viên có GPA lớn nhất.
        """
        sv_max_gpa = max(self.danh_sach_sv, key=lambda sv: sv.gpa)
        print(sv_max_gpa.xuat_thong_tin())
        
    def cap_nhat_xep_loai_tat_ca(self):
        """
        Cập nhật xếp loại học lực cho tất cả sinh viên.
        """
        for sv in self.danh_sach_sv:
            sv.xep_loai = sv.cap_nhat_xep_loai()
            
    def tim_sv_theo_ma(self, ma_sv):
        """
        Tìm sinh viên theo mã sinh viên.
        """
        for sv in self.danh_sach_sv:
            if sv.ma_sv == ma_sv:
                print(sv.xuat_thong_tin())
                return sv
        print("Không tìm thấy sinh viên với mã:", ma_sv)
        
    def tim_sv_theo_gpa(self, gpa):
        """
        Tìm các sinh viên theo điểm trung bình.
        """
        dem=0
        for sv in self.danh_sach_sv:
            if sv.gpa == gpa:
                dem=dem+1
                print(sv.xuat_thong_tin())
        if dem==0:
            print("Không tìm thấy sinh viên với gpa:", gpa)
    
    def top_sv_gpa_cao_nhat(self, so_sv=10):
        """
        Trả về danh sách 10 sinh viên có GPA cao nhất.
        """
        top_sv = sorted(self.danh_sach_sv, key=lambda sv: sv.gpa, reverse=True)
        for i in range(0, so_sv):
            sv = top_sv[i]
            print(sv.xuat_thong_tin())

    def top_sv_gpa_thap_nhat(self, so_sv=10):
        """
        Trả về danh sách 10 sinh viên có GPA thấp nhất.
        """
        bottom_sv = sorted(self.danh_sach_sv, key=lambda sv: sv.gpa)
        for i in range(0, so_sv):
            sv = bottom_sv[i]
            print(sv.xuat_thong_tin())
       

quan_ly_sv = QuanLySinhVien()
ds_sv_gvth = [
    ('SV1', 'Nguyen Van A', 8.2),
    ('SV2', 'Tran Thi B', 6.5),
    ('SV3', 'Le Van C', 9.0)
]
quan_ly_sv.them_sv(ds_sv_gvth)
quan_ly_sv.khoi_tao_ngau_nhien(10)
quan_ly_sv.xuat_thong_tin_sv()

print("\nSinh viên có GPA lớn nhất:")
quan_ly_sv.xuat_sv_gpa_max()

quan_ly_sv.cap_nhat_xep_loai_tat_ca()

print("\nSinh viên có mã SV2:")
quan_ly_sv.tim_sv_theo_ma("SV2")

print("\nSinh viên có GPA là 6.5:")
quan_ly_sv.tim_sv_theo_gpa(6.5)


print("\n Danh sách 10 sinh viên có GPA cao nhất.:")
quan_ly_sv.top_sv_gpa_cao_nhat()

print("\n Danh sách 10 sinh viên có GPA thấp nhất.:")
quan_ly_sv.top_sv_gpa_thap_nhat()
