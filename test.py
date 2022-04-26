from GLOBAL import *
from IMEM import imem
from IF import IF
from ID import ID
from EX import EX
from MEM import MEM
from WB import WB
i = 0
while i < (len(imem)):
    IF(imem, 4*i)
    i += 1
clocks = 0
GLBLPC['PC'] = 0
while True:
    IF(imem, GLBLPC['PC'])
    ID(IF_ID['IR'])
    EX(ID_EX['IR'])
    MEM(EX_MEM['IR'])
    WB(MEM_WB['IR'])
    clocks += 1
    print(IF_ID['IR'])
    if GLBLPC['PC'] >= 56:
        break
print(REGMEM)
print(DMEM)
