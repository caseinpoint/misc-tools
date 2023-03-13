from sys import argv


def calculate_rolls(num_dice=2, num_sides=6, results={}, current_res=0):
    if num_dice < 1:
        results[current_res] = results.get(current_res, 0) + 1
        return results

    for s in range(1, num_sides + 1):
        calculate_rolls(num_dice - 1, num_sides, results, current_res + s)

    return results


# get dice from argv, format: 2d6
num_dice, num_sides = argv[1].split('d')
num_dice = int(num_dice)
num_sides = int(num_sides)
total_rolls = num_sides ** num_dice

results = calculate_rolls(num_dice, num_sides)

print('TOTAL | # COMBOS | PERCENT')
for roll in sorted(results.keys()):
    num_rolls = results[roll]
    ratio = num_rolls / total_rolls
    print(f'{roll:<5} | {num_rolls:<8} | {ratio:<6.3%}')
