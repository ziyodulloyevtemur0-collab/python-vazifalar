# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 16:25:07 2026

@author: user
"""

# def kopaytma_hisobla(*sonlar):
#    """kopaymani hisoblab beruvchu funksiya nechta sonligidan qatiy nazar hisoblaydi"""
#    kopaytma=1
#    for son in sonlar:
#         kopaytma*=son
#    return kopaytma
 
# print (kopaytma_hisobla(3,4,2,34))





def talabalar_malumotini_ber( ism, familiya,**talabalar):
    """talabalarni malumotlarini beradi bu funksiyamiz"""
    talabalar["ism"]=ism
    talabalar["familiya"]=familiya
    return talabalar 
talaba=talabalar_malumotini_ber("olim","rahimov",tyil=2000,fakultet="finance",yonalish="kb")
print(talaba)