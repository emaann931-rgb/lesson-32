#Write a program that keeps asking the user for a password until the correct password is entered.
password="abcdef"
passkey=input("what is your password?")
while passkey!=password:
    print("wrong,try again!!!")
    passkey=input("enter password again:")
print("correct password,continue!")

'''#Write a program that allows the user only 3 login attempts using a while loop.'''

password=input("Enter password:")
keys="67"
if password==keys:
        print("Login succesful")
elif input("enter password")==keys:
        print("Login succesful")
elif input("enter password")==keys:
        print("Login succesful")
else:
        print("account locked")