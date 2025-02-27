stuff = input()
stuff = stuff.upper()
stuff = stuff.split()

num = int(stuff[0])

t = 0
s = 0

for i in stuff:
    if i == "TAKE":
        t += 1
    elif i == "SERVE":
        s += 1
    elif i == "CLOSE":
        w = t - s
        num += t
        print(f"{t} {w} {num}\n")
        t = 0
        s = 0
