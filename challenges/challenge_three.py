from functions.input_list import get_input_list

def challenge_three():
    sorted_coins = get_sorted_coins_list()

    possible_change_list = build_possible_change_list(sorted_coins)

    min_impossible_change = get_min_int_out_of_list(possible_change_list)

    print(min_impossible_change)
        

################################################################################
def get_sorted_coins_list():
    coins = get_input_list()
    coins = [int(x) for x in coins]
    return coins.sort()

def build_possible_change_list(sorted_coins):
    possible_change_list = []

    return possible_change_list        

def append_change_to_possible_change(possible_change_list, change):
    if change not in possible_change_list:
        possible_change_list.append(change)

    return possible_change_list

def get_min_int_out_of_list(sorted_list):
    min_int = 1

    while min_int in sorted_list:
        min_int += 1

    return min_int
    
################################################################################


if __name__ == "__main__":
    challenge_three()


# [5, 7, 1, 1, 2, 3, 22]
# [1, 1, 1, 1, 1]
# [1, 5, 1, 1, 1, 10, 15, 20 ,100]
# [1, 2, 4]