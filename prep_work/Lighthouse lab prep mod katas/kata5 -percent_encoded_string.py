

# INPUT: a string with whitespace throughout
# OUTPUT: a cleaned string with %20 instead of spaces between words
#  EXCEPTIONS: do not use replace()

def urlEncode(sentence):
    search_ready = str()

    for letter in sentence.strip(): #not sure if it saves more memory by adding one line of code: sentence += sentence.strip()
        if letter == ' ':
            search_ready += '%20'
        else:
            search_ready += letter
    return search_ready


print(urlEncode("Lighthouse Labs"))
print(urlEncode(" Lighthouse Labs  "))
print(urlEncode("blue is greener than purple for sure"))