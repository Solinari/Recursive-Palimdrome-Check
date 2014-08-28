def Palimdromerie(pali):
    '''recursive string slicing to determine
    if a string is a palimdrome or not'''
    
    print(pali + '\n')
    
    if pali == '':
        
        print("Found a palimdrome!\n")
        return
    
    first = pali[:1]
    last = pali[-1:]
    rest = pali[1:-1]

    if first == last:
        print("'{}' == '{}' ...\n".format(first, last))
        Palimdromerie(rest)

    if first != last:
        print("{} =/= {} !\n".format(first, last))
        print("Not a palimdrome.\n")
        return
        


palimdrome = "live evil"
nonpali = "sassafrass"

Palimdromerie(palimdrome)
Palimdromerie(nonpali)
