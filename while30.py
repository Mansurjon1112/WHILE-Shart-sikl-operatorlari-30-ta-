# -*- coding: utf-8 -*-
"""
While30. A, B, C musbat butun sonlari berilgan. A x B to’rtburchak ichida tomoni C bo’lgan
kvadratdan nechtasi sig’ishini aniqlovchi programma tuzilsin. Ko’paytirish va bo’lish amallarini
ishlatmang

Created on Wed Jun 30 06:59:39 2021

@author: Mansurjon Kamolov
"""

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

if a>0 and b>0 and c>0 :
    sanoq=0
    while a>=c:
        d=b
        while d>=c:
            sanoq+=1
            d-=c
        a-=c
    print(sanoq)
else:
    print('a,b,c sonlari musbat bo\'lsin!')
