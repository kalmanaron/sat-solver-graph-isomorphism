SIZE = 80

matrix = ""
for i in range(SIZE):
    for ii in range(SIZE):
        matrix += "1"
        if ii != SIZE -1:
            matrix += ' '
    if i != SIZE-1:
        matrix += '\n'

print(matrix)