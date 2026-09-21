numbers_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, numbers_input.split()))

numbers.sort()
second_largest = numbers[-2]

print("The second largest number is:", second_largest)