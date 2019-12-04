def validate_6digits(code):
    return False if len(code) != 6 else True


def validate_has_double(code):
    concurrent_digit = {}

    for d in code:
        digit = int(d)
        if digit not in concurrent_digit:
            concurrent_digit[digit] = 1
        else:
            concurrent_digit[digit] = concurrent_digit[digit] + 1
    has_double = len([_ for _ in concurrent_digit.values() if _ == 2]) > 0
    return has_double


def validate_no_decreasing(code):
    previous_value = -1
    for d in code:
        digit = int(d)
        if digit < previous_value:
            return False
        previous_value = digit
    return True


def is_valid_code(code):
    code_string = str(code)
    validators = [
        validate_no_decreasing,
        validate_has_double,
        validate_6digits
    ]

    for validator in validators:
        if not validator(code_string):
            return False
    return True


def main():
    valid_code = []
    for i in range(168630, 718098 + 1):
        if is_valid_code(i):
            valid_code.append(i)
    print(len(valid_code))


if __name__ == '__main__':
    main()
