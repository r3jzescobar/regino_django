#file=open("test.txt",r)
# def greet():
#     print("Hello Greetings from everyone!")
# greet()

# def greet(name):
#     print(f"hello {name}, How are you doing?")

# name = input("enter your name")

#greet(name)

# def chk_division(x,y):
#     if x % y == 0:
#         print("divisible by 0")
#     else:
#         print("not divisible")

# chk_division(5,9)

# def factorial(n):
#     for i in range(1, n+1):
#         print(i)
# factorial(3)


def mul(x,y):
    z= x*y
    #print(z)
    return z

#mul(4,5)

def main():
    print("enter 1st number ")
    a= int(input())
    print("Enter 2nd number ")
    b= int(input())
    result = mul(a,b)
    print("the result is ", result)

main()