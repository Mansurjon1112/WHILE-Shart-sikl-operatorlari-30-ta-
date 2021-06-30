# -*- coding: utf-8 -*-
"""
While9. n natural soni berilgan (n > 1). 3k > n shartni qanoatlantiruvchi eng kichik butun k sonini
aniqlovchi programma tuzilsin.

Created on Tue Jun 29 17:51:38 2021

@author: Mansurjon Kamolov
"""

n=int(input('N='))
if n>0:
    p=1
    k=0    
    while p<=n:
        p*=3
        k+=1
    print(k)        
else:
    print('Masala shartiga mos son kiritilmadi! n>0 ')
