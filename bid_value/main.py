#from replit import clear

maggy={}
m=False
while not m:
    a=input("enter your name")
    g=int(input("bid value"))
    maggy[a]=g
    y=input("is there any other person who wants to bid")
    if y=="no":
        m=True
    #else:
        #clear()
largest=None
for x in maggy:
    if largest is None or maggy[x]>largest:
        largest=maggy[x]
        maharshi=x
print(f"The {maharshi} made a highest bid:${largest}")

