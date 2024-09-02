# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:40:32 2024

@author: Administrator
"""

import math

def tong_tu_1_den_n(n):
    """
    Tính tổng từ 1 đến n.

    Parameters
    ----------
    n : int
        Số nguyên dương n

    Returns
    -------
    int
        Tổng S = 1 + 2 + 3 + ... + n
    """
    return sum(range(1, n + 1))

def tong_binh_phuong_tu_1_den_n(n):
    """
    Tính tổng các bình phương từ 1 đến n.

    Parameters
    ----------
    n : int
        Số nguyên dương n

    Returns
    -------
    int
        Tổng S = 1^2 + 2^2 + 3^2 + ... + n^2
    """
    return sum(i**2 for i in range(1, n + 1))

def tong_nghich_dao_tu_1_den_n(n):
    """
    Tính tổng các nghịch đảo từ 1 đến n.

    Parameters
    ----------
    n : int
        Số nguyên dương n

    Returns
    -------
    float
        Tổng S = 1 + 1/2 + 1/3 + ... + 1/n
    """
    return sum(1 / i for i in range(1, n + 1))

def tong_giai_thua_tu_1_den_n(n):
    """
    Tính tổng các giai thừa từ 1! đến n!.

    Parameters
    ----------
    n : int
        Số nguyên dương n

    Returns
    -------
    int
        Tổng S = 1! + 2! + 3! + ... + n!
    """
    return sum(math.factorial(i) for i in range(1, n + 1))

def tich_tu_1_den_n(n):
    """
    Tính tích từ 1 đến n.

    Parameters
    ----------
    n : int
        Số nguyên dương n

    Returns
    -------
    int
        Tích S = 1 * 2 * 3 * ... * n
    """
    return math.prod(range(1, n + 1))

n = int(input("Nhap vao so nguyen duong n: "))
print("Tong S = 1 + 2 + 3 + ... + n la:", tong_tu_1_den_n(n))
print("Tong S = 1^2 + 2^2 + 3^2 + ... + n^2 la:", tong_binh_phuong_tu_1_den_n(n))
print("Tong S = 1 + 1/2 + 1/3 + ... + 1/n la:", tong_nghich_dao_tu_1_den_n(n))
print("Tong S = 1! + 2! + 3! + ... + n! la:", tong_giai_thua_tu_1_den_n(n))
print("Tich S = 1 * 2 * 3 * ... * n la:", tich_tu_1_den_n(n))
