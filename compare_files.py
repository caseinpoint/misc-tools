from sys import argv


with open(argv[1]) as f1:
    file_1 = f1.readlines()

with open(argv[2]) as f2:
    file_2 = f2.readlines()

longer = max(len(file_1), len(file_2))

for i in range(longer):
    print(f'line #{i + 1}:')

    if i >= len(file_1):
        print(f'{argv[1]} past EOF')
        