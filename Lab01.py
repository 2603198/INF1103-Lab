print("Hello world")

username = "LZQ"
bio = "test"
followers = 100

followers += 50
print("Day 1:" , followers)

followers += 20
print("Day 2:", followers)

followers -= 10
print("Day 3:", followers)

username = input("Enter username:")
age = int(input("Enter age:"))
category = input("Enter content category:")

print("\nInstagram Profile")
print("===================")
print("username:", username)
print("Age:", age)
print("Category", category)

if age > 40 and category == "fun":
    print("You are old what is fun for you")

