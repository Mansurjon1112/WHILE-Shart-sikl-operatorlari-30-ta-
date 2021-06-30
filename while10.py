# -*- coding: utf-8 -*-
"""
While10. n natural soni berilgan (n > 1). 3k <= n shartni qanoatlantiruvchi eng katta butun k sonini
aniqlovchi programma tuzilsin.

Created on Tue Jun 29 17:53:30 2021

@author: Mansurjon Kamolov
"""

n=int(input('N='))
if n>0:
    p=1
    k=0    
    while p*3<=n:
        p*=3
        k+=1
    print(k)        
else:
    print('Masala shartiga mos son kiritilmadi! n>0 ')
