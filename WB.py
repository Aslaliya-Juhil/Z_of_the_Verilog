from GLOBAL import *


def WB(I):
    if I[0] == '000010':
        pass
    elif I[0] == '000000':
        REGMEM[MEM_WB['WREG']] = MEM_WB['WDATA']
    else:
        if I[0] == '001000':
            REGMEM[MEM_WB['WREG']] = MEM_WB['WDATA']
        elif I[0] == '001100':
            REGMEM[MEM_WB['WREG']] = MEM_WB['WDATA']
        elif I[0] == '001101':
            REGMEM[MEM_WB['WREG']] = MEM_WB['WDATA']
        elif I[0] == '001101':
            REGMEM[MEM_WB['WREG']] = MEM_WB['WDATA']
        elif I[0] == '100011':
            REGMEM[MEM_WB['WREG']] = MEM_WB['RD']
