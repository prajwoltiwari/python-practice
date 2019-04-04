months = ("January", "February", "March", "April", "May")
for month in months:
    print(month)
i = len(months) - 1
while i >= 0:
    print(months[i])
    i -= 1
print(months.count("January"))


tupl = (1,2,3,3,3,4,(5,5,7),6)
print(tupl[6])
print(tupl[6][1])
print(tupl.count(5))


print(months[:3:2])
