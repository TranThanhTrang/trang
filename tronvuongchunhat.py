# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:22:12 2024

@author: Administrator
"""

import math

hinh = input("Nhập hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ").lower()
if hinh == 'v':
    canh = float(input("Nhập cạnh của hình vuông: "))
    chuvi = 4 * canh
    dientich = canh * canh
    print(f"Kết quả P = {chuvi}, S = {dientich}")
elif hinh == 'n':
    chieurong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    chieudai = float(input("Nhập chiều dài của hình chữ nhật: "))
    chuvi = 2 * (chieudai + chieurong)
    dientich = chieudai * chieurong
    print(f"Kết quả P = {chuvi}, S = {dientich}")
elif hinh == 't':
    bankinh = float(input("Nhập bán kính của hình tròn: "))
    chuvi = 2 * math.pi * bankinh
    dientich = math.pi * bankinh * bankinh
    print(f"Kết quả P = {chuvi:.2f}, S = {dientich:.2f}")
else:
    print("Hình nhập không hợp lệ")
