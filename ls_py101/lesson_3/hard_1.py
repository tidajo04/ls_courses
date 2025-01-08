# question4
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) in range(1, 5):
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True