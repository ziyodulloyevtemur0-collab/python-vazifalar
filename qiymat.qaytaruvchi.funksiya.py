# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 23:05:58 2026

@author: user
"""

#Bu ancha qiyin ekan o'zim tushunishga, qilishga qiynaldim 
#buni javoblaridan oldim va har birini tahlil qilib chiqdim nima uchun buna qilinganligini

# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")



# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring,
# va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar 
# haqidagi ma'lumotni konsolga chiqaring.

#print(mijozlar)-----mijozlar ro'yxati shakllantirildi 


# def kattasini_qaytar(x,y,z):
#     """katta sonni topib beradi"""
#     if x>y:
#         return x
#     elif x<y:
#         return y
#     else:
#         return " sonlar teng "
# print("kattasini chiqaradi")
# kattasini_qaytar(4, 5, 9)


# def aylana_top(radius):
 #   """Aylana parametrlarini hisoblovchi funksiya"""
#     aylana={
#         "radius":radius,
#         "diametr":radius*2,
#         "perimetri":radius*2*3.14,
#         "yuzi":radius**2*3.14
#         }
#     return aylana

# def tub_sonmi(son):
#     """Bu funksiyalar tub sonlarni topib beradi 1-funksiya tublikka tekshiradi,
#     2-tublarni ro'yxatga joylaydi"""
#     if son < 2:
#         return False
#     for i in range(2, int(son**0.5) + 1):
#         if son % i == 0:
#             return False
#     return True

# def tub_sonlarni_ber(min_son,max_son):
#   """Bu funksiyalar tub sonlarni topib beradi 1-funksiya tublikka tekshiradi,
#        2-tublarni ro'yxatga joylaydi"""
#   royxat=[]
#   for i in range(min_son,max_son+1):
#        if tub_sonmi(i):
#             royxat.append(i)
#   return(print(royxat, end=''))


























































