# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:43:08 2024

@author: Administrator
"""

import math
n=int(input("nhap vao so nguyen duong: "))
if n > 0:
    sqrtn = int(math.sqrt(n))
    if sqrtn * sqrtn == n:
        print(n,"la so chinh phuong")
    else:
        print(n,"khong la so chinh phuong")
else:
    print("khong phai so nguyen duong")