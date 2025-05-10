numbers = [5, 7, 9, 12, 15, 18]

for index, number in enumerate(numbers):
    if number % 2 == 0:
        print(f"First even number is {number} at index {index}")
        break
