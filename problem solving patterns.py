# define the problem

#understand the problem

#break it down

#look for a pattern

#choose an approach or a strategy

#write the code

#test

#improve

#frequency counting pattern
scores = [70,80,70,90,80,70,60]

frequency = {}

for score in scores:
    if score in frequency:
        frequency[score] += 1
    else:
        frequency[score] = 1
print(frequency)

# TWO POINTERS
numbers = [1,2,3,4,5,6,7,8,9,10]

target = 10

left = 0
right = len(numbers) -1

while left < right:

    total = numbers[left] + numbers[right]

    if total == target:
        print("Found:", numbers[left], numbers[right])

        break
    elif total < target:
        left += 1

    else:
        right -= 1

#PATTERN SEARCHING

def linear_search(items, target):

    for index in range(len(items)):
        if items [index] == target:
           return index

    return -1
students = ["Bob", "Job", "Roy"]

result = linear_search(students, "Job")

print(result)
