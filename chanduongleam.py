# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:58:06 2024

@author: Administrator
"""

def kiemtraso(n):
    """
    Kiểm tra n nếu:
        -số âm có giá trị lẻ thì trả về -1
        -số dương có giá trị chẵn thì trả về 1
        trường hợp khác trả về 0.

    Parameters
    ----------
    n : int
        Số n cần kiểm tra

    Returns
    -------
    int
        Kết quả của số n trả về giá trị -1,1,0
    """
    if n < 0 and n%2==1:
        return -1
    elif n>0 and n%2==0:
        return 1
    return 0

n=int(input("nhap so n:"))
if kiemtraso(n) ==-1:
    print("n la so le am")
elif kiemtraso(n)==1:
    print("n la so chan duong")
else: 
    print("n khong la so le am ma cung khong la so chan duong")