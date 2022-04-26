from GLOBAL import *


def EX(I):
    if I[0] == '000000':
        EX_MEM['ZERO'] = 0
        EX_MEM['WREG'] = ID_EX['WREG']
        if I[5] == '100000':
            EX_MEM['ALURES'] = ID_EX['RD1'] + ID_EX['RD2']
        elif I[5] == '100010':
            EX_MEM['ALURES'] = ID_EX['RD1'] - ID_EX['RD2']
        elif I[5] == '011000':
            EX_MEM['ALURES'] = ID_EX['RD1'] * ID_EX['RD2']
        elif I[5] == '011010':
            EX_MEM['ALURES'] = ID_EX['RD1'] / ID_EX['RD2']
        elif I[5] == '100100':
            EX_MEM['ALURES'] = ID_EX['RD1'] & ID_EX['RD2']
        elif I[5] == '100101':
            EX_MEM['ALURES'] = ID_EX['RD1'] | ID_EX['RD2']
        elif I[5] == '100110':
            EX_MEM['ALURES'] = ID_EX['RD1'] ^ ID_EX['RD2']
        elif I[5] == '101010':
            if ID_EX['RD1'] < ID_EX['RD2']:
                EX_MEM['ALURES'] = 1
            else:
                EX_MEM['ALURES'] = 0
    elif I[0] == '000010':
        EX_MEM['PC'] = ID_EX['PC'] + 4 * ID_EX['IMM']
    else:
        EX_MEM['ZERO'] = 0
        EX_MEM['WDATA'] = ID_EX['RD2']
        EX_MEM['PC'] = ID_EX['PC']
        EX_MEM['WREG'] = ID_EX['WREG']
        if I[0] == '001000':
            EX_MEM['ALURES'] = ID_EX['RD1'] + ID_EX['IMM']
        elif I[0] == '001100':
            EX_MEM['ALURES'] = ID_EX['RD1'] & ID_EX['IMM']
        elif I[0] == '001101':
            EX_MEM['ALURES'] = ID_EX['RD1'] | ID_EX['IMM']
        elif I[0] == '001110':
            EX_MEM['ALURES'] = ID_EX['RD1'] ^ ID_EX['IMM']
        elif I[0] == '000100':
            if ID_EX['RD1'] == ID_EX['IMM']:
                EX_MEM['PC'] = ID_EX['PC'] + 4 * ID_EX['IMM']
            else:
                EX_MEM['PC'] = ID_EX['PC']
        elif I[0] == '100011':
            EX_MEM['ALURES'] = ID_EX['RD1'] + ID_EX['IMM']
        elif I[0] == '101011':
            EX_MEM['ALURES'] = ID_EX['RD1'] + ID_EX['IMM']
    EX_MEM['IR'] = ID_EX['IR']
