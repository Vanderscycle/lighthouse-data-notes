# sum a certain numbs in a list if they match a specific condition

# Input: list of num, condition("even\odd")
# output: sum
# exception: 0 if no number match the condition


def conditionalSum (num_list, cond):
    result = 0 
    for value in num_list:
        if cond == "even" and (value % 2 == 0):
            result += value
        elif cond == 'odd' and (value % 2 != 0):
            result += value
        else:
            pass
    return result


