# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:48:33 2024

@author: Administrator
"""

so = int(input("Nhap so bat ki: "))

so_thanh_chuoi = {
    0: "Khong",
    1: "Mot",
    2: "Hai",
    3: "Ba",
    4: "Bon",
    5: "Nam",
    6: "Sau",
    7: "Bay",
    8: "Tam",
    9: "Chin"
}


if 0 <= so <= 9:
    print(so_thanh_chuoi[so])
else:
    print("Khong doc duoc")
