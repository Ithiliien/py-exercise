#Write a Python function that takes a tuple of numbers as input and returns a new tuple containing the square of each number in the original tuple.

def square_tuple(input_tuple):
    # Utilizamos una comprensión de lista para calcular el cuadrado de cada número en la tupla.
    numero_multiplo = [x**2 for x in input_tuple]
    # Convertimos la lista de cuadrados en una tupla antes de devolverla.
    return tuple(numero_multiplo)

numbers = (1, 2, 3, 4, 5)
result = square_tuple(numbers)
print(result) 
print("--------------------------")

def set_intersection(set1, set2):
  intersection = set1 & set2
  return intersection

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = set_intersection(set1, set2)
print(result)  # Output: {4, 5}
print("-----------------")

def merge_dictionaries(dict1, dict2):
  diccionario= dict1.copy()
  diccionario.update(dict2)
  return diccionario

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
result = merge_dictionaries(dict1, dict2)
print(result)  # Output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}


print("------------------")

def string_length_dictionary(strings):
    length_dict = {word: len(word) for word in strings}
    return length_dict

words = ["apple", "banana", "cherry"]
result = string_length_dictionary(words)
print(result)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}