# -*- coding: utf-8 -*-
"""
While6. n natural soni berilgan (n > 0). Quyidagi ifodani hisoblovchi programma tuzilsin:
n!! = n * (n - 2) * (n - 4) …
Agar n juft bo’lsa oxirgi ko’payuvchi 2, toq bo’lsa 1 bo’ladi.

Created on Tue Jun 29 17:36:28 2021

@author: Mansurjon Kamolov
"""

n=int(input('N='))
p=1
if n>0:
    while n>=1:
        p*=n
        n-=2
    print(p)
else:
    print('Masala shartiga mos son kiritilmadi! n>0 ')