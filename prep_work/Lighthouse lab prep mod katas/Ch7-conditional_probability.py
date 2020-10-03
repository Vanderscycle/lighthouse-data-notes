import numpy as np

# how many times we run the simulation
n_runs = 100000

# initialize variables
SAM = 0
SAM_YES = 0
SAM_NO = 0
ALEX = 0
ALEX_YES = 0
ALEX_NO = 0
YES = 0
NO = 0

# process simulation
for _ in range(n_runs):
    # Sam (probability of Sam being the coach)
    if np.random.random() < 0.6: # 60%
        SAM += 1

        # YES
        if np.random.random() < 0.5:
            SAM_YES += 1
            YES +=1

        # NO
        else:
            SAM_NO += 1
            NO += 1

    #Alex (probability of Alex being the coach)
    else: #40%
        ALEX += 1

        # YES
        if np.random.random() < 0.3:
            ALEX_YES += 1
            YES += 1

        # NO
        else:
            ALEX_NO += 1
            NO +=1

            # create probabilities
P_SAM = SAM / n_runs * 100
P_SAM_YES = SAM_YES / n_runs * 100
P_SAM_NO = SAM_NO / n_runs * 100
P_ALEX = ALEX / n_runs * 100
P_ALEX_YES = ALEX_YES / n_runs * 100
P_ALEX_NO = ALEX_NO / n_runs * 100
P_YES = YES / n_runs * 100
P_NO = NO / n_runs * 100

print(f'Sam is the coach: {P_SAM}%')
print(f'Sam is the coach and you are the goalkeeper: {P_SAM_YES}%')
print(f'Sam is the coach and you are not the goalkeeper: {P_SAM_NO}%')
print(f'Alex is the coach: {P_ALEX}%')
print(f'Alex is the coach and you are the goalkeeper: {P_ALEX_YES}%')
print(f'Alex is the coach and you are not the goalkeeper: {P_ALEX_NO}%')
print(f'You are the goalkeeper: {P_YES}%')
print(f'You are not the goalkeeper: {P_NO}')

# P(Sam | goalkeeper)
P_SAM_GOAL = P_SAM_YES / P_YES
print(P_SAM_GOAL)