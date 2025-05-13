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
    with open(csvLocation, newline='') as csvfile:
        users = DictReader(csvfile)

        for index, user in enumerate(users, start=1):
            user_id = user.get("id")

            if not user_id:
            
                print(f"[Row {index}] Skipped: 'id' field is missing or empty.")
            
                continue

            try:
                int(user_id)  # Validate it's a number
            except ValueError:
            
                print(f"[Row {index}] Skipped: 'id' is not a valid number → {user_id}")
            
                continue

            delete_url = f"{url}/api/v1/users/{user_id}"
            r = s.delete(delete_url, json="")

            print(f"[Row {index}] Deleting user ID {user_id} - Status: {r.status_code}")
        
            try:
            
                print("Response:", r.json())

            except requests.exceptions.JSONDecodeError:
            
                print("Raw Response:", r.text)



if __name__ == "__main__":
    main()
