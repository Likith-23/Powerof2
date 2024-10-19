#program to check if the number is the power of 2
def power_of2(number):
    #as the power of 2 will have one set bit, then n- 1 & n will always be be 0 for any power of two
    if (number == 0):
        return 0
    if ((number & (~ (number - 1))) == number):
        return 1
    return 0
number = int(input("ENTER A NUMBER............................"))
if (power_of2(number)):
    print("The number is the power of 2..............................................................:)")
else:
    print("The number is not the power of 2.........................................:)")