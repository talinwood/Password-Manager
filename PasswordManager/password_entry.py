class PasswordEntry:

    def __init__(self, username, password, website):
        self.username = username
        self.password = password
        self.website = website

    def get_website(self):
        return self.website
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password