#GCF
frt = input("Type number")
scd = input("Type another number")

frt = int(frt)
scd = int(scd)

fct = []

def ftr(y):
    for i in range(1, y + 1):
        if y % i == 0:
            fct.append(i)
        if i > y:
            return(ftr)

ftr(frt)
ftr(scd)

fctA = list()

for i in range:
    

print(f"The greatest common factor between {frt} and {scd} is {fctA}")