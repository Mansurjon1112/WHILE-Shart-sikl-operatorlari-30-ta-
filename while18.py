# -*- coding: utf-8 -*-
"""
While18. n butun soni berilgan (n > 0). Bo’lib butun va qoldiq qismlarini aniqlash orqali, berilgan son
raqamlarini teskari tartibda chiqaruvchi programma tuzilsin.

Created on Tue Jun 29 19:22:40 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
if n>0:
    natija = 0
    while n>0:
        raqam = n % 10
        n=n//10
        natija = natija*10 + raqam
    print(natija)
else:
    print('Masala shartiga mos son kiritilmadi! n>0 bo\'lishi kerak edi')