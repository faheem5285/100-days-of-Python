#operators
# print(5**5)
# print(5//3)

# print("Enter your name:")
# name = input()
# print(f"Hello {name}")

#here we will create a calculator

#! taking input from user always in string data type if you want to use it in any other then you need to first convert it

a=input("ENTER FIRST NUMBER:")
b=input("ENTER (+, -, X, /, %,//,XX: )")
c=input("ENTER SECOND NUMBER: ")
a=float(a)
c=float(c)
if b == "+":
    sum1= a - c
    print(f"Hello {sum1}")
elif b == "-":
    sum1= a - c
    print(f"Hello {sum1}")
elif b == "*":
    sum1= a * c
    print(f"Hello {sum1}")
elif b == "/":
    sum1= a / c
    print(f"Hello {sum1}")
elif b == "//":
    sum1= a // c
    print(f"Hello {sum1}")
elif b == "%":
    sum1= a % c
    print(f"Hello {sum1}")
elif b == "**":
    sum1= a ** c
    print(f"Hello {sum1}")
else:
    print("no number found")


