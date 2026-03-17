attendence=[1,1,0,1,0,1,1]
present=attendence.count(1)
absent=attendence.count(0)
percentage=(present/len(attendence))*100
print(present)
print(absent)
print(percentage)