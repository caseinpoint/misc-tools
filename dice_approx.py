from sys import argv
from random import randint

# get dice from argv, format: 2d6
num_dice, num_sides = argv[1].split('d')
num_dice = int(num_dice)
num_sides = int(num_sides)

results = {}

print(f'Simulating 1,000,000 rolls of {argv[1]}...')
for _ in range(1_000_000):
    roll_total = 0
    for _ in range(num_dice):
        roll_total += randint(1, num_sides)

    results[roll_total] = results.get(roll_total, 0) + 1

print('TOTAL - # ROLLS - PERCENT')
for roll in sorted(results.keys()):
    num_rolls = results[roll]
    ratio = num_rolls / 1_000_000
    print(f'{roll:<5} - {num_rolls:<7} - {ratio:<6.3%}')
