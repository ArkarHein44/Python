# one print = one line
print("Hello, World")
print("Welcome")

# \n (new line)
print("Welcome\nMg Mg")

# \t (one tab)
print("Topic One")
print("\tTopic two")
print("\tTopic three")
print("\tTopic four")

# special escape characters ( \ )
print('I\'m from Myanmar.')

# print formatting
# 1. %s
city = "Yangon"
print("I want to go %s" % city)
# 2. %d
print("I've visited %d times to %s" % (3, city))

# {} and format()
name = "ArKar Hein"
print("I'm {},I live in {}.".format(name, city))
print("I'm {name} and {age} years old.".format(name="Apple", age=25))

# Fstring
print(f"I live in {city}")
