import math

class Equation:

    def calc(self, a,b,c):
        d = b**2 -4 * a * c
        if d > 0:
            dqrt = math.sqrt(d)
            root1 = (-b + dqrt/(2*a))
            root2 =(-b - dqrt/(2*a))
            return root1 , root2
        elif d==0:
            return -b / (2*a)
        else:
            return "this equation has no roots"

if __name__ == '__main__':
    eqt = Equation()
    while True:
        a= int(input("a: "))
        b= int(input("b: "))
        c= int(input("c: "))
        result = eqt.calc(a,b,c)
        print(result)




