numT = 0
numS = 0

sent = input("Give me a sentence in English or French.")

for i in sent:
     if i == "t" or  i == "T":
          numT = numT + 1
     if i == "s" or i == "S":
          numS = numS + 1

if numS > numT:
     print("French")
elif numT > numS:
     print("English")