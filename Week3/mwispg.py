from pprint import *

if __name__ == '__main__':
    with open("week3\mwis.txt") as f:
        lines = f.readlines()
        count = lines[0]
        weights = [int(line) for line in lines[1:]]

        mwis = [0, weights[0]]        

    for w in weights[1:]:
        mwis.append(max(mwis[-1], mwis[-2] + w))

    result = {}
    i = 1
    while i < len(mwis):
        cur_weight = weights[-i]
        if(mwis[-i-1] >= mwis[-i-2] + weights[-i]):
            result[cur_weight] = 0
            i += 1
        else:
            result[cur_weight] = 1
            result[weights[-i-1]] = 0
            i += 2


    # pprint(result)
    pprint(result[weights[0]])
    pprint(result[weights[1]])
    pprint(result[weights[2]])
    pprint(result[weights[3]])
    pprint(result[weights[16]])
    pprint(result[weights[116]])
    pprint(result[weights[516]])
    pprint(result[weights[996]])
    # pprint(result[2])
    # pprint(result[3])
    # pprint(result[4])
    # pprint(result[17])
    # pprint(result[117])
    # pprint(result[517])
    # pprint(result[997])
    



