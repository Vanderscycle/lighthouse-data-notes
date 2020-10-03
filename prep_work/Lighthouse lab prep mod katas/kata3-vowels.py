# Counting the number of vowels in a given string

# Input: a string (of varaying length)
# Output number of vowels found

def numberOfVowels(sentence):
    vowels = ['a','e','i','o','u']
    vowels_count = 0
    for letter in sentence:
        if letter.lower() in vowels:
            vowels_count += 1
    return vowels_count


print(numberOfVowels("orange"))
print(numberOfVowels("ThIs SeNtEnCe HaS CaPiTaL LeTeRs"))
print(numberOfVowels("AEIOU"))