import array as arr
a = arr.array('i', [1, 23, 3])

print(a)

# Adding 2 in each element of the array
a_plus_2 = arr.array('i', (x+2 for x in a))
print(a_plus_2)

for x in a:
    print(x)