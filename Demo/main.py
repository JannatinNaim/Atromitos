# x = []

# for i in range(1, 101):
#     if i % 2 == 0:
#         x.append(i * i)
#     else:
#         x.append(i * 2)

# print(x)

x = [i * i if i % 2 == 0 else i * 2 for i in range(1, 101)]
print(x)
