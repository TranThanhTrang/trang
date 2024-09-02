# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:21:52 2024

@author: Administrator
"""

tonglonnhat = 0
bonghiem = ()
for x in range(1, 980 // 2 + 1):
    for y in range(1, (980 - 2 * x) // 7 + 1):
        for z in range(1, (980 - 2 * x - 7 * y) // 9 + 1):
            if 2 * x + 7 * y + 9 * z == 979:
                tong = x + y + z
                if tong > tonglonnhat:
                    tonglonnhat = tong
                    bonghiem = (x, y, z)
if bonghiem:
    print(f"bo nghiem (x, y, z) = {bonghiem} co tong x + y + z lon nhat la {tonglonnhat}.")
else:
    print("Khong tim thay bo nghiem.")
