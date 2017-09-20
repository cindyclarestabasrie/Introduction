h = 10
x = 1
star = "*"
y = 1
for i in range (1, 6):
    print (" " * (h-x), star * y)
    x += 1
    y += 2
for i in range (6, 12):
    print (" " * (h-x), star * y)
    x -= 1
    y -= 2
