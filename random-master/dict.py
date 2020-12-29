d1 = {'a': '100', 'b': 200, 'c':300}
d2 = {'a': 300, 'b': '200', 'd':400}


d3 = dict(d1)
d3.update(d2) 

for z, j in d1.items():
    j = int(j)
    for x, y in d2.items():
        y = int(y)
        if z == x:
            d3[z]=(j+y)
print(d3)


