stuff = input()
t = 0
s = 0

for i in stuff:
    if i == "TAKEN":
        t += 1
    elif i == "SERVE":
        s += 1
    elif i == "CLOSED":
        print(f"{t}  \n")