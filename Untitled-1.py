class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, password):
        self.passwords[website] = password
        print("Password added successfully")

    def get_password(self, website):
        if website in self.passwords:
            print("Password:", self.passwords[website])
        else:
            print("Website not found")

    def show_all(self):
        for site in self.passwords:
            print(site)

pm = PasswordManager()

pm.add_password("gmail", "12345")
pm.add_password("facebook", "abc123")

pm.show_all()
pm.get_password("gmail")