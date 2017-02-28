from pprint import *

if __name__ == '__main__':
    with open("week3\mwis.txt") as f:
        lines = f.readlines()
        count = lines[0]
        weights = [int(line) for line in lines[1:]]

        mwis = [0, weights[0]]        

    for w in weights[1:]:
        if(mwis[-2] + w > mwis[-1]):
            mwis.append(mwis[-2] + w)
        else:
            mwis.append(mwis[-1])            
        
    result = []
    i = 1
    while i < len(mwis):
        cur_weight = weights[-i]  
        if i == (len(mwis) - 1):
            result.insert(0, 1)
            break;            
        if (i == (len(mwis) - 1) or mwis[-i-1] >= mwis[-i-2] + weights[-i]):
            result.insert(0, 0)
            i += 1
        else:
            result.insert(0, 1)
            result.insert(0, 0)
            i += 2

    pprint(len(result))

    # pprint(result)
    pprint(result[0])
    pprint(result[1])
    pprint(result[2])
    pprint(result[3])
    pprint(result[16])
    pprint(result[116])
    pprint(result[516])
    pprint(result[996])
    



