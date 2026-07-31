name = input("What is your name : ")
letters = list(name)
print(letters)
count = 0
for letter in name:
    if letter == 'a' or letter == 'A':
        count = count + 1
    if letter == 'e' or letter == 'E':
        count = count + 1
    if letter == 'i' or letter == 'I':
        count = count + 1
    if letter == 'o' or letter == 'O':
        count = count + 1
    if letter == 'u' or letter == 'U':
        count = count + 1 

print(f"Your text you have",count,"vowels")