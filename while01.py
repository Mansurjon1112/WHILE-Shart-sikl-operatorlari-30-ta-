# -*- coding: utf-8 -*-
"""
While1. A va B butun musbat sonlari berilgan ( A > B). A usunlikdagi kesmada maksimal darajada
B kesma joylashtirilgan. A kesmaning bo’sh qismini aniqlovchi programma tuzilsin. Ko’paytirish va
bo’lish amallarini ishlatmang

Created on Tue Jun 29 05:42:22 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
b=int(input('B='))
if a>b:
    while a>=b:
        a=a-b
    if a==0:
        print("Bo'sh joy qolmadi")
    else:
        print('qolgan qismi:',a)
else:
    print('Masala shartiga mos son kiritilmadi! A>B ')