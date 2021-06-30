# -*- coding: utf-8 -*-
"""
While17. n va m butun musbat sonlari berilgan (n > m). n sonini m soniga bo’lib butun va qoldiq
qismlarini bo’lish va qoldiqni olish amallarini ishlatmasdan topuvchi programma tuzilsin.

Created on Tue Jun 29 19:16:32 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
m=int(input('m='))
if n>m:
    butun = 0
    while n>=m:
        n-=m
        butun+=1
    if n!=0 : 
        print('To\'liqsiz bo\'linma qismi',butun,'Qoldiq',n)
    else:
        print('Qoldiqsiz bo\'linadi. Bo\'linma',butun)
else:
    print('Masala shartiga mos son kiritilmadi! n>m bo\'lishi kerak edi')