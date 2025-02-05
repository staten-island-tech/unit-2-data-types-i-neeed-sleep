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
bill = input("What was the bill?")
tip = input("Tip? [0%, 10%, 20%, 25%]")

if tip = "0%"