import json

def BuildAttackMatrix(fd):
    f = open(fd)
    a_mtrx = json.load(f)
    f.close()
    return a_mtrx
