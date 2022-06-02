''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
code to optimize a singular funciton in a singular text file

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from time import perf_counter
import numpy as np
from copy import deepcopy

def main():
    #writes the code to code.py
    with open("test.txt", "r") as original:
        stored = np.array(original.readlines()) #stored is an array of the initial lines of code
        with open("code.py", "w") as code: #code.py is a file that stores the initial code
            code.writelines(stored)

    #gets output and time of the initial code
    best, output = timer("code.py")

    #loop
    ans = getbest(stored)

    print(ans)

#given filename return time of execution and output of function
def timer(filename):
    from code import func
    with open(filename, "w") as output:
        start = perf_counter()
        output = func()          
        end = perf_counter()
        time = end - start

        return time, output

def getbest(lines):
    code = open("current_code.py", "w")
    current_best = open("current_best.py", "w")
    
    best, output = timer("code.py")
    ans = lines
    current_best.writelines(ans)

    for i,ele in enumerate(lines[1:]):
        temp = np.delete(lines, i)

        code.writelines(temp)
        current_time, current_output = timer("current_code.py")

        if(output == current_output):
            ans = temp
            current_best.truncate(0)
            current_best.writelines(ans)

        code.truncate(0)

    code.close()
    current_best.close()

    return ans

if __name__ == "__main__":
    main()

file = open("current_code.py", "r")