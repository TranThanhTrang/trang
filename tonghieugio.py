# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:11:21 2024

@author: Administrator
"""

tinh1=input("Nhap gio phut giay thu nhat:")
h1=int(tinh1.split('h')[0])
ph1= int(tinh1.split('h')[1].split('p')[0])
gi1= int(tinh1.split('p')[1].split('s')[0])
tinh2=input("Nhap gio phut giay thu hai:")
h2=int(tinh2.split('h')[0])
ph2= int(tinh2.split('h')[1].split('p')[0])
gi2= int(tinh2.split('p')[1].split('s')[0])
c=h1*3600+ph1*60+gi1
d=h2*3600+ph2*60+gi2
a=c+d
gio1=a//3600
phut1=(a%3600)//60
giay1=a%60
print("tong 2 gio la:",gio1,"\bh",phut1,"\bp",giay1,"\bs")
if c<d :
    print("tong gio thu nhat phai lon hon tong gio thu hai")
else:
    b=c-d
    gio2=b//3600
    phut2=(b%3600)//60
    giay2=b%60
    print("hieu la:",gio2,"\bh",phut2,"\bp",giay2,"\bs")
    
    