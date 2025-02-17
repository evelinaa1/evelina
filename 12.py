teikums = input()
vardi = teikums.split(" ")
for vards in vardi:
    drukato_sk=0
    for i in range(len(vards)):
      if vards[i]>='A' and vards[i]<='Z':
         drukato_sk+=1
         print(drukato_sk)