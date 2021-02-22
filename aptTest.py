# - The user should input two numbers
# - Then print out numbers from 0 to 1000
# - When a number is divisible by the smaller input number, instead print "HANS"
# - When a number is divisible by the larger input number, instead print "DEKKERS"
# - When a number is divisible by both, instead print "HANS DEKKERS
# - returns a list containing the resulting strings for each number (0-1000 is incusive)
def hansDekkers(smallNum, largeNum):
    resList = []
    
    for i in range(0, 1001):
        res = ""
        
        if i % smallNum == 0:
            res = "Hans"
        
        if i % largeNum == 0:
            if res != "":
                res += " Dekkers"
            else:
                res = "Dekkers"
        
        resList = resList + [res]
        
    return resList

print(hansDekkers(3,4))