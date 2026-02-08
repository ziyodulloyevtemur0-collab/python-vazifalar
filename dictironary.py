



# otam={"ism":'Maqsud',"yosh":"55","familiya":"bomulloyev","shahar":"koson"}
# print(f" {otam["ism"].upper() } mening otam , familiyalari  {otam["familiya"].title()}, {otam["shahar"].title() }da tugilganlar")



# sevimli_taom={"ali":"osh","vali":"somsa","toshmat":"manti"}
# print(f"Alining sevimli taomi{sevimli_taom["ali"].capitalize()},\n>> {sevimli_taom["vali"].title()}- bu esa valiniki , {sevimli_taom["toshmat"].upper()} Toshmatning tanlovi")



# python={}
# python["int"]="butun son"
# python["if"]="agar operatori"
# python["list"]="ro'yxat"
# python["string"]="matn bilan ishlsh"
# print(python)

# soz=input("biror so'z kiriting\n>> ").lowerr()
# print(python.get(soz, 'mavjud emas'))


python={}
python["int"]="butun son"
python["if"]="agar operatori"
python["list"]="ro'yxat"
python["string"]="matn bilan ishlsh"
print(python)

soz=input("biror so'z kiriting\n>> ")
tarjima=python.get(soz)
if tarjima==None:
    print("mavjud emas")
else: print(f"{soz.title()} sozi {tarjima} deb tarjima qilinadi")


























