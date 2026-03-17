ages=[10,23,45,60,34]
minor=[]
adults=[]
for i in ages:
    if i<18:
        minor.append(i)
    else:
        adults.append(i)
print(minor)
print(adults)            