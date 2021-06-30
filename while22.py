# -*- coding: utf-8 -*-
"""
While22. n butun soni berilgan (n > 1). N sonini tub yoki tub emasligini aniqlovchi programma
tuzilsin.

Created on Wed Jun 30 06:08:38 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
if n>1 :
    i=1
    tekshir = False
    while i*i<n and not(tekshir):
        i+=1
        if n % i == 0:
            tekshir = True
    if tekshir:
        print('Tub son emas')
    else: 
        print('Tub son')
        
else:
    print('Masala shartiga mos son kiritilmadi! n>0 bo\'lishi kerak edi')