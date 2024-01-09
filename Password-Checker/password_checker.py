import requests
import hashlib


def request_api(query):
    url = "https://api.pwnedpasswords.com/range/" + query
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Request to {url} failed. Status code: {response.status_code}')

    return response


def password_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    query, tail = sha1password[:5], sha1password[5:]
    response = request_api(query)
    return response, tail


def get_password_leaks(hashes, hash_of_interest):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_of_interest:
            return int(count)
    return 0
