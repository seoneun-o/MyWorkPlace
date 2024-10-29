'''
make a triangle with a given number

ex)
when you have a 5, then an image like below should be made

*
**
***
****
*****
'''

def makeTriangle(num):
    # show your work
    for line in range(5):
        for start in range(0, line+1,1):
            print("*", end="")
        print()
    
makeTriangle(5)