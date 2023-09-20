import random

for i in range(50):
  randomLetter = random.choice('ABCD')
  print(f'q{i+1},{randomLetter}')