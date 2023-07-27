DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
           }

# The below code is the one that will -
#   1. Work correctly for input - convert("one two three four".split())
#   2. Raise exception for input - convert("around two billion and four".split()) since around is not in dictionary


# def convert(s):
#     number = ''
#     for token in s:
#         number += DIGIT_MAP[token]
#         x = int(number)
#     return x
#
# print(convert("one two three four".split()))

# modifying the convert to handle exception as stated in point 2 above


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
            x = int(number)
            print(f"Conversion Suceeded! {x}")
    except KeyError:
        print(f"Conversion Failed! From KeyError")
        x = -1
    return x


print(convert("around two billion and four".split()))

# 3. if we pass a non-iterable a different error (TypeError) would be displayed

# print(convert(123))

# modifying the convert to handle the TypeError as well


def convert(s):
    """" Convert  string to an integer """
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion Suceeeded! {x}")
    except KeyError:
        print(f"Conversion Failed! From KeyError")
        x = -1
    except TypeError:
        print(f"Conversion Failed! From TypeError")
        x = -1
    return x


print(convert(512))

#  the code above has repeated statements, so we can collapse to be concise as shown below:


def convert(s):
    """" Convert  string to an integer """
    x = -1  # Moved to top from the except block
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion Suceeeded! {x}")
    except (KeyError, TypeError):  # Created a list of exceptions
        print(f"Conversion Failed!")
    return x


# we can remove the print if we are confident of error handling,
# however the except block without any statement as shown in the below code will throw an IndentationError
# This can be avoided by just keeping a pass statement which is a no op code


def convert(s):
    """" Convert  string to an integer """
    x = -1  # Moved to top from the except block
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion Suceeeded! {x}")
    except (KeyError, TypeError):  # Created a list of exceptions
        #print(f"Conversion Failed!")  # Removing this statement will cause Indentation Error
        pass   # To avoid the exception and allow a syntactically permissible blocks that are semantically empty

    return x


