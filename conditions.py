## if-else syntax in python
# if condition:
#  statement 1

i = 10
if (i > 15):
    print("i is less than 15")
else:
    print(" i is greater than 15")

if i > 15:
    print("i is 15")


## nested loops in python
## FOR LOOP

x = [1, 2]
y = [4, 5]

for i in x:
    for j in y:
        print(i, j)

## WHILE LOOP

x = [1, 2]
y = [4, 5]

i = 0
while i < len(x) :
    j = 0
    while j < len(y) :
        print(x[i], y[j])
        j =j + 1
    i = i + 1

##Output
1 4
1 5
2 4
2 5