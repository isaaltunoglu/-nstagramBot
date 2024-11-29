import json
import os

class InteractionInfo:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    def sign_in(self):
        print("Please enter your username and password")
        self.username = input("Username: ")
        self.password = input("Password: ")
        # Dosya yolunu kontrol edip oluşturuyoruz
        file_path = "accountinfo.json"
        with open(file_path, "w") as file:
            json.dump({"username": self.username, "password": self.password}, file, indent=4)
        print(f"Data saved to {file_path}")
    def load_account_info(self):
        # Dosya yolunu kontrol edip açıyoruz
        file_path = "accountinfo.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                account_info = json.load(file)
                self.username = account_info["username"]
                self.password = account_info["password"]
        else:
            print("Account information file not found.")



if __name__ == "__main__":
    print("This is the module.py file.")

