user_num=int(input("enter the number please:   "))
def factorial(num):
    if num==1: return 1
    num*=factorial(num-1)
    return num
print(factorial(user_num))