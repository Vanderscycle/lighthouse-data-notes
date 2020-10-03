# 

# Input: a LIST of instructor dictionaries not a dictionary of dictionaries
# Output: the dictionary k:v object of the instructor with the longest name
# Exceptions: if there are 2 instructors with the same name length return the first one

def instructorWithLongestName (master_list):
    longest_named_instructor = dict()
    longest_name_length = 0
    for instructor in master_list:
        name_length = len(instructor['name'])
        if name_length > longest_name_length:
            longest_name_length = name_length
            longest_named_instructor = instructor
    return longest_named_instructor

instruktors = [
{'name': "Samuel", 'course': "iOS"},
{'name': "Jeremiah", 'course': "Data"},
{'name': "Ophilia", 'course': "Web"},
{'name': "Donald", 'course': "Web"},
{'name': "Domascus", 'course': "Web"}
]

print(instructorWithLongestName(instruktors))


