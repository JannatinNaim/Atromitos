try:
    user_input = input("enter a number: ")
    x = int(user_input)
    result = 1234 / x
    print(result)
except ValueError:
    print("value error")
except ZeroDivisionError:
    print("zero division error")
except:
    print("uncaught error")


try:
    # fetch data
    pass
except:
    print("some error occurred")


# user_input = input("enter a number: ")
# x = int(user_input)

# user_input = input("enter a number: ")
# x = int(user_input)
# result = 1234 / x
# print(result)
