# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:36:44 2024

@author: Administrator
"""

while True:
    month = int(input('Nhập vào tháng: '))
    year = int(input('Nhập vào năm: '))
    if 1 <= month <= 12 and year >= 0:
        break
month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]
if month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(year,'là năm nhuận và tháng 2 có 29 ngày.')
elif month in month_31:
    print('Tháng',month,'có 31 ngày.')
elif month in month_30:
    print('Tháng',month,'có 30 ngày.')
else:
    print(year,'là năm không nhuận và tháng 2 có 28 ngày.')