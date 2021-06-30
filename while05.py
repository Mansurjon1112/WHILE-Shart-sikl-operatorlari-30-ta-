# -*- coding: utf-8 -*-
"""
While5. 2 sonining qandaydir darajasini bildiruvchi n butun soni berilgan (n > 0). n = 2k . k ni
aniqlovchi programma tuzilsin.

Created on Tue Jun 29 05:57:51 2021

@author: Mansurjon Kamolov
"""

n=int(input('N='))
if n>0:
    b=1
    k=0
    while n>b:
        b*=2
        k+=1
    if n==b:
        print('k =',k)
    else:
        print("2 ning darajasi emas")
else:
    print('Masala shartiga mos son kiritilmadi! n>0 ')