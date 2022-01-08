# [order of n] O(n) = LINEAR
def get_sqr_numbers(numbers):
    steps = 1
    sqr_list = []
    for n in numbers:
        print("Steps: ", steps)
        steps += 1
        result = n*n
        sqr_list.append(result)
    return sqr_list

# print(get_sqr_numbers([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]))

# [order of squared n] O(n^2) = QUADRANIC
def find_duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return "am gasit un duplicat"

# print(find_duplicate([1,2,3,4,5,6,6,7,8,9,10]))

# [order of one] O(1) = CONSTANT
def return_element_by_index(numbers, index):
    return numbers[index]

print(return_element_by_index([1,2,3,4,5,6,6,7,8,9,10], 1))