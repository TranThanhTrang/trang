# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:17:30 2024

@author: Administrator
"""

def tinhchuvi(dai, rong):
    """
    Tính chu vi hình chữ nhật.

    Parameters
    ----------
    dai : float
        Chiều dài của hình chữ nhật.
    rong : float
        Chiều rộng của hình chữ nhật.

    Returns
    -------
    float
        Chu vi của hình chữ nhật.
    """
    return 2 * (dai + rong)

def tinhdientich(dai, rong):
    """
    Tính diện tích hình chữ nhật.

    Parameters
    ----------
    dai : float
        Chiều dài của hình chữ nhật.
    rong : float
        Chiều rộng của hình chữ nhật.

    Returns
    -------
    float
        Diện tích của hình chữ nhật.
    """
    return dai * rong

def vehinhchunhat(dai, rong):
    """
    Vẽ hình chữ nhật bằng các dấu *.

    Parameters
    ----------
    dai : int
        Chiều dài của hình chữ nhật (số cột).
    rong : int
        Chiều rộng của hình chữ nhật (số dòng).

    Returns
    -------
    None
    """
    for i in range(rong):
        print("*" * dai)

dai = float(input("Nhap chieu dai cua hinh chu nhat: "))
rong = float(input("Nhap chieu rong cua hinh chu nhat: "))

chuvi = tinhchuvi(dai, rong)
dientich = tinhdientich(dai, rong)

print("Chu vi hinh chu nhat la:", chuvi)
print("Dien tich hinh chu nhat la:", dientich)

vehinhchunhat(int(dai), int(rong))
