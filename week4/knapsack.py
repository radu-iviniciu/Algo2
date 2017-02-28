from pprint import *

def gen_pairs(pairs, weights, elem, capacity):
    pairs.append((elem, capacity))
    if elem > 1:        
        gen_pairs(pairs, weights, elem - 1, capacity)
        if capacity - weights[elem - 1] > 0:   # -1 since it is zero indexed
            gen_pairs(pairs, weights, elem - 1, capacity - weights[elem - 1])

if __name__ == '__main__':
    with open("week4\sack.txt") as f:
        line = f.readline()
        capacity, count = (int(x) for x in line.split(' '))                

        val_weights =  [[int(x) for x in line.split(' ')] for line in f.readlines()]
    
    a = [[0 for x in range(capacity + 1)] for y in range(count + 1)] 

    # i goes on nodes to use 
    # x goes on residual capacity 
    

    # generate info about what values from a we really we need 
    x = capacity        

    ix_pairs = [()]
    gen_pairs(ix_pairs, [vw[1] for vw in val_weights], count, capacity)

    pprint(len(ix_pairs))

    # generate matrix
    for i in range(1, count + 1):
        for x in range(capacity + 1):
            if x - val_weights[i-1][1] >= 0:
                a[i][x] = max(a[i-1][x], a[i-1][x - val_weights[i-1][1]] + val_weights[i -1][0])
            else:
                a[i][x] = a[i-1][x]
    
    pprint(a[count][capacity])
