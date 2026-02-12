def my_function():
  print("Hello from a function")
my_function()

def my_functions(name):
  print("Hello ", name)
my_functions("atiqa")

# lambda => digunakan sekali
x = lambda a : a + 10
print(x(5))

# rekursi function => fungsi yang manggil dirinya sendiri
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)
print(factorial(5))