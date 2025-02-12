vrb = input("Give me a present tense verb (-ing ending)")
pstV = input("Give me 2 past tense verbs (preferably both ending in -ed)")
nn = input("Now give me 2 animals or mythical creatures")
obj = input("Name an object")
num = input("Tell me a number")
celeb = input("Name a celebrity")


nn = nn.split()
nnA = nn[0]
nnB = nn[1]
pstV = pstV.split()
pstVa, pstVb = pstV
celeb = celeb.capitalize()
obj = obj.capitalize()


print(f"{celeb} was {vrb}, until the {nnA} {pstVa}. {obj}s {pstVb}. {celeb}'s {num} {nnB}s also {pstVb}. Everything was chaos.")