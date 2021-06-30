# -*- coding: utf-8 -*-
"""
While3. N va K butun musbat sonlari berilgan. Faqat ayirish va qo’shish amallarini ishlatib N sonini
K soniga bo’lgandagi qoldiq va butun qismini aniqlovchi programma tuzilsin.

Created on Tue Jun 29 05:44:10 2021

@author: Mansurjon Kamolov
"""
n=int(input('N='))
k=int(input('K='))
if n>0 and k>0:
    c=0
    while n>=k:
        n=n-k
        c+=1
    if n==0 :
        print("Bo'linma:",c)
    else:
        print("To'liqsiz bo'linma:",c,"Qoldiq",n)
else:
    print('Musbat sonlarni kiriting.')