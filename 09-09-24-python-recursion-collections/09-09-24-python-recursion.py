list_of_nums = [1, 2, 3, 4, 5, 6, 8, 4, 1, 2, 3, 6, 9, 4]


# do not use sum() or loops here
def sum_l(lst):
    # break case : the function won't call itself again
    if len(lst) == 0:  # or if not lst
        return 0
    else:
        return lst[0] + sum_l(lst[1:])


"""
[1, 2, 3, 4, 5, 6, 8, 4, 1, 2, 3, 6, 9, 4]
1+[2, 3, 4, 5, 6, 8, 4, 1, 2, 3, 6, 9, 4]
1+2+[3, 4, 5, 6, 8, 4, 1, 2, 3, 6, 9, 4]
[4, 5, 6, 8, 4, 1, 2, 3, 6, 9, 4]
[5, 6, 8, 4, 1, 2, 3, 6, 9, 4]
[6, 8, 4, 1, 2, 3, 6, 9, 4]
[8, 4, 1, 2, 3, 6, 9, 4]
[4, 1, 2, 3, 6, 9, 4]
[1, 2, 3, 6, 9, 4]
[2, 3, 6, 9, 4]
[3, 6, 9, 4]
[6, 9, 4]
[9, 4]
[4]
[]
58"""
result = print(sum_l(list_of_nums))
print(sum_l([]))
print("-" * 50)


def factorial(n):
    # n*(n-1)*(n-2)*.....*1
    # 5! = 120
    # 0! = 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(6))
print("-" * 50)


def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 1,1,2,3,5,8,13,21
print(fibonacci(9))
print("-" * 50)


def is_palindrome(string):
    # level
    # racecar
    # bob
    # return string == string[::-1]
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False


print("racecar", is_palindrome("racecar"))
print("level", is_palindrome("level"))
print("pythop", is_palindrome("pythop"))
print("-" * 50)
country_list = ["USA", "Canada", "Germany", "France", "Australia", "India"]
target_country = "India"


def search_country(list_of_countires, target):
    if not list_of_countires:
        return "country not found"
    if list_of_countires[0] == target:
        return f"{target} found"
    else:
        return search_country(list_of_countires[1:], target)


print(search_country(country_list, target_country))
print(search_country(country_list, target="Tunisia"))
print(search_country(country_list, "Brasil"))
print(search_country(country_list, target="USA"))
