# 1. Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

# def countdown(num):
#     for i in range(num, -1, -1):
#         print(i)
# countdown(5)

# 2. Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

# def printReturn(list):
#     print(list[0])
#     return(list[1])
# printReturn([3, 7])

# 3. First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

# def firstPlusLength(list):
#     sum = list[0] + len(list)
#     return sum
# print(firstPlusLength([3, 5, 7, 2]))

#4. Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only element long, have the function return False

# def greaterSecond(list):
#     min = list[1]
#     newList = []
#     if len(list) > 2:
#         for i in range(len(list)):
#             if list[i] > min:
#                 newList.append(list[i])
#
#         return newList
#
#     else:
#         return False
#
# print(greaterSecond([1, 4,]))

# # 5. This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].
#
# def lengthAndValue(size, value):
#     list = []
#     for i in range(size)):
#         list.append(value)
#
#     return list
#
# print(lengthAndValue(4, 7))
