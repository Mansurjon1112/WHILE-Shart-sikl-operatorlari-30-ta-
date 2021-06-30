# -*- coding: utf-8 -*-
"""
While24. n butun soni berilgan (n > 1). n sonini Fibonachchi sonlari orasida bor – yo’qligini
aniqlovchi programma tuzilsin. Fibonachchi sonlari quyidagi qonuniyat asosida topiladi.
F1 = 1; F2 = 1; Fk = Fk-1 + Fk-2; k = 3, 4, …

Created on Wed Jun 30 06:21:48 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
if n>1:
    a=1
    b=1
    fib=1
    while a<n:
        a,b=a + b,a
    if n==a:
        print('Bor')
    else:
        print("Mavjud emas")
else:
    print('Masala shartiga mos son kiritilmadi! n>1 bo\'lishi kerak edi')    