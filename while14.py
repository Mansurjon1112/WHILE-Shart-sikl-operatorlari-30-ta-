# -*- coding: utf-8 -*-
"""
While14. a soni berilgan (a > 1). (1 + 1 / 2 + 1 / 3 + … + 1 / k) <= a shart bajariladigan eng katta k
sonini aniqlovchi programma tuzilsin. Yig’indi ham ekranga chiqarilsin.
 
Created on Tue Jun 29 18:07:40 2021

@author: Mansurjon Kamolov
"""

a=float(input('N='))
if a>1:
    yig = 0
    k=0
    while yig + 1/(k+1) <=  a:
        k+=1
        yig+=1/k
    print('Eng katta k soni:',k,"Yig'indisi:",yig)
else:
    print('Masala shartiga mos son kiritilmadi! n>1 ')
