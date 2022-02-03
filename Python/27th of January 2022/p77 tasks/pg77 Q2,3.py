import lib

password_file = "Q2,3 psswd.txt"
password = lib.fr(password_file)
user_password = input("What is the password: ")
if user_password == password:
    print("Correct")
print(password)