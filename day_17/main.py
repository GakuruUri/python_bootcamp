class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # This is a default value for number of followers.


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

print(user_1.followers)

# Methods are the things that the object does.








# # You can use your class to create an object.
# user_1 = User()
#
# # Creating an attribute for our class
# user_1.id = "001"
# user_1.username = "angela"
#
# print(user_1.username)
#
# # Constructors are part of our blueprint, initializing, init.
#
# # Attributes are the things the object will have. These are variables associated with the final object.
