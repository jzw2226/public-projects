# Prompt the user for a sentence or series of characters and record the input

text = input("Please enter a string: ")
newText = ""

# Check the first character of the input to see if it is a lowercase vowel (a, e, i o, or u) and if so, replace it with it's uppercase counterpart

for x in text:
    if x in {"a", "e", "i", "o", "u"}:
        newText += x.upper()
    elif x in {"B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"}:
        newText += x.lower()
    else:
        newText += x

# Repeat step 3 for every character in the input
# Display the new sentence or series of characters with the altered cases

print(newText)