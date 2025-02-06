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
else :
    print("Please answer with one of the options")


#Input then factor

