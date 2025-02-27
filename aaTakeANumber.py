status = input()
t = 0
s = 0

for i in status:
    if i == "TAKEN":
        t += 1
    elif i == "SERVE":
        s += 1
    elif i == "CLOSED":
        print(f"{t} 0 23 \n")