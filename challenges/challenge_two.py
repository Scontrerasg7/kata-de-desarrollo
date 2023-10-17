from functions.input_list import get_input_list
import random

S = 3
SS = int( str(S)*2 )

def challenge_two():        
    input_list = get_input_list()

    squares_list = [int(x)*int(x) for x in input_list if int(x)*int(x) <= SS]

    print(quicksort(squares_list))

################################################################################

def quicksort(list_to_sort):
    n = len(list_to_sort)

    if n < 2:
        return list_to_sort
    
    pivot, less, greater = randomize_partition(list_to_sort)

    return quicksort(less) + [pivot] + quicksort(greater)

def randomize_partition(list_to_sort):
    n = len(list_to_sort)

    pivot_index = random.randint(0, n-1)
    pivot = list_to_sort[pivot_index]

    indexes_of_interest = [i for i in range(n) if i != pivot_index]

    less = [list_to_sort[i] for i in indexes_of_interest if list_to_sort[i] <= pivot]
    greater = [list_to_sort[i] for i in indexes_of_interest if list_to_sort[i] > pivot]

    return pivot, less, greater

################################################################################
if __name__ == "__main__":
    challenge_two()