# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:18:14 2024

@author: le Thi Huyen Nga
"""
gio = int(input("Nhập giờ:"))
phut = int(input("Nhập phút:"))
giay = int(input("Nhập giây:"))
tong_giay = gio * 3600 + phut * 60 + giay
print ("Tổng số giây là:",tong_giay)
