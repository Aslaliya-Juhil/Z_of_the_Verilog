from GLOBAL import *
def MEM(I):
    if I[0] == '000010':
        IF_ID['PC'] = EX_MEM['PC'] + 4
        GLBLPC['PC'] = EX_MEM['PC']
    elif I[0] == '000000':
        MEM_WB['WDATA'] = EX_MEM['ALURES']
        GLBLPC['PC'] = GLBLPC['PC'] + 4
    else:
        if I[0] == '001000':
            MEM_WB['WDATA'] = EX_MEM['ALURES']
        elif I[0] == '001100':
            MEM_WB['WDATA'] = EX_MEM['ALURES']
        elif I[0] == '001101':
            MEM_WB['WDATA'] = EX_MEM['ALURES']
        elif I[0] == '001110':
            MEM_WB['WDATA'] = EX_MEM['ALURES']
        elif I[0] == '101011':
            DMEM[EX_MEM['ALURES']%256] = EX_MEM['WDATA']
        elif I[0] == '100011':
            MEM_WB['RD'] = DMEM[EX_MEM['ALURES']%256]
        GLBLPC['PC'] = GLBLPC['PC'] + 4
    MEM_WB['WREG'] = EX_MEM['WREG']
    MEM_WB['IR'] = EX_MEM['IR']