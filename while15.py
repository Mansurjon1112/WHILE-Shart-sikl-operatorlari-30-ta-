# -*- coding: utf-8 -*-
"""
While15. Bankka boshlang’ich S so’m qo’yildi. Har oyda bor bo’lgan summa p foizga oshadi (0 < p <
25 ). Necha oydan keyin boshlang’ich qiymat 2 martadan ko’p bo’lishini hisoblovchi programma
tuzilsin. Necha oy k – butun son. Bankda hosil bo’lgan summa haqiqiy son ekranga chiqarilsin

Created on Tue Jun 29 18:15:06 2021

@author: Mansurjon Kamolov
"""

s=int(input('Bankka qo\'yilgan pulni kiriting: '))
p=int(input('Foizni kiriting: '))
if 0<p<25:
    k=0
    natija=0
    while natija <= s:
        k+=1
        natija=s*p/100*k
    print(k)
else:
    print('Foiz 0 dan katta lekin 25 dan kichik son bo\'lsin')