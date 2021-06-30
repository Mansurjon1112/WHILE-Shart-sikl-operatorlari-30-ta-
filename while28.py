# -*- coding: utf-8 -*-
"""
While28. e haqiqiy musbat soni berilgan. Ketma - ketlik xadlari quyidagicha aniqlanadi:
a1=2; ak = 2 + 1 / ak – 1; k = 2, 3, …

|ak – ak-1| < e shartni qanoatlantiruvchi eng kichik k sonini aniqlovchi programma tuzilsin.
ak va ak – 1 ham ekranga chiqarilsin.

Created on Wed Jun 30 06:40:29 2021

@author: Mansurjon Kamolov
"""

e=float(input('e='))
if e>0 :
    a=2
    k=1
    while abs(2+1/a-a)>=e:
        k+=1
        ak=2+1/a
        ak,a=a,ak
    print(k+1)
    
else:
    print('e soni musbat bo\'lishi kerak!')