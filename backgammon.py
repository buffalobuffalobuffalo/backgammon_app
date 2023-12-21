import numpy as np

def create_initial_board():
    'intialize a board array with the starting positions of all checkers'
    initial_board = np.array([2, 0, 0, 0, 0, -5,
                       0, -3, 0, 0, 0, 5,
                       -5, 0, 0, 0, 3, 0,
                       5, 0, 0, 0, 0, -2])
    return initial_board

def roll():
    return np.random.randint(low=1, high=6, size=2)

def create_checkers(position):
    drawn_points = []
    for point in position[:12]:
        if point == 0:
            drawn_point = 10 * ' '
        if point >= 0:
            drawn_point = 'X' * point + (10 - point) * ' '
        if point < 0:
            drawn_point = 'O' * abs(point) + (10 + point) * ' '
        drawn_points.append(drawn_point)
    for point in position[12:]:
        if point == 0:
            drawn_point = 10 * ' '
        if point >= 0:
            drawn_point = (10 - point) * ' ' + 'X' * point 
        if point < 0:
            drawn_point = (10 + point) * ' ' + 'O' * abs(point)  
        drawn_points.append(drawn_point)
    return drawn_points

def calculate_remaining_pips(position):
    x_pips = o_pips = 0
    for i, point in enumerate(position):
        if point > 0:
            dist = 23 - i
            x_pips += point * dist
        if point < 0:
            dist = i
            o_pips += point * dist * -1
    return x_pips, o_pips
    
def draw_board(position):
    drawn_position = create_checkers(position) 
    x_pips, o_pips = calculate_remaining_pips(position)
    
    print(f'''
     |---------------------|
  12 |{drawn_position[11]}|{drawn_position[12]}|13
  11 |{drawn_position[10]}|{drawn_position[13]}|14
  10 |{drawn_position[9]}|{drawn_position[14]}|15
   9 |{drawn_position[8]}|{drawn_position[15]}|16
   8 |{drawn_position[7]}|{drawn_position[16]}|17
   7 |{drawn_position[6]}|{drawn_position[17]}|18
     |---------------------|
     |---------------------|
   6 |{drawn_position[5]}|{drawn_position[18]}|19
   5 |{drawn_position[4]}|{drawn_position[19]}|20
   4 |{drawn_position[3]}|{drawn_position[20]}|21
   3 |{drawn_position[2]}|{drawn_position[21]}|22
   2 |{drawn_position[1]}|{drawn_position[22]}|23
   1 |{drawn_position[0]}|{drawn_position[23]}|24
     |---------------------|

    X remaining pips : {x_pips}
    O remaining pips : {o_pips}
    ''')

def parse_move(move, roll):
    checks_moved = move.count('/')

    if checks_moved == 2:
        first_move = move.split(' ')[0]
        second_move = move.split(' ')[1]
        
        first_start = int(first_move.split('/')[0])
        first_end = int(first_move.split('/')[1])
        second_start = int(second_move.split('/')[0])
        second_end = int(second_move.split('/')[1])
        #check if it fits the roll
        diff1= abs(first_end - first_start)
        diff2= abs(second_end - second_start)
        if sorted(list(roll)) != sorted([diff1, diff2]):
            print('This is not a legal move because of dice')
            return
    else:
        first_start = int(move.split('/')[0])
        second_end = int(move.split('/')[1])
        diff = first_start - second_end
        first_end = second_start = first_start - roll[0]
        
        if sum(roll) != diff:
            print('This is not a legal move because of dice')
            return           
    #this will fail if you can move a piece 3 and then 5, but not 5 and then 3    
    return [first_start, first_end, second_start, second_end]

def adjust_board_for_move(position, pieces, bar=[]):
    'ensure pieces always go down in indices and up in checkers'
    if pieces not in (['x','o']):
        print('Not a legal position')
        return
        
    if pieces == 'x':
        return np.flip(position)
    if pieces == 'o':
        return position * -1
    
def update_board(move,position,pieces='x', bar=[]):
    #initialize board orientation
    adjust_board_for_move(position, pieces)

    #decrement the places you're moving from
    position[move[0]] -= 1
    position[move[2]] -= 1

    for new_pos in [move[1], move[3]]:
        # when you hit on a loose checker
        if position[new_pos] == -1:
            position[new_pos] = 1
            bar.append('o') if pieces == 'x' else bar.append('x') 
        #otherwise
        else:
            position[new_pos] += 1

    # return board orientation to original position
    adjust_board_for_move(position, pieces)

    return position
    
def move(position, roll, move, pieces='x'):
    
    move = parse_move(move,roll)
        
    #adjust values for indices
    move = [x-1 for x in move]
    position = adjust_board_for_move(position, pieces)

    #check where you have checkers and where you can move them
    legal_starts = np.where(position > 0)[0]
    open_spaces = np.where(position >= -1)[0]
    # print(f'legal starts : {legal_starts}')
    # print(set([move[1],move[3]]))
    # print(f'open spaces : {open_spaces}')
    # print(set([move[0],move[2]]))

    # confirm these match
    if (set([move[0],move[2]]).issubset(legal_starts)) & set([move[1],move[3]]).issubset(open_spaces):
        new_position = update_board(move,position,pieces)
        # return board orientation to original position
        new_position = adjust_board_for_move(new_position, pieces)
        return new_position
    else:
        print('This is not a legal move')
        return