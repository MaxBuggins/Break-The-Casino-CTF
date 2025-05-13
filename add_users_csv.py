#! python
import requests
import sys
from csv import DictReader


def main():
    
    try:
        url = str(sys.argv[1])
        token = str(sys.argv[2])
        csvLocation = str(sys.argv[3])

    except IndexError:
        print("Usage: python3 add_user.py <url> <admin_token> <csv path>")
        sys.exit(1)

    # Create API Session
    url = url.rstrip("/")
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {token}"})

    # See users.csv example template at https://docs.ctfd.io/docs/imports/csv#users
    users = DictReader(open(csvLocation))

    for user in users:
        # Note that the notify parameter is being passed here so CTFd will send the 
        # user an email with their credentials after the account is created if mail server settings are configured.
        r = s.post(
            f"{url}/api/v1/users?notify=true",
            json={
                "name": user["name"],
                "email": user["email"],
                "password": user["password"],
                "type": "user",
                "verified": True,
                "hidden": False,
                "banned": False,
                "fields": [],
            },
            headers={"Content-Type": "application/json"},
        )

        print("Status:", r.status_code)
    
        try:
            print("Response:", r.json())
        except requests.exceptions.JSONDecodeError:
            print("Raw Response:", r.text)



if __name__ == "__main__":
    main()
