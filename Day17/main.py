class User:
    # pass -When a class or function is empty
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "Sharon")
print(user_1.username)