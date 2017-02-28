from pprint import *

if __name__ == '__main__':
    with open("week4\sack.txt") as f:
        line = f.readline()
        capacity, count = (int(x) for x in line.split(' '))                

        vw =  [[int(x) for x in line.split(' ')] for line in f.readlines()]
    
    a = [[0 for x in range(capacity + 1)] for y in range(count + 1)] 



    # i goes on nodes to use 
    # x goes on residual capacity 
    

    # generate info about what values from a we really need we need 


    # generate matrix
    for i in range(1, count + 1):
        for x in range(capacity + 1):
            if x - vw[i-1][1] >= 0:
                a[i][x] = max(a[i-1][x], a[i-1][x-vw[i-1][1]] + vw[i -1][0])
            else:
                a[i][x] = a[i-1][x]
    
    pprint(a[count][capacity])