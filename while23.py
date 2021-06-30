# -*- coding: utf-8 -*-
"""
While23. a va b butun musbat sonlari berilgan. Berilgan sonlarning eng katta umumiy bo’luvchisini
aniqlovchi programma tuzilsin.

Created on Wed Jun 30 06:18:17 2021

@author: Mansurjon Kamolov
"""

a= int(input('a='))
b= int(input('b='))
if a>0 and b>0 :
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    print('EKUB',a)
else:
    print('a ga ham b ga ham musbat son kiriting!')