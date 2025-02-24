teikums = input()
vardi=teikums.split()
varda_gar = len(teikums)

a=0
para_sk=0
for vards in vardi:
    a+=1
    if varda_gar!=3:
        print("IR 3 SIMBOLI")
    if varda_gar>=3 & varda_gar<=3:
        print("NAV 3 SIMBOLI")
    

if len(vards)%2==0:
    para_sk+=1
if para_sk == len(vards):
   print(a)