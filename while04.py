# -*- coding: utf-8 -*-
"""
While4. n butun soni berilgan (n > 0). Agar n soni 3 ning darajasi bo’lsa “3 – ning darajasi”, aks
xolda “3 – ning darajasi emas” degan natija chiqaruvchi programma tuzilsin. Qoldiqli bo'lish va
bo’lish amallarini ishlatmang.

Created on Tue Jun 29 05:49:22 2021

@author: Mansurjon Kamolov
"""

n=int(input('N='))
if n>0:
    b=1
    while n>b:
        b*=3
    if n==b:
        print("3 – ning darajasi")
    else:
        print("3 – ning darajasi emas")
else:
    print('Masala shartiga mos son kiritilmadi! n>0 ')