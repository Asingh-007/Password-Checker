import password_checker
import sys

if __name__ == '__main__':
    passwords = sys.argv[1:]

    for password in passwords:
        response, tail = password_checker.password_check(password)
        count = password_checker.get_password_leaks(response, tail)

        if count == 0:
            print(f"{password} has not been breached")
        else:
            print(f"{password} has been breached {count} times")
