# -*- coding: utf-8 -*-
"""
While20. n butun soni berilgan (n > 0). Bo’lib butun va qoldiq qismlarini aniqlash orqali, berilgan son
raqamlarining orasida 2 raqami bor – yo’qligini aniqlovchi programma tuzilsin.

Created on Tue Jun 29 19:35:46 2021

@author: Mansurjon Kamolov
"""

#1-usul
n=int(input('n='))
if n>0:
    borligi = False
    k=0
    while n>0 and not(borligi):
        raqam = n % 10
        n=n//10
        if raqam == 2:
            borligi=True
    if borligi :
        print('2 raqami mavjud')
    else:
        print('2 raqami mavjud emas')
else:
    print('Masala shartiga mos son kiritilmadi! n>0 bo\'lishi kerak edi')

#2-usul 
n = int(input("n= "))
while n > 0:
    a = n % 10
    if a == 2:
        print('2 bor')
        break
    n = n // 10
else:
    print('2 mavjud emas')
