# def sum_all(*args):
#     print(args)
#     total = 0
#     for num in args:
#         total += num
#     return total 
# print(sum_all(5,6,9,8,7,5,6,5))    



# def fav_colors(**kwargs):
#     print(kwargs)
# fav_colors(cat="pet")  



# def special_greeting(**kwargs):
#     if "Prajwol" in kwargs and kwargs["Prajwol"] == "special":
#         return("Prajwol gets a special greeting.")
#     elif "Prajwol" in kwargs:
#         return f"{kwargs['Prajwol']} Prajwol"  
#     return "You are not recognized!"    
# print(special_greeting(whatever = "whatever",Prajwol = "special"))    
# print(special_greeting(Prajwol = "Domo"))    
# print(special_greeting(whatever = "whatever"))    


# def fav_colors(**kwargs):
#     for person, color in kwargs.items():
#         print(f"{person}'s favorite color is {color}")
# fav_colors(prajwol = "purple", someone="wassup")       