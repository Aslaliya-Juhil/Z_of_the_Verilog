from cProfile import label
from GLOBAL import *


def ID(I):
    if I[0] == '000000':
        ID_EX['RD1'] = REGMEM[int(I[1], 2)]
        ID_EX['RD2'] = REGMEM[int(I[2], 2)]
        ID_EX['PC'] = IF_ID['PC']
        ID_EX['WREG'] = int(I[3], 2)
    elif I[0] == '000010':
        ID_EX['PC'] = IF_ID['PC']
        if I[1] != 0 or I[1] not in LABLES.keys():
            ID_EX['IMM'] = int(I[1], 2)
        else:
            ID_EX['IMM'] = LABLES[I[1]]
    else:
        ID_EX['RD1'] = REGMEM[int(I[1], 2)]
        ID_EX['PC'] = IF_ID['PC']
        ID_EX['WREG'] = int(I[2], 2)
        if I[3] != 0 or I[3] not in LABLES.keys():
            ID_EX['IMM'] = int(I[3], 2)
        else:
            ID_EX['IMM'] = LABLES[I[3]]
    ID_EX['IR'] = IF_ID['IR']
