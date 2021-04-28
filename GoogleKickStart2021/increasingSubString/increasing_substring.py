def longest(word):
    stac = []
    result = []
    length = len(word)
    i = 0
    while i < length:
        current = word[i]
        if i == 0:
            stac.append(current)
            result.append(1)
            i+=1
            continue
        if current not in stac:
            if len(stac) and ord(current) > ord(stac[-1]):
                stac.append(current)
                result.append(len(stac))
            else:
                if len(stac):
                    result.append(len(stac))
                else:
                    result.append(1)
                stac = []
        else:
            result.append(1)
            stac = []
            stac.append(current)
        i+=1
    # print(result)
    return result
    

longest("ABACDA")
# longest("ABBC")
