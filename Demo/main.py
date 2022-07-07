def function(name, age=17, *args):
    print(name, age)
    print(args)

    for value in args:
        print(value)


function("naim", 8, 2, 3, 4)
