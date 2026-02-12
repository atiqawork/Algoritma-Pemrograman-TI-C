fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # jika bentuknya list, tuple atau lain yang banyak data nya, yang di-breakdown isi masing masing

for x in "banana":
  print(x) # jika bentuknya string, yang di-breakdown per char nya

for x in range(6, 10, 2): # 6, 10, 2 masing masing start, stop, dan set
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")