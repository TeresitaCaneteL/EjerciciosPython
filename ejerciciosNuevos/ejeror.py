ar=[]
cont=0
num=int(input("cuantos numero quiere?: "))
for x in range(num):
  ar.insert(x,int(input("ingrese numero:")))
  #if ar[-1] > ar[-2]:
  print(ar[x],"menor")
