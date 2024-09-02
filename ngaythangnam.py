# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:33:01 2024

@author: Administrator
"""
day = int(input('Nhập ngày sinh: '))
mon = int(input('Nhập tháng sinh: '))
year = int(input('Nhập năm sinh: '))
    #câu a:
print('a) {:02}/{:1}/{:04}'.format(day,mon,year))

    #câu b:
year_short = year % 100
print('b) {:02}/{:1}/{:02}'.format(day,mon,year_short))

    #câu c:
print('c) {:04}/{:1}/{:02}'.format(year,mon,day))
