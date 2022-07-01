numbers = [1, 2, 3, 4, 5, 6]

smallest = numbers[0]
count = 0

for number in numbers:
    count += 1
    if number < smallest:
        smallest = number

print(count, smallest)
