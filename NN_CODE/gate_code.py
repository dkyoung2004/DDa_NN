def AND_gate(x1,x2):
    w1=0.7
    w2=0.7
    b=-0.4
    result = x1*w1+x2*w2 +b
    if result >=1:
        return 1
    else:
        return 0
def NAND_gate(x1,x2):
    w1=0.7
    w2=0.7
    b=-0.4
    result = x1*w1+x2*w2 +b
    if result >= 1:
        return 0
    else:
        return 1
