list_of_nums = [1,2,3,4,5,6]
#list comprehension : mapping
squared_nums = [i**2 for i in list_of_nums]#[1,4,9,16,25,36]
print(squared_nums)
print('-'*30)

colors = ["red", "green", "blue", "yellow"]  # ===> ['R','G','B','Y']
accr = [color[0].upper() for color in colors]
print(accr)
"""
accr = []
for color in colors:
    accr.append(color[0].upper())
print(accr)
"""
print('-'*30)
#list comprehension : filtering
list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_nums = [i for i in list_of_ints if i%2 == 0]
odd_nums = [i for i in list_of_ints if i%2 != 0]
print('even',even_nums)
print('odd',odd_nums)
print("-" * 50)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#all the fruits that have a in their names [apple,banana,mango]
fruit_with_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruit_with_a)
fruit_with_a_2 = [fruit for fruit in fruits if fruit.count('a') > 0]#Christian solution
print(fruit_with_a_2)
print("-" * 50)
list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
fizzbuzz = ["fizz" if i % 3 == 0 else "buzz" for i in list_of_ints]#hint if else
print(fizzbuzz)
print("-" * 50)
nums = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
flat_nums = [x for n in nums for x in n]
print(flat_nums)
squared_nested = [x**2 for n in nums for x in n]
print(squared_nested)
list_of_sums = [sum(n) for n in nums]  # mapping
print(list_of_sums)