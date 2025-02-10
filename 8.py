n = int(input())
der_no = it(input())
der_lidz = int(input())
for i in range (1,n):
    no = int (input())
    lidz = int(input())
if no<der_no: 
 der_no = no 
if lidz<der_lidz:
   der_lidz = lidz
if der_no<der_lidz:
   print("JĀ")
else:
   print("NĒ")