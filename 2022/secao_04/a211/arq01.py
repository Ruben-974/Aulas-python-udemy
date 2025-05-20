class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None


    def set_user(self, user):
        self.user = user


    def set_password(self, password):
        self.password = password


    @classmethod
    def crate_with_auth(cls, user, password):
        connect = cls()
        connect.user = user
        connect.password = password
        return connect.user, connect.password


usr = Connection()
usr.set_user('John')
usr.set_password('123456')

print(usr.user, usr.password)

usr2 = Connection.crate_with_auth('Mike', '654321')
print(usr2)
