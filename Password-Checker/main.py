import password_checker
import sys

if __name__ == '__main__':
    # Checks if any arguments have been given through Command Line / Terminal
    sys_passwords = sys.argv[1:]

    # If there are no sys arguments, check Passwords.txt
    if len(sys_passwords) == 0:
        with open("Passwords.txt", "r") as file:
            passwords = file.read().splitlines()

            if len(passwords) == 0:
                print("No passwords given through command line or file")
    else:
        passwords = sys_passwords

for password in passwords:
    response, tail = password_checker.password_check(password)
    count = password_checker.get_password_leaks(response, tail)

    if count == 0:
        print(f"{password} has not been breached")
    else:
        print(f"{password} has been breached {count} times")
