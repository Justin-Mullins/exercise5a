'''

Exercise 5a

In addition to the functions of your solution from exercies 5,
Handle capitalized words—If a word is capitalized (i.e., the first letter is capital-
ized, but the rest of the word is not), then the Pig Latin translation should be
similarly capitalized.

'''

def pig_latin(string1):
    first_letter = string1[0]
    if first_letter in 'aeiou':
        string1 += 'way'
    else:
        string1 = string1[1:] + first_letter + 'ay'
    if first_letter.isupper():
        string1 = f'{string1[0].upper()}{string1[1:].lower()}'
    return string1
 
print(pig_latin('Computer'))
print(pig_latin('Python'))
print(pig_latin('arrow'))