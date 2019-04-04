cars = dict(lamborghini = "awesome", nissan = "sigma_male")
cars = {"car":"red", "bike":"white", 44:"fav"}
print(cars)
print(cars["lamborghini"])
print(cars["nissant"])
car = "lamborghini"
print(cars[car])





for x in cars.values():
	print(x)

print(cars.values())


for y in cars.keys():
	print(y)

print(cars.keys())	


for z in cars.items():
	print(z)

print(cars.items())

print(cars[44])
print(cars["44"])





for k,v in cars.items():
	print(f"the key is {k} and the value is {v}")
	print(k,v)
for g in cars.items():
	print(g)	

print("car" in cars)
print("red" in cars) 
print("red" in cars.values())

if "fav" in cars.values():
	print("Yes. There is your favorite.")





dictn = {"f":"g", "h":"j"}
dictn.clear()
print(dictn)




a=print(dictn.get("g"))
print(dictn.get("f"))
print(a == None)



dictn = {}.fromkeys(["apple", "banana", "orange", "Avacado"], "fruit")
print (dictn)
print({}.fromkeys(["player"], "awesome"))
print(dict.fromkeys(["player"], "awesome"))

while bikes = {"bmw": "s1000r", "ducati":"panigale", "cfmoto":"250nk", "benelli": "leoncino"}:
print(bikes.fromkeys("player", "yeah"))
print(bikes)
print(bikes.fromkeys(range(1,8), "what"))
	x = bikes.pop("cfmoto")
	print(x, bikes)
	print(bikes.popitem())
	print(bikes)




cars = {"car":"red", "bike":"white", str(44):"fav"}
balll = {key: value * 2 for key,value in cars.items()}
print(balll)
hyper_cars = {k.upper():v.upper() for k,v in cars.items()}
print(hyper_cars)
hyper_cars = {(k.upper() if k == "bike" else k):v.upper() for k,v in cars.items()}
print(hyper_cars)



nums = [1, 2, 3, 4, 5, 6]
print({num: num **3 for num in nums})
print({num:("even" if num % 2 == 0 else "odd") for num in nums})
print({num:("even" if num % 2 == 0 else "odd") for num in range(1, 20)})



st1 = "ABC"
st2 = "DEF"
for i in range(0,len(st1)):
	print(st1[i])
	for j in range(0,len(st2)):
		print(st2[j])
	print({st1[i]:st2[i]})

print({st1[i]:st2[i],st1[i]:st2[i] for i in range (0, len(st1))})
print({st1[j]:(st2[i] for i in range(0, len(st2))) for j in range (0, len(st1))}) #this line is wrong



lst1 = ['A', 'B', 'C']
lst2 = [1, 2, 3]
str1 = ''
for e, f in zip(lst1, lst2):
   str1 = str1 + e + str(f)
print(str1)


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
# print((zip(list1,list2)))
print(dict(zip(list1,list2)))