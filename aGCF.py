#GCF
frt = input("Type number")
scd = input("Type another number")

frt = int(frt)
scd = int(scd)

fct = []
fctB = []

def ftr(y):
    for i in range(1, y + 1):
        if y % i == 0:
            fct.append(i)

def ftrB(y):
    for i in range(1, y + 1):
        if y % i == 0:
            fctB.append(i)

ftr(frt)
ftrB(scd)

cf = []

for item in fct:
    if item in fctB:
        cf.append(item)

gcf = max(cf)

print(f"The greatest common factor between {frt} and {scd} is {gcf}")