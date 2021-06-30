# -*- coding: utf-8 -*-
"""
While2. A va B butun musbat sonlari berilgan ( A > B). A usunlikdagi kesmada B kesmadan nechta
joylashtirish mumkinligini aniqlovchi programma tuzilsin. Ko’paytirish va bo’lish amallarini
ishlatmang.

Created on Tue Jun 29 05:42:08 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
b=int(input('B='))
if a>b:
    c=0
    while a>=b:
        a=a-b
        c+=1
    print('B kesmadan ',c,'ta joylashtirish mumkin')
else:
    print('Masala shartiga mos son kiritilmadi! A>B ')