x = [1, 2, 3]
y = [1, 2, 3]
z = y

print(x == z)
print(z == y)

z[0] = "asdf"
print(y)
