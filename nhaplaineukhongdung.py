# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:04:44 2024

@author: Administrator
"""

def kiemtraso(n):
    """
    Kiểm tra n có thuộc đoạn [-89, 90] hay không.

    Parameters
    ----------
    n : int
        Số n cần kiểm tra

    Returns
    -------
    Boolean
        True: Nếu n thuộc đoạn [-89, 90]
        False: Nếu n không thuộc đoạn [-89, 90]
    """
    if n >= -89 and n <= 90:
        return True
    return False

while True:
    n=int(input("nhap so n:"))
    if kiemtraso(n) == True:
        print("so hop le")
        break
    else:
        print("vui long nhap lai")