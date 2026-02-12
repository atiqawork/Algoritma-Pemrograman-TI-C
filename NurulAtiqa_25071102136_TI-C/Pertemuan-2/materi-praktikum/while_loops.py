i = 1
while i < 6:
  print(i)
  i += 1 # print i dari 1 sampai 6

# break = berhenti
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 # print i dari 1 sampei 3 (break nya)

# continue = loncat
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # print i dari 1 sampai sebelum 6 dengan loncatin 3