# -*- coding: utf-8 -*-
"""
While8. n natural soni berilgan (n > 0). Kvadrati n dan katta bo’lmagan eng katta butun k sonini
(k2 <= n) aniqlovchi programma tuzilsin. Ildizdan chiqaruvchi funksiyadan foydalanmang.

Created on Tue Jun 29 17:45:11 2021

@author: Mansurjon Kamolov
"""

n=int(input('N='))
if n>0:
    k=1
    while (k+1)*(k+1)<=n:
        k+=1
    print(k)        
else:
    print('Masala shartiga mos son kiritilmadi! n>0 ')
