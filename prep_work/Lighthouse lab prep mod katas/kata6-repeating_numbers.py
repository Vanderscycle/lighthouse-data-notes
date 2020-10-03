

# INPUT: a list of lists (each list containing 2 sets of nums) 
# [num to repeat, times to repeat]
# OUTPUT: STRING of the output separated by commas if there are more thatn 1 nested lisy

def repeatNumbers (dataset):
    aggregate = str()
    for data in dataset:
        for value in data:
            if value == data[0]:
                aggregate += str(value) * data[1]
        aggregate += ', '
    return aggregate

print(repeatNumbers([[10, 4], [34, 6], [92, 2]]))

