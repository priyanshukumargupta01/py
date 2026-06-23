# Loop Examples

#for loop
for i in range(5):
    print(i)        

#while loop
count = 0
while count < 5:
    print(count)
    count += 1

#nested loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")  

#Using continue
for i in range(5):
    if i == 2:
        continue
    print(i) 