class PasswordEntry:

    def __init__(self, username, password, website):
        self.username = username
        self.password = password
        self.website = website

    #Getters
    def get_website(self):
        return self.website
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    #Setters
    def set_website(self, website):
        self.website = website

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    #Convert entry into a dictionary for easy storage
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "website": self.website
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["password"], data["website"])
    