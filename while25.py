# -*- coding: utf-8 -*-
"""
While25. n butun soni berilgan (n > 1). n sonidan katta bo’lgan birinchi Fibonachchi sonini
aniqlovchi programma tuzilsin. Fibonachchi sonlari while24 masalasida berilgan.

Created on Wed Jun 30 06:27:32 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
if n>1:
    a=1
    b=1
    fib=1
    while a<=n:
        a,b=a + b,a
    print(n,'sonidan katta bo\'lgan birinchi fibonachchi soni:',a)
else:
    print('Masala shartiga mos son kiritilmadi! n>1 bo\'lishi kerak edi')    
