def get_input_list():
    """Removes the square brackets snd splits the string by comma and space."""
    
    input_str = input("Enter a list of numbers: ").strip()

    input_as_list = input_str[1:-1].split(", ")

    return input_as_list