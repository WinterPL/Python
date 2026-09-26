def printresult(int):
    print ("Result is " + str(int));
    return



print ("What is the first Number")
a = int(input())
print ("+-x/")
p = input()
print ("What is the Second Number")
b = int(input())

if p == "+":
    o = a+b
    printresult(o)
elif p == "-":
    o = a-b
    printresult(o)
elif p == "x":
    o = a*b
    printresult(o)
elif p == "/":
    o = a/b
    printresult(o)
else:
    print ("error")



