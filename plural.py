#this program makes a singular word plural

#get user input
def word_get():
    return input("Please enter a word: ")

#pluralize word
def plural(word):
    #if the last 2 characters are 'ch' or 'sh', add 'es'
    if word.endswith("ch") or word.endswith("sh"):
        word += "es"
        return word
    
    #if the last character is 's', 'x', or 'z', add 'es'
    elif word.endswith("s") or word.endswith("x") or word.endswith("z"):
        word += "es"
        return word
    
    #if the last character is 'y' and the second-to-last is a consonant, replace 'y' with 'ies'
    elif word.endswith("y") and word[-2] not in "aeiou":
        word = word[0:-1] + "ies"
        return word
    
    #if the last character is 'f', replace 'f' with 'ves'
    elif word.endswith("f"):
        word = word[0:-1] + "ves"
        return word
    
    #if the last 2 characters are 'ef', replace 'ef' with 'ves'
    elif word.endswith("ef"):
        word = word[0:-2] + "ves"
        return word
    
    #otherwise, add 's'
    else:
        word = word + "s"
        return word

#call to get word function and set singlular word to the output of get_world
word_single = word_get()

#call to get pluralize the singlular word
word_plural = plural(word_single)

#print results
print(f"The plural form of {word_single} is {word_plural}.")