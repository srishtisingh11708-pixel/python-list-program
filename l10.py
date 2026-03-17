marks=[78,35,90,40,55]
count=0
total=0
for i in marks:
    if i>=40:
        print(i,"-pass")
        count+=1
        total+=i
    else:
        print(i,"fail")

print("number of pass student",count) 
avg=total/count
print(avg)           