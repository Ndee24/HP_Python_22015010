#python program to display name,age and mobile phone number

name=input("what is your full name\t")

age=int(input("how old are you?\t"))

#your age should be only in numeric form,e.g 10

phone=int(input("Your phone number\t"))

print("Hello {}, you are {} years old with the mobile phone number ({})".format(name,age,phone))
