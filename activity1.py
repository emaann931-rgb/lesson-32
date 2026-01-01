#Write a program that keeps asking the user for a password until the correct password is entered.
password="abcdef"
passkey=input("what is your password?")
while passkey!=password:
    print("wrong,try again!!!")
    passkey=input("enter password again:")
print("correct password,continue!")

