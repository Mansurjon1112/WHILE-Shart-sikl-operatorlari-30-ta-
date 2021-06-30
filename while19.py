# -*- coding: utf-8 -*-
"""
While19. n butun soni berilgan (n > 0). Bo’lib butun va qoldiq qismlarini aniqlash orqali, berilgan son
raqamlari yig’indisini va raqamlari sonini chiqaruvchi programma tuzilsin.

Created on Tue Jun 29 19:33:15 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
if n>0:
    natija = 0
    k=0
    while n>0:
        raqam = n % 10
        n=n//10
        natija += raqam
        k+=1
    print("Raqamlar yig'indisi",natija,' Raqamlar soni',k)
else:
    print('Masala shartiga mos son kiritilmadi! n>0 bo\'lishi kerak edi')
    