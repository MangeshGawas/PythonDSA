# Day lambda function
#sytax
# lambda argument: expression

#simple addition example
add = lambda x, y : x+y
print(add(12,3))

#map function 
numbers = [1,2,3,4,5,6]
squared = map(lambda x: x**2, numbers)
print(list(squared))

#filters
even_number = filter(lambda x: x%2==0, numbers)
print(list(even_number))

#sorted
fruits = ["apple","mango", "grapes", "date"]
sorted_fruits = sorted(fruits, key= lambda x : len(x))
print(sorted_fruits)