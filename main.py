import math
import string
import sys

password_user = str(input("Your password:\n"))


def calculate_entropy(password: str) -> float:
    has_digits = any(x in string.digits for x in password)
    has_ascii_lowercase = any(x in string.ascii_lowercase for x in password)
    has_ascii_uppercase = any(x in string.ascii_uppercase for x in password)
    has_punctuation = any(x in string.punctuation for x in password)
    pool_size = 0
    if has_digits:
        print('has_digits')
        pool_size += len(string.digits)
    if has_ascii_lowercase:
        print('has_ascii_lowercase')
        pool_size += len(string.ascii_lowercase)
    if has_ascii_uppercase:
        print('has_ascii_uppercase')
        pool_size += len(string.ascii_uppercase)
    if has_punctuation:
        print('has_punctuation')
        pool_size += len(string.punctuation)

    password_len = len(password)
    pool_size_log = math.log2(pool_size)
    result = password_len * pool_size_log

    print("Password len is", password_len)
    print("Pool size is", pool_size)
    print("Log is", pool_size_log)
    print(f"Result is {password_len} * {pool_size_log} = {result}")
    return result


# print(calculate_entropy(password_user))


def result(res: float) -> str:
    global printed_result
    if res <= 25:
        printed_result = "Your password is poor"
    elif 25 < res <= 50:
        printed_result = "Your password is week"
    elif 50 < res <= 75:
        printed_result = "Your password is reasonable"
    elif 75 < res <= 100:
        printed_result = "Your password is good"
    elif res > 100:
        printed_result = "Your password is excellent"
    return printed_result


result(calculate_entropy(password_user))

if __name__ == "__main__":
    pw = sys.argv[1]
    print(calculate_entropy(pw))
