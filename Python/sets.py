sets = {1,2,3,3,4,5}
print(sets)
lst = [1,2,3,3,4,5]
settings = set(lst)
print(settings)

print(list(settings))
print(len(set(lst)))

math_students = {"Prajwol", "Prashant", "Nischal"}
biology_students = {"Ganesh", "Prasansha", "Prashant"}
print(math_students | biology_students)
print(math_students & biology_students)