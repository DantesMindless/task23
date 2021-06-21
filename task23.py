
def power(x, y):
    if y == 0:
        return 1

    if y >= 1:
        return x * power(x, y - 1)


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    if looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1])
    return False

def mult(x, y):
    if y == 0:
        return y

    if y == 1:
        return x
    else:
        return x + mult(x, y - 1)
def reverse(input_str: str) -> str:
    if len(input_str) <= 1:
        return input_str
    else:
        return reverse(input_str[1:]) + input_str[0]

def sum_of_digits(digit_string: str) -> int:
    if digit_string == 0:
        return 0
    return (digit_string%10) + sum_of_digits(digit_string//10)
print(power(10,5))
print(is_palindrome('catac'))
print(mult(4,5))
print(reverse('roro'))
print(sum_of_digits(567))