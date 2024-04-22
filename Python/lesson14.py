# рекурсия это функция которая вызывает саму себя

"""
Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке, разделяя  
их пробелами или новыми строками. При решении этой задачи нельзя использовать строки,  
списки, массивы (ну и циклы, разумеется). Разрешена только рекурсия и целочисленная  
арифметика.
"""


def factorial(n: int) -> int:
    """функция вычисляет факториал"""
    if n == 0:
        return 1
    return f"{4}*{factorial(n-1)}" 

print(factorial(5))

#    5*4*3*2*1

# n = 5
# Fn = n*(n-1)
# 5! = 5*4
# 0! = 1
# 1! = 1
