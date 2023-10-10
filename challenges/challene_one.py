
s = 3

def challenge_one():
    input_str = input("Enter a list of numbers: ").strip()
    
    input_list = transform_input_str_to_list(input_str)

    cleaned_list = clean_digits_greater_than_s(input_list)

    sorted_cleaned_list = sort_list(cleaned_list)

    print(sorted_cleaned_list)

def transform_input_str_to_list(input_str):
    input_as_list = input_str[1:-1].split(", ")

    return input_as_list

def clean_digits_greater_than_s(input_list):
    greaters_than_s = build_list_of_greaters_than_s()

    cleaned_list = remove_digits_greater_than_s(input_list, greaters_than_s)

    return cleaned_list

def build_list_of_greaters_than_s():
    greaters_than_s = [ str(x) for x in range(1, 10) if x >= s ]

    return greaters_than_s

def remove_digits_greater_than_s(input_list, greaters_than_s):
    cleaned_list = []

    for number in input_list:
        clenaed_number = ''.join([dig for dig in number if dig not in greaters_than_s])

        if clenaed_number != '':
            cleaned_list.append(clenaed_number)

    return cleaned_list

def sort_list(cleaned_list):
    sorted_list = []

    return sorted_list

if __name__ == "__main__":
    challenge_one()