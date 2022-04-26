filename = "/home/juhil/Workspace/python/ES215_Project/instructions.txt"
file = open(filename)
imem = []
for l in file:
    imem.append(l.strip().split(' '))
for i in range(len(imem)):
    for k in range(len(imem[i])):
        if imem[i][k][-1] == ',':
            imem[i][k] = imem[i][k][0:len(imem[i][k])-1]
