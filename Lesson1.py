# Witbh strings we can print("Hello" + input("whats your name"))
# print("Hello " + input("whats your name "))

# changing values
a = int(input('a: '))
b = int(input("b: "))
#complicated but usefull only works on ints

a = a ^ b
b = a ^ b
a = a ^ b

print("a = " + str(a) + " b = " + str(b))


city_name = input("What is a name of the city you grew up in?\n")
pet_name = input("what is a name of the pet you grew up with?\n")
print("Your band name should be: " + city_name + " " + pet_name)