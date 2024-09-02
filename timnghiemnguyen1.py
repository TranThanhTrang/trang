# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:16:03 2024

@author: Administrator
"""

for x in range(1, 980 // 2 + 1):
    for y in range(1, 980 // 7 + 1):
        for z in range(1, 980 // 9 + 1):
            if 2 * x + 7 * y + 9 * z == 979:
                print(f"bo nghiem (x, y, z) = ({x}, {y}, {z})")