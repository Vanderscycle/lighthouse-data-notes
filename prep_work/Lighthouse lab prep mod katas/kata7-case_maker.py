# reminder:
#  strings are ummutable so: sentence[index + 1] = '' does not work  you get around that by creating a new string
# also .pop() is for list only

# INPUT: a string
# OUTPUT: same string but without spaces and with camel notation

def camelCase(sentence):
    sentence = sentence.strip()
    camelResult = str()
    for index, letter in enumerate(sentence):

        #if index == len(sentence):
        #    pass
        #else:
        if sentence[index-1] == ' ':
            camelResult += letter.upper()
        elif index == 0:
            camelResult += letter.upper()
        else:
            camelResult += letter

    camelResult = camelResult.replace(' ','')
    return camelResult

print(camelCase("this is a string"))
print(camelCase("   loopy lighthouse    "))
print(camelCase("supercalifragalisticexpialidocious"))