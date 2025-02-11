teikums1=input()
print()
print(len(teikums1.split()))

print(teikums1[-2])
vardi = teikums1.split()
for i in range(len(vardi)-1): 
    print(vardi[i][-1])
print(vardi[len(vardi)-1][-2])



