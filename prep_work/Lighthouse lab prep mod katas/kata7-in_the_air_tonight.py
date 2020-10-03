import math

# INPUT: list of strings (each string representing a small air sample clean/dirty), threshold value float
# OUTPUT: Poluted/Clean

def checkAir( sample_list, threshold):
    # calculating the alarm level
    size = len(sample_list)
    alarm_threshold = math.floor(size*threshold) # we round down to ensure a greater safety margin
    failed_test = 0
    # Poluted/Clean
    for test in sample_list:
        if test == 'clean':
            pass
        elif test == 'dirty':
            failed_test += 1
        else: 
            print('unrecognized value, please ensure entries are either: clean or dirty')
            return 
    if failed_test > alarm_threshold:
        return 'Poluted'
    else:
        return 'Clean'


print(checkAir(
  ['clean', 'dirty', 'clean', 'dirty', 'clean', 'dirty', 'clean'],
  0.9
))