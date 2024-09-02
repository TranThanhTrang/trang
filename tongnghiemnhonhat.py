# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:33:14 2024

@author: Administrator
"""

tongnhonhat=979
bonghiem = ()
for x in range(1, 980 // 2 + 1):
    for y in range(1, (980 - 2 * x) // 7 + 1):
        for z in range(1, (980 - 2 * x - 7 * y) // 9 + 1):
            if 2 * x + 7 * y + 9 * z == 979:
                tong = x + y + z
                if tong < tongnhonhat:
                    tongnhonhat = tong
                    bonghiem = (x, y, z)
if bonghiem:
    print(f"bo nghiem (x, y, z) = {bonghiem} co tong x + y + z nho nhat la {tongnhonhat}.")
else:
    print("Khong tim thay bo nghiem.")
    