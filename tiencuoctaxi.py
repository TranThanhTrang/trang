# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:18:31 2024

@author: Administrator
"""

so=float(input("so km di duoc la: "))
tien=0
if so==1:
    tien=15000
elif so>=2 and so<=5 :
    tien=15000+(so-1)*13500
elif so>5 and so<120:
    tien=15000+(5-1)*13500+ (so-5)*11000
else:
    tien=15000+(5-1)*13500+ (so-5)*11000
    tien=tien*0.9
print("so tien phai tra la:",tien)

