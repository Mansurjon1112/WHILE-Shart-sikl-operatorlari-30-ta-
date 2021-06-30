# -*- coding: utf-8 -*-
"""
While16. Sportsmen birinchi kuni 10 km yugirib boshladi. Keyingi kunlari bir oldingi kunga nisbatan
p foiz ko’p yugurdi (0 < p < 50). Sportsmenning necha kundan keyin jami yugurgan masogasi 200
km dan oshadi? Jami kunlar soni va masofani (butun son) chiqaruvchi programma tuzilsin.

Created on Tue Jun 29 19:00:12 2021

@author: Mansurjon Kamolov
"""

foiz=int(input('Necha foiz oshirdi:'))
kun=0
yigindi = 0
keyingi_kun = 10
while yigindi < 200:
    kun+=1
    yigindi += keyingi_kun
    keyingi_kun*=(1+foiz/100)
print('kunlar',kun,'masofa',yigindi,'~',round(yigindi))