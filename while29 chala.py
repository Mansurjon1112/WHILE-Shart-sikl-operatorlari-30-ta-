# -*- coding: utf-8 -*-
"""
While29. e haqiqiy musbat soni berilgan. Ketma - ketlik xadlari quyidagicha aniqlanadi:
a1=1; a2=2; ak = ( ak – 2 + 2 * ak - 1 ) / 3; k = 3, 4, …
|ak – ak-1| < e shartni qanoatlantiruvchi eng kichik k sonini aniqlovchi programma tuzilsin.
ak va ak – 1 ham ekranga chiqarilsin.

Created on Wed Jun 30 07:07:04 2021

@author: Mansurjon Kamolov
"""

e=float(input('e='))
if e>0 :
    a=1
    ak=2
    k=2
    while abs(ak-a)<e:
        k+=1
        ak=a+2*ak
        a=ak
        
        print(k, ak, a)
    
else:
    print('e soni musbat bo\'lishi kerak!')
