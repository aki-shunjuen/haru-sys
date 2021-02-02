
from os import sep


print("good morning")

x = 5
if x > 8:
    print("ok")
else:
    print("No")

for y in range(x):
    for i in range(3):
        print(y,i,sep="-")
        if y ==3:
            break
print(y)


z = x + y
print(z)
