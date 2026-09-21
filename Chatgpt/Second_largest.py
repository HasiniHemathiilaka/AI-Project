# Program to find the second-largest number

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

numbers.sort()

second_largest = numbers[-2]

print("Second-largest number:", second_largest)
