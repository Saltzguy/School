
top  = " --- "
side = "|    |"

def get_size():
    length = int(input("What is the length of the board -> "))
    width = int(input("What is the width of the board ->"))
    return [length, width]

def print_board(lst):
    top_board = ""
    side_board = ""
    for x in range(lst[1]):
        top_board = top +" " + top_board
        side_board = side + side_board
    for x in range(lst[0]):
        print(top_board)
        print(side_board)
        print(top_board)
print_board(get_size())
