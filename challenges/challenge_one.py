from functions.input_list import get_input_list

s = 3

def challenge_one():
    
    input_list = get_input_list()

    cleaned_list = clean_digits_greater_than_s(input_list)

    switched_cleaned_list = switch_list(cleaned_list)

    print(switched_cleaned_list)

################################################################################

def clean_digits_greater_than_s(input_list):
    greaters_eqs_than_s = build_list_of_greaters_eqs_than_s()

    cleaned_list = remove_digits_greater_than_s(input_list, greaters_eqs_than_s)

    return cleaned_list

def build_list_of_greaters_eqs_than_s():
    greaters_eqs_than_s = [ str(x) for x in range(1, 10) if x >= s ]

    return greaters_eqs_than_s

def remove_digits_greater_than_s(input_list, greaters_eqs_than_s):
    cleaned_list = []

    for number in input_list:
        clenaed_number =  ''.join([dig for dig in number if dig not in greaters_eqs_than_s]) 

        if clenaed_number != '':
            cleaned_list.append(int(clenaed_number))

    return cleaned_list

def switch_list(list_to_switch):
    """Since negative indexes can't be used in some languages, 
    using list[::-1] is kind of built-in in Python,
    so this function reverse a list using a for loop
    """
    n = len(list_to_switch)

    for i in range(n//2):
        list_to_switch[i], list_to_switch[n-i-1] = list_to_switch[n-i-1], list_to_switch[i]

    return list_to_switch

################################################################################

if __name__ == "__main__":
    challenge_one()