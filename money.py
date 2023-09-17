num = int(input("Enter an integer number: "))
num = num % 2
print(num)
if num == 0:
    is_even = False
else:
    is_even = True
is_even1 = is_even if num > 0 else False
print(is_even1)