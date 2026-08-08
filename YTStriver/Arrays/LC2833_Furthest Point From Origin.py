def furthestDistanceFromOrigin(moves):                                      # Runtime: 3 ms
    return abs(moves.count('L') - moves.count('R')) + moves.count('_')

                                    #### OR ####


def furthestDistanceFromOrigin(moves):                                      # Runtime: 0 ms
    left = 0
    right = 0
    blank = 0
    for ch in moves:
        if ch == "L":
            left += 1
        elif ch == "R":
            right += 1
        else:
            blank += 1
    total = (left - right) 
    return abs(total) + blank

moves = "L_RL__R"         #Output: 3
print(furthestDistanceFromOrigin(moves))