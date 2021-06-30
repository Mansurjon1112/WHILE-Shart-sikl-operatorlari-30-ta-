# -*- coding: utf-8 -*-
"""
While26. Fibonachchi soni bo’lgan n butun soni berilgan (n > 1). ( Fibonachchi sonlari while24
masalasida berilgan.) n sonidan bir oldingi va bir keyingi Fibonachchi sonlarini chiqaruvchi
programma tuzilsin.

Created on Wed Jun 30 06:29:46 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
if n>1:
    a=1
    b=1
    fib=1
    while a<=n:
        a,b=a + b,a
        if a==n :
            print('Oldingi fibonachchi soni:',b)            
    if n==b:
        print('Keyingi fibonachchi soni:',a)  
    else:
        print('Fibonachchi soni kiritilmadi')
else:
    print('Masala shartiga mos son kiritilmadi! n>1 bo\'lishi kerak edi')    
