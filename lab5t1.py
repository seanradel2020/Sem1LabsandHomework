#Sean Radel
#Lab 5 task 1, a and b


print("(a.)")
print()
for i in range(1,4):
    print("This is the outside loop on iteration", i)
    for k in range(1,3):
        print("This is the inside loop on iteration:",k)
print()
print("(b.)")
print()
fun = ""
game = input("Wanna play a game?")
while game.lower() != 'n':
    while fun.lower() != 'n':
        fun = input("Are you having fun?")
    game = input("Wanna play a game?")
print()
print("(c.)")
print()
for i in range(1,101):
    num = 0
    for k in range(i):
        num = num + k

    print(num)
    
