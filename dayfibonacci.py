# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:43:37 2024

@author: Administrator
"""

def in_danh_sach_fibonacci(n):
    """
    In ra n phan tu dau tien cua day Fibonacci.

    Parameters
    ----------
    n : int
        So phan tu cua day Fibonacci can in ra (n >= 1)

    Returns
    -------
    None
    """
    if n <= 0:
        print("Nhap n phai lon hon 0.")
        return

    fibonacci = []
    
    if n == 1:
        fibonacci.append(0)
    
    if n == 2 or n > 2:
        fibonacci.append(0).append(1)
    
    if n > 2:
        for i in range(2, n):
            sotieptheo = fibonacci[i-2] + fibonacci[i-1]
            fibonacci.append(sotieptheo)
    
    print(" ".join(map(str, fibonacci)))

n = int(input("Nhap vao so phan tu cua day Fibonacci (n >= 1): "))

in_danh_sach_fibonacci(n)
