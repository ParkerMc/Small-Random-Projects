def toArray(filename): # Loads the file to array
    f = open(filename, "r")
    tempOut = f.readlines()
    f.close()
    out = []
    for i in tempOut:
        out.append(i.replace("\n", ""))
    return out

#Load files
twoLetter = toArray("2letterwords.txt")
threeLetter = toArray("3letterwords.txt")
fourLetter = toArray("4letterwords.txt")

def works(word, twoLetter=twoLetter, threeLetter=threeLetter, fourLetter=fourLetter):
    nextStep = False
    if word.replace("\n", "")[0] in ["A","I","O"]: # For (1)-2345
        nextStep = True
    elif word.replace("\n", "")[1:] in fourLetter: # For 1-(2345)
        nextStep = True
    if not nextStep:
        return

    nextStep = False
    if word.replace("\n", "")[-1] in ["A","I","O"]: # For 1234-(5)
        nextStep = True
    elif word.replace("\n", "")[:-1] in fourLetter: # For (1234)-5
        nextStep = True
    if not nextStep:
        return

    nextStep = False
    if word.replace("\n", "")[:-2] in twoLetter: # For (12)-345
        nextStep = True
    elif word.replace("\n", "")[-3:] in threeLetter: # For 12-(345)
        nextStep = True
    if not nextStep:
        return

    nextStep = False
    if word.replace("\n", "")[2:] in twoLetter: # For 123-(45)
        nextStep = True
    elif word.replace("\n", "")[:3] in threeLetter: # For (123)-45
        nextStep = True
    if not nextStep:
        return

    print(word.replace("\n", ""))

f = open("5letterwords.txt", "r")
index = 0
for i in f.readlines():
    for j in i.split(" "):
        index += 1
        works(j)
print(str(index)+" Words scanned")
