# def a():
#     return 5
# print(a())

# # Prediction: 5
# # Actual: 5

# def a():
#     return 5
# print(a()+a())

# # Prediction: 10
# # Actual: 10

# def a():
#     return 5
#     return 10
# print(a())

# # Prediction: 5
# # Actual: 5

# def a():
#     return 5
#     print(10)
# print(a())

# # Prediction: 5
# # Actual: 5

# def a():
#     print(5)
# x = a()
# print(x)

# # Prediction:
# 5
# undefined
# # Actual:
# 5
# None

# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# # Prediction:
# 3
# 5
# 8
# # Actual:
# 3
# 5
# None

# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# # Prediction: 25
# # Actual: 25

# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a)

# # Prediction: a
# # Actual: 0x100463400

# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# # Prediction:
# 7
# 14
# 21
# # Actual:
# 7
# 14
# 21

# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# # Prediction: 8
# # Actual: 8

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# # Prediction:
# 500
# 500
# 500
# # Actual:
# 500
# 500
# 300
# 500

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# # Prediction: 
# 500
# 500
# 300
# 300
# # Actual:

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# # Prediction:
# 500
# 500
# 300
# 300
# # Actual:
# 500
# 500
# 300
# 300

# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

# # Prediction:
# 1
# 3
# 2
# # Actual:
# 1
# 3
# 2

# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

# # Prediction:
# 1
# 3
# 5
# 10
# # Actual:
# 1
# 3
# 5
# 10
