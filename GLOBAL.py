REGS = {'$zero': 0, '$at': 1, '$v0': 2, '$v1': 3,
        '$a0': 4, '$a1': 5, '$a2': 6, '$a3': 7,
        '$t0': 8, '$t1': 9, '$t2': 10, '$t3': 11,
        '$t4': 12, '$t5': 13, '$t6': 14, '$t7': 15,
        '$s0': 16, '$s1': 17, '$s2': 18, '$s3': 19,
        '$s4': 20, '$s5': 21, '$s6': 22, '$s7': 23,
        '$t8': 24, '$t9': 25, '$k0': 26, '$k1': 27,
        '$gp': 28, '$sp': 29, '$fp': 30, '$ra': 31}
REGMEM = [0 for i in range(32)]
ITYPE = {'addi': 8, 'beq': 4, 'lw': 35,
         'sw': 43, 'andi': 12, 'ori': 13, 'xori': 14}
RTYPE = {'add': 32, 'sub': 34, 'mult': 24, 'div': 26,
         'and': 36, 'or': 37, 'xor': 38, 'slt': 42}
JTYPE = {'j': 2}
DMEM = [i for i in range(256)]
CONTROLS = {'RegWrite': 0, 'ALUSrc': 0, 'PCSrc': 0,
            'MemWrite': 0, 'MemRead': 0, 'MemToReg': 0}
IF_ID = {'PC': 0, 'IR': []}
ID_EX = {'PC': 0, 'RD1': 0, 'RD2': 0, 'IMM': 0, 'WREG': 0, 'IR': []}
EX_MEM = {'PC': 0, 'ZERO': 0, 'ALURES': 0, 'WDATA': 0, 'WREG': 0, 'IR': []}
MEM_WB = {'RD': 0, 'WDATA': 0, 'WREG': 0, 'IR': []}
LABLES = {}
GLBLPC = {'PC': 0}
