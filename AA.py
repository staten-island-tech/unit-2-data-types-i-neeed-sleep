#Counts words in a sentence
sentence = input("Input a sentence. ")
eee = sentence.split()

oo = 0

for i in eee:
    oo = oo + 1

print(f"There are {oo} words")


#Tells if a number is odd or even
n = input("The number is...")
n = int(n)

if n % 2 == 0:
    print("Which means it's even")
else:
    print("Which means it's odd")


#"Would you like to tip?"
bill = input("How much was the bill?")
ser = input("How was the service? [bad, okay, good, or great]")

if ser == "bad":
    tip = input("Would you like to tip 0%?")
elif ser == "okay":
    tip = input("Would you like to tip 10%?")
elif ser == "good":
    tip = input("Would you like to tip 20%?")
elif ser == "great":
    tip = input("Would you like to tip 25%?")


#Input then factor
nnn = input("Give a number")
nnn = int(nnn)

if nnn < 0:
    nnn = nnn * -1

def fac(x):
   print("The factors of",x,":")
   for i in range(1, x + 1):
        if x % i == 0:
           print(i)
        if i > x:
            return(fac)

fac(nnn)