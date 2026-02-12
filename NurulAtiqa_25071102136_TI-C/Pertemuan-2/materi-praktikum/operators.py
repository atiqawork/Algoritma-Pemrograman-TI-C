# aritmetika
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# comparison
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#assignment
x = 5
y = 3
x += 3
y -= 2
print(x)
print(y)

# logical
x = 5
print(x < 5 or x > 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))

# identity
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(x is not y)

# membership
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("cherry" not in fruits)
text = "Hello world"
print("h" in text)
print("World" not in text)

#bitwise
print(6 & 3)

# presedence
print((6 + 3) - (6 + 3))