x = int(input("x = "))
n = input("Operation(+,-,*,/): ")
y = int(input("y = "))

# print("* " * 20)
# if n == "+":
#     a = x +y
#     print("{} {} {} = {}".format(x,n,y,a))
# elif n == "-":
#     a = x - y
#     print("{} {} {} = {}".format(x,n,y,a))
# elif n == "*":
#     a = x *y
#     print("{} {} {} = {}".format(x,n,y,a))
# elif n =="/":
#     a = x / y
#     print("{} {} {} = {}".format(x,n,y,a))
res = 0
if n == "+":
    res = x + y
elif n =="-":
    res = x - y
elif n == "*":
    res = x * y
elif n =="/":
    res = x / y
    
print("* " * 20)
print("{} {} {} = {}".format(x,n,y,res))
print("* " * 20)