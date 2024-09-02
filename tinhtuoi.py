# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:16:17 2024

@author: Administrator
"""

import datetime
a=int(input("nhap vao nam sinh cua ban:"))
hientai = datetime.datetime.now().year
if a<0 :
    print("nam sinh khong hop le")
else:
    tuoi=hientai-a
    print("vay ban sinh nam",a,"va ban",tuoi,"tuoi")