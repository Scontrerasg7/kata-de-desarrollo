from functions.input_list import get_input_list

def challenge_three():
    sorted_coins = get_sorted_coins_list()

    min_impossible_change = find_min_impossible_change(sorted_coins)

    print(min_impossible_change)
        
################################################################################
def get_sorted_coins_list():
    coins = get_input_list()
    coins = [int(x) for x in coins]
    return sorted(coins)

def find_min_impossible_change(sorted_coins):
    min_impossible_change = 1

    for coin in sorted_coins:
        if coin <= min_impossible_change:
            min_impossible_change += coin
        else:
            break        

    return min_impossible_change

################################################################################

if __name__ == "__main__":
    challenge_three()