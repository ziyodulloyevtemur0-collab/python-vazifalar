# -*- coding: utf-8 -*-



# python={"if":"agar","keys":"kalit", "else":"aks holda","string":"matn"}
# for kalit,qiymat  in sorted(python.items()):
#     print(f"kalit:{kalit}")
#     print(f"qiymat:{qiymat}\n")


# davlatlar={
#     "ozbekiston":"tashkent",
#     "rossiya":"moskva",
#     "tojikiston":"dushanbe",
#     "amerika":"nyu-york"
#     }
# print("DUNYO DAVLATLARI:\n ")
# for davlat in sorted(davlatlar):
#      print(davlat.title())
     
# print(f"davlatlarning poytaxtlari:\n ".upper())
# for poytaxt in sorted(davlatlar.values()):
#         print(poytaxt.title())




# davlatlar={
#     "ozbekiston":"tashkent",
#     "rossiya":"moskva",
#     "tojikiston":"dushanbe",
#     "amerika":"nyu-york"
#     }
# davlat=input("davlat nomini kiriting men sizga poytaxtini topib beraman \n>>")
# poytaxt=davlatlar.get(davlat.lower())
# if poytaxt==None:
#     print("bu davlatni bilmayman")
# else :print(f"{davlat.upper()}ning poytaxti {poytaxt.title()} shahri")





menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
print("Xush kelibsiz")


soni=int(input("nechta taom buyurtma qilmoqchisiz\n>>"))
buyurtmalar=[]
for n in range(soni):
   buyurtma=input(f"{n+1}-taomingiz:\n>>").lower()
   buyurtmalar.append(buyurtma)
for buyurtma in buyurtmalar:
    if buyurtma in menu:
     print(f"{buyurtma.title()}-{menu[buyurtma]} som")
    else:
     print(f"bizda {buyurtma.title()} mavjud emas")





# n_people=int(input("nechta odam bilan ko'rishdingiz\n>>"))
# ismlar=[]  
# for n in range(n_people):
#    ismlar.append(input(f" {n+1}- odam kim:"))
# print(f"mana odamlaringiz {ismlar}")
























