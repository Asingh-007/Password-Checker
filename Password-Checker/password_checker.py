import requests
import hashlib


# Requests Pwned Password Information
def request_api(query):
    _url = "https://api.pwnedpasswords.com/range/" + query
    response = requests.get(_url)

    # Breaks if API call fails
    if response.status_code != 200:
        raise RuntimeError(f'Request to {_url} failed. Status code: {response.status_code}')

    return response


def password_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Takes only first 5 characters as API uses k anonymity
    query, tail = sha1password[:5], sha1password[5:]
    response = request_api(query)
    return response, tail


def get_password_leaks(hashes, hash_of_interest):
    # Creates List from each line in response
    hashes = (line.split(':') for line in hashes.text.splitlines())

    for h, count in hashes:
        if h == hash_of_interest:
            return int(count)
    return 0
