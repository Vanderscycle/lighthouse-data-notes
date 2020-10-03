#we will be given 2 or more numbers
# we will have to find the largest number and sum them together

# input a list with # 2<= nums < n
# #output: return the sum of the two largest numbers


def sumLargestNumbers( num_list):
    largest_num = num_list[0]
    second_largest_num = num_list[1]

    if len(num_list) == 2: # we are not checking if there are cases where the list is less than 2 numbs due to the business description
        result = largest_num + second_largest_num
        return result
    for value in num_list:
        if value > largest_num:
            second_largest_num = largest_num #otherwise we the current largest number will not be moved to the second largest num
            largest_num = value
        elif value > second_largest_num and value != largest_num:
            second_largest_num = value
        else:
            pass
    # I know that I am repeating myself, but its a simple addition which does not warrant another function
    result = largest_num + second_largest_num
    return result #Python alwasy return something be a value or None


#print(sumLargestNumbers([1, 10]))
#print(sumLargestNumbers([1, 2, 3]))
print(sumLargestNumbers([10, 4, 34, 6, 92, 2]))
#print(sumLargestNumbers([92, 82, 34, 6, 94, 93]))