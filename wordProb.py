e = []
x = (input("Please enter the price of items one by one"))

while x != "done":
     e.append(x)
     x = (input("next"))

t = 0

for i in e:
     i = int(i)
     t += i

if t >= 100:
     t *= 0.9

print(f"Total:${t}")