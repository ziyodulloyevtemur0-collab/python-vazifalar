# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 14:48:18 2026

@author: user
"""

# def katta_harf_qil(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
        
# yozuv=["mehnat","yutuq","muhim"]
# katta_harf_qil(yozuv)
# print(yozuv)




# def katta_harf_qil(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
        
# yozuv=["mehnat","yutuq","muhim"]
# katta_harf_qil(yozuv[:])
# print(yozuv)





talabalar = ['tursunali', 'nozim', 'ahmad', 'yusuf']

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
        
baholar = bahola(talabalar)
print(baholar)
print(talabalar)

