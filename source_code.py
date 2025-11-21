print("VITyarthi Evaluated Course Project\nSubmitted by: Aditya Kundliya")
print("Shopping discount calculator")
items=[]
tb=0
while True:
    n=input("Enter the name of item purchased (type 'done' once all items are added): ")
    if n=="done":
        break
    p=int(input("Price: ₹"))
    q=int(input("Qty(n units): "))
    t=p*q
    items.append([n,p,q,t])
    tb+=t
print("Total before discount: ₹",tb)
print("Discount types: ")
print("1: Percentage discount")
print("2: Flat discount (in ₹)")
ch=int(input("Chooose the type of discount to be given: "))
if ch==1:
    d=float(input("Enter % discount: "))
    da=(d/100)*tb
elif ch==2:
    da=int(input("Enter flat discount (in ₹): "))
else:
    print("Invalid choice, no discount applied")
    da=0
ft=tb-da
print("BILL")
for i in items:
    print(f"{i[0]}-₹{i[1]}x{i[2]}=₹{i[3]}")
print("Total before discount: ₹",tb)
print("Discount: ₹",da)
print("Final amount: ₹",ft)
          
