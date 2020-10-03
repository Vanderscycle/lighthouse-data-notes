

# INPUT: single integer
# OUTPUT: Not really specified.

#unsure what exact format we want the multiplication table to be in.

def multiplicationTable (maxValue):
    column_size = list(range(1, maxValue + 1))
    index = 1
    line_printer = str()
    while index <= maxValue:

        for val in column_size:
            line_printer += f'{str(val*index)} '
        line_printer +='\n'
        index += 1

    return line_printer

print(multiplicationTable(10))