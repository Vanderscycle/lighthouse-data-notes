

# INPUT: parking grid, type of vehicle
# OUTPUT: returns the coordinates [x/columns,Y/rows] of an available parking sport/ false if none avail 

# Regular cars R
# Smol cars R/S
# Motorcycle R/S/M

# Grid: UPPERCASE = AVAILABLE / lowercase = unavailable
# list of lists (use nested loops)

#NOTE1: in your example you return 'false' when there are no parking spot available. My function returns the boolean value False.
#NOTE2: this function may enrage car drivers as it doesn't try to match the vehicle to its 'designed' parking spot and instead, do as the problem asked, only look for the first available spot.
def whereCanIPark(grid,vehicle):
    # determining what vehicle is being driven
    if vehicle == 'regular':
        parking_code = ['R']
    elif vehicle == 'small':
        parking_code = ['R','S']
    elif vehicle == 'motorcycle':
        parking_code = ['R','S','M']
    else:
        print('This is not a valid transportation method')
        return False
    # determining availability of parking sport
    for row in grid:
        for column in row:
            if column in parking_code:
                return [row.index(column),grid.index(row)]
    else: # no parking sport
        return False



print(whereCanIPark(
  [
    # 0    1    2    3    4    5
    ['s', 's', 's', 's', 's', 's'], # 0
    ['s', 'm', 's', 'S', 'r', 's'], # 1
    ['s', 'm', 's', 'S', 'r', 's'], # 2
    ['S', 'r', 's', 'm', 'r', 's'], # 3
    ['S', 'r', 's', 'm', 'R', 's'], # 4
    ['S', 'r', 'S', 'M', 'm', 'S']  # 5
  ],
  'motorcycle'
))