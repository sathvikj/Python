import random
P = input("Enter the length of your password: ")
l = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
Strong_Password = "".join(random.sample(l,P))
print(strong_Password)

