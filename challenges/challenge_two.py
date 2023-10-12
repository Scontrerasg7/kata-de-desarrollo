from functions.input_list import get_input_list

s = 6
ss = int( str(s)*2 )

def challenge_two():
        
    input_list = get_input_list()

    squares_list = [int(x)*int(x) for x in input_list if int(x)*int(x) < ss]

