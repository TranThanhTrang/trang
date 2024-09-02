# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:25:45 2024

@author: Administrator
"""

import math

def can_bac_x(n, x):
    """
    Tính căn bậc x của n.

    Parameters
    ----------
    n : int
        Số n
    x : int
        Số căn bậc hai

    Returns
    -------
    float
        Kết quả căn bậc x của n
    """
    return n ** (1 / x)

def dao_nguoc(n):
    """
    Tính số đảo ngược của n.

    Parameters
    ----------
    n : int
        Số n

    Returns
    -------
    int
        Kết quả đảo ngược của n
    """
    return int(str(n)[::-1])

def la_so_chinh_phuong(n):
    """
    Kiểm tra n là số chính phương

    Parameters
    ----------
    n : int
        Số n

    Returns
    -------
    Boolean
        Kết quả n có phải là số chính phương hay không
    """
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def la_so_nguyen_to(n):
    """
    Kiểm tra n là số nguyên tố

    Parameters
    ----------
    n : int
        Số n

    Returns
    -------
    Boolean
        Kết quả n có phải là số nguyên tố hay không
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def tich_cac_chu_so_le(n):
    """
    Tính tích các chữ số lẻ

    Parameters
    ----------
    n : int
        Số n

    Returns
    -------
    int
        Tích của các chữ số lẻ theo n
    """
    tich = 1
    has_odd = False
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            tich *= digit
            has_odd = True
        n //= 10
    return tich if has_odd else 0

# f) Phương thức tính tổng các số nguyên tố nhỏ hơn n
def tong_cac_so_nguyen_to_nho_hon_n(n):
    """
    Tỉnh tổng các số nguyên tố nhỏ hơn n

    Parameters
    ----------
    n : int
        Số n

    Returns
    -------
    int
        Tổng các số nguyên tố nhỏ hơn n
    """
    tong = 0
    for i in range(2, n):
        if la_so_nguyen_to(i):
            tong += i
    return tong

def tong_cac_so_chinh_phuong_nho_hon_n(n):
    """
    Tính tổng các số chính phương nhỏ hơn n

    Parameters
    ----------
    n : int
        Số n

    Returns
    -------
    int
        Tổng của các số chính phương nhỏ hơn n
    """
    tong = 0
    for i in range(1, n):
        if la_so_chinh_phuong(i):
            tong += i
    return tong

def tong_cac_uoc_so_duong(n):
    """
    Tính tổng các ước số dương của n

    Parameters
    ----------
    n : int
        Số n

    Returns
    -------
    int
        Tổng các ước số dương của n
    """
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong

n = int(input("nhap vap so nguyen duong n: "))

print("Can bac 2 cua n la:", can_bac_x(n, 2))
print("So dao nguoc cua n la:", dao_nguoc(n))
print("N co phai la so chinh phuong khong?", la_so_chinh_phuong(n))
print("N co phai la so nguyen to khong?", la_so_nguyen_to(n))
print("Tich cac chu so le cua n la:", tich_cac_chu_so_le(n))
print("Tong cac so nguyen to nho hon n la:", tong_cac_so_nguyen_to_nho_hon_n(n))
print("Tong cac so chinh phuong nho hon n la:", tong_cac_so_chinh_phuong_nho_hon_n(n))
print("Tong cac uoc so duong cua n la:", tong_cac_uoc_so_duong(n))
