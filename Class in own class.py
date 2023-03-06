class User:

    def __init__(self):
        print("new user being created...")


user_1 = User()

#Now to create an attribute for that class we can write the code as
user_1.id = "001"
user_1.username = "Irtiza"

print(user_1.username)#This will print the username
print(user_1.id)#this will print the user_id

user_2 = User()
user_2.id = "002"
user_2.name = "Ziya"

print(user_2.name)
 
 
