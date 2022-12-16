import random
min = 1
max = 1000
count = 10
countt =0
num = random.randint(min, max)
while countt<count:
  n = int(input())
  if n<num:
    print("Больше!!")
    countt=countt+1
  elif n>num:
    print("МеньшЕ!!!!!!!!")
    countt = countt + 1
  else:
    print("Капец ты крутой, угадал!!!!!!!!!!")
    break
print("к0нЕц!!!!!!!!")
