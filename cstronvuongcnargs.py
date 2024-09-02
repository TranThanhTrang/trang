# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:47:26 2024

@author: Administrator
"""

import math

def tinh(*args, **kwargs):
    """
    Hàm tính chu vi và diện tích cho hình vuông, hình chữ nhật và hình tròn.

    Parameters
    ----------
    *args : tuple
        Các đối số không bắt buộc, có thể chứa kích thước các cạnh hoặc bán kính.
    **kwargs : dict
        Các đối số đặt tên, xác định loại hình (hinh) và kiểu tính toán (tinh).

    Returns
    -------
    float
        Kết quả tính chu vi hoặc diện tích dựa trên tham số đầu vào.
    """
    hinh = kwargs.get('hinh')
    tinh = kwargs.get('tinh')
    
    if hinh == 'vuong':
        canh = args[0]
        if tinh == 'cv':
            return 4 * canh  
        elif tinh == 'dt':
            return canh * canh 
    
    elif hinh == 'chu_nhat':
        dai, rong = args
        if tinh == 'cv':
            return 2 * (dai + rong)  
        elif tinh == 'dt':
            return dai * rong  
    
    elif hinh == 'tron':
        ban_kinh = args[0]
        if tinh == 'cv':
            return 2 * math.pi * ban_kinh  
        elif tinh == 'dt':
            return math.pi * ban_kinh ** 2  
    
    else:
        return "Hinh khong duoc ho tro hoac tham so sai."

print(tinh(10, hinh='vuong', tinh='cv'))  
print(tinh(50, hinh='vuong', tinh='dt'))  
print(tinh(18, hinh='tron', tinh='cv'))   
print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))  