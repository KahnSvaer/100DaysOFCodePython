import requests


class Customer:
    def __init__(self, sheety_endpoint_user: str, sheety_header: dict):
        self.sheety_header = sheety_header
        self.sheety_endpoint = sheety_endpoint_user

    def _user_creation(self):
        print("Welcome to Shivansh's flight club")
        print("We find the best flight deals and email them to you.")
        fname = input("What is you name?\n").lower()
        lname = input("What is your last name?\n").lower()
        email = input("What is your email?\n").lower()
        email_confirmation = input("Type your email again.\n").lower()
        if email == email_confirmation:
            print("You are in the club!")
            return {"firstName": fname, "lastName": lname, "email": email}
        else:
            print("Your email is not matching\n\n")
            return self._user_creation()

    def sheety_fill_user(self):
        user_data = {"user": self._user_creation()}
        try:
            response = requests.post(url=self.sheety_endpoint, headers=self.sheety_header, json=user_data)
            response.raise_for_status()
        except requests.HTTPError:
            print("User Creation Failed")

    def get_emails(self):
        try:
            response = requests.get(url=self.sheety_endpoint, headers=self.sheety_header)
            response.raise_for_status()
        except requests.HTTPError:
            print("Error in opening email")
            return []
        else:
            records = response.json().get("users")
            return [user_record.get("email") for user_record in records]
