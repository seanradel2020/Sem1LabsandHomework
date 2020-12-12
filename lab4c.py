##############################
# LAB 4 Block C              #
# by Sean Radel    #
##############################

##############################################################################
# The following block of code should print a block of numbers. It
# doesn't. Fix it. When fixed, it should print exactly the following block
# of ten lines:

# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9

outer = 1

while outer > 0 and outer < 11:
    for i in range(1,11):
        print(i, end=" ")
    print()
    outer = outer + 1
