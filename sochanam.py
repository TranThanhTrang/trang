# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:43:05 2024

@author: Administrator
"""
def kiemtrachanam(n):
    """
    Kiểm tra n có phải là số chẵn âm hay không.

    Parameters
    ----------
    n : int
        Số n cần kiểm tra

    Returns
    -------
    Boolean
        Kết quả của số n có phải là chẵn âm không.
    """
    if n < 0 and n%2==0:
        return True
    return False

n=int(input("nhap so n:"))
if kiemtrachanam(n):
    print("n la so chan am")
else: 
    print("n khong la so chan am")