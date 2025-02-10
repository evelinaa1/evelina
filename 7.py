nauda_kopa = int(input())
klientu_sk = int(input())
min_kg_cena = 30000.0
for i in range (klientu_sk):
    iep_masa = int(input())
    iep_cena = int(input())
    zimols = input()
    if zimols != "DOGO":
    kg_cena = iep_cena / iep_masa
    if kg_cena<min_kg_cena:
        min_kg_cena = kg_cena
        derigs_zimols = zimols
        iep_daudz = nauda_kopa // iep_cena
print(iep_daudz, derigs_zimols)



