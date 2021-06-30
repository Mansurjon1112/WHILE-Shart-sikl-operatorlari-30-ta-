# -*- coding: utf-8 -*-
"""
While21. n butun soni berilgan (n > 0). Bo’lib butun va qoldiq qismlarini aniqlash orqali, berilgan son
raqamlarining orasida toq raqamlar bor – yo’qligini aniqlovchi programma tuzilsin.

Created on Tue Jun 29 19:43:38 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
if n>0:
    borligi = False
    k=0
    while n>0 and not(borligi):
        raqam = n % 10
        n=n//10
        if raqam %2 == 1:
            borligi=True
    if borligi :
        print('Toq raqam mavjud')
    else:
        print('Toq raqam mavjud emas')
else:
    print('Masala shartiga mos son kiritilmadi! n>0 bo\'lishi kerak edi')
    