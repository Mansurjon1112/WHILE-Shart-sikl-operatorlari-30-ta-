# -*- coding: utf-8 -*-
"""
While27. Fibonachchi soni bo’lgan n butun soni berilgan (n > 1). ( Fibonachchi sonlari while24
masalasida berilgan.) n soni Fibonachchi ketma – ketligining nechanchi xadi ekanini chiqaruvchi
programma tuzilsin.

Created on Wed Jun 30 06:36:58 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
if n>1:
    a=1
    b=1
    sanoq=2
    while a<n:
        a,b=a + b,a
        sanoq+=1
    if n==a:
        print(str(sanoq)+'-hadi')
    else:
        print('Fibonachchi soni kiritilmadi')
else:
    print('Masala shartiga mos son kiritilmadi! n>1 bo\'lishi kerak edi')    