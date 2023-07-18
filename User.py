""" User.py """
import file

class User:
    
    FILE_NAME = 'data/users.json'

    first_name: str
    last_name: str
    username: str
    password: str
    email: str

    def __init__(self, first_name: str, last_name: str, username: str, password:str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        
    def save(self):
        file.create_or_update(self.FILE_NAME, self.__dict__)

test = User('Enrique', 'Avalos','eavalos','123', 'avalosenator@gmail.com')
test.save()

