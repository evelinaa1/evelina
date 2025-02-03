a = int(input())
malka_kopa = int(input())

for i in range(1,k+1,1):
    saina_masa = int (input())
    saina_cena = int (input())
    saina_daudzums = malka_kopa//saina_masa
    if malka_kopa%saina_masa>0:
        sainu_daudzums+=1
    nauda = sainu_daudzums*saina_cena
    if nauda<min_saina_cena:
        mi_saina_cena=nauda
print(min_saina_cena)
