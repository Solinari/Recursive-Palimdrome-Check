def Palimdromerie(pali):
    '''recursive string slicing to determine
    if a string is a palimdrome or not'''
    
    print(pali + '\n')
    
    if pali == '':
        
        print("Found a palimdrome!\n")
        return

    if pali[:1] == pali[-1:]:
        print("'{}' == '{}' ...\n".format(pali[:1], pali[-1:]))
        Palimdromerie(pali[1:-1])

    if pali[:1] != pali[-1:]:
        print("{} =/= {} !\n".format(pali[:1], pali[-1:]))
        print("Not a palimdrome.\n")
        return
        


palimdrome = "live evil"
nonpali = "sassafrass"

Palimdromerie(palimdrome)
Palimdromerie(nonpali)
