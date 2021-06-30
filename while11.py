# -*- coding: utf-8 -*-
"""
While11. n natural soni berilgan (n > 1). (1 + 2 + 3 + … + k) >= n shart bajariladigan eng kichik k
sonini aniqlovchi programma tuzilsin. 1 dan k gacha bo’lgan yig’indi ham ekranga chiqarilsin.

Created on Tue Jun 29 17:55:16 2021

@author: Mansurjon Kamolov
"""
n=int(input('N='))
if n>1:
    yig = 0
    k=0
    while yig < n:
        k+=1
        yig+=k
    print('eng kichik son:',k," yig'indisi:",yig)
else:
    print('Masala shartiga mos son kiritilmadi! n>1 ')

