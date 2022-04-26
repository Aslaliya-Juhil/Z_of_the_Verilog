from GLOBAL import *


def IF(imem, PC):
    i = imem[PC//4]
    insn = []
    tag = ''
    if i[0][-1] == ':':
        tag = i[0]
        i = i[1:]
    if i[0] in RTYPE.keys():
        insn.append('000000')
        insn.append(str(bin(REGS[i[2]]))[2:])
        insn.append(str(bin(REGS[i[3]]))[2:])
        insn.append(str(bin(REGS[i[1]]))[2:])
        insn.append('00000')
        insn.append(str(bin(RTYPE[i[0]]))[2:])
        if len(insn[1]) < 5:
            insn[1] = '0'*(5-len(insn[1]))+insn[1]
        if len(insn[2]) < 5:
            insn[2] = '0'*(5-len(insn[2]))+insn[2]
        if len(insn[3]) < 5:
            insn[3] = '0'*(5-len(insn[3]))+insn[3]
        if len(insn[5]) < 6:
            insn[5] = '0'*(6-len(insn[5]))+insn[5]
    if i[0] in ITYPE.keys():
        insn.append(str(bin(ITYPE[i[0]]))[2:])
        offset = ''
        if ITYPE[i[0]] == 43 or ITYPE[i[0]] == 35:
            src = ''
            includesrc = False
            for c in i[-1]:
                if includesrc == False:
                    if c == '(':
                        includesrc = True
                    else:
                        offset = offset + c
                else:
                    if c == ')':
                        continue
                    else:
                        src = src + c
            insn.append(str(bin(REGS[src]))[2:])
            insn.append(str(bin(REGS[i[1]]))[2:])
            insn.append(str(bin(int(offset)))[2:])
        else:
            insn.append(str(bin(REGS[i[2]]))[2:])
            insn.append(str(bin(REGS[i[1]]))[2:])
            if i[3][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if i[3] in LABLES.keys():
                    insn.append(str(bin(LABLES[i[3]]))[2:])
                else:
                    insn.append('0')
            else:
                insn.append(str(bin(int(i[3])))[2:])
        if len(insn[0]) < 6:
            insn[0] = '0'*(6-len(insn[0]))+insn[0]
        if len(insn[1]) < 5:
            insn[1] = '0'*(5-len(insn[1]))+insn[1]
        if len(insn[2]) < 5:
            insn[2] = '0'*(5-len(insn[2]))+insn[2]
        if len(insn[3]) < 16:
            insn[3] = '0'*(16-len(insn[3]))+insn[3]
    if i[0] in JTYPE.keys():
        insn.append(str(bin(JTYPE[i[0]]))[2:])
        if i[1][0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if i[1] in LABLES.keys():
                insn.append(str(bin(LABLES[i[1]]))[2:])
            else:
                insn.append('0')
        else:
            insn.append(str(bin(int(i[1])))[2:])
        if len(insn[0]) < 6:
            insn[0] = '0'*(6-len(insn[0]))+insn[0]
        if len(insn[1]) < 26:
            insn[1] = '0'*(26-len(insn[1]))+insn[1]
    if tag != '':
        LABLES[tag] = PC
    IF_ID['IR'] = insn
    IF_ID['PC'] = PC + 4
