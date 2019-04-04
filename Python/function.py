# def say_hi():
#     print("Hi!!!")
# say_hi()    
# print(say_hi())    


# def no_print():
#     "You won!!"
# print(no_print())


# def say_hi_return():
#     return "Hi!!!"
#     print("Hi again.")
# greeting = say_hi_return()
# print(greeting)

# def say_hi_return():
#     return "Hi!!!"
#     return ("Hi again.")
# greeting = say_hi_return()
# print(greeting)



# from random import random
# def coin_flip():
#     if random() > 0.5:
#         print("Heads")
#     else:
#         print("Tails")
# coin_flip()
# print(coin_flip())  
# for x in range(1, 4):
#     coin_flip()        

# import random
# def coin_flip():
#     if random.randint(-1, 1) > 0:
#         print("Heads")
#     else:
#         print("Tails")      
# for x in range(1, 6):
#     coin_flip() 



# def sq_number(x):
#     return x**2
# print(sq_number(10))
# print(sq_number(8.565))    

# def add(x, y):
#     return x*x + 2*x*y + y*y
# print(add(5, 6))    
# print(x)



# def your_name(first_name, last_name):
#     return (f"Your name is {first_name} {last_name}.")
# print(your_name("P","J"))
# print(your_name(4, 5))


# returns 9
# def sum_odd(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#     return total
# print(sum_odd([1, 2, 3, 4, 5]))
# print(total)  #total scoped within the function

# returns 1 (mistake)
# def sum_odd(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#     return total
# print(sum_odd([1, 2, 3, 4, 5])) 




# Default parameters
# def exponent(nums, power):
#     return nums ** power
# print(exponent(3, 6))    
# print(exponent(3))    
# print(exponent(9))  




# def add(a, b):
#     return a+b
# def math(a, b, fn = add):
#     return fn(a, b)
# def subtract(a, b):
#     return a - b
# print(math(2, 3))
# print(math(2, 3, subtract))    




# # EXAMPLE OF A SCOPING PROBLEM:
# total = 0
# def increment():
# 	total += 1
# 	return total
# print(increment()) # Error! 
# # "I can't find a variable named total in this function"





# total = 0
# def increment():
# 	global total #use the global variable total
# 	total += 1
# 	return total
# print(increment()) # 1
# print(increment()) # 2
# print(increment()) # 3




# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner()   
# print(outer()) 




# def exponent(num, power=2):
# 	"""exponent(num, power)raises num to specified power. Power defaults to 2."""
# 	return num ** power
# print(exponent(2,3)) #8
# print(exponent(3)) #9
# print(exponent(7)) #49
# print(exponent.__doc__)




# def return_day(num):
#     days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
#     # Check to see if num valid
#     if num > 0 and num < len(days):
#         # use num - 1 because lists start at 0 
#         return days[num-1]
#     return None
# print(return_day(0))    


# def return_day(num):
#     try:
#         return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
#     except IndexError as e:
#         return None
# print(return_day(8))


# def list_(j):
#     if  j:
#         return j[-1]
#     return None
# # m = [123,2356,54987987987987987987987]
# print(list_([123,2356,54987987987987987987987]))     




# def count_letters(word, letter):
#     return word.lower().count(letter.lower())
# print(count_letters("banana", "a"))    


# def create_dict(sttr):
#     return {l: sttr.count(l) for l in sttr}
# print(create_dict("banana"))    




# def list_manipulation(collection, command, location, value=None):
#     if(command == "remove" and location == "end"):
#         return collection.pop()
#     elif(command == "remove" and location == "beginning"):
#         return collection.pop(0)
#     elif(command == "add" and location == "beginning"):
#         collection.insert(0,value)
#         return collection
#     elif(command == "add" and location == "end"):
#         collection.append(value)
#         return collection
# print(list_manipulation([1, 6, "wassup", None], "add", "beginning"))        



# string = "banana"
# print(string[:1:-2])

# def is_palindrome(string):
#     return string == string[::-1]
# print(is_palindrome("asasa"))    


# def capitalize(string):
#     return string[:1].upper() + string[1:]
# print(capitalize("banana")) 




# def intersection(l1, l2):
#     intersect = []
#     for val in l1:
#         if val in l2:
#             intersect.append(val)
#     return intersect        
# print(intersection([1,2,3,4,5, 6], [5,6,7,8,9]))    



# def intersectn(x, y):
#     return [val for val in set(y) if val in set(x)]
# print(intersectn([1,2,3,4,5,5,6], [5,5, 6,7,8,9]))