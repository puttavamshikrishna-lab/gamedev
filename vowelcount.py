inputstr=input("Enter a sentence:")
vowels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0,
}

for c in inputstr:
    if c in vowels:
        vowels[c]+=1

print(vowels)