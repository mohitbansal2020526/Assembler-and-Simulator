import opcode
def return_register(str):
    if(str == "R0"):
        return "000"
    elif(str == "R1"):
        return "001"
    elif(str == "R2"):
        return "010"
    elif(str == "R3"):
        return "011"
    elif(str == "R4"):
        return "100"
    elif(str == "R5"):
        return "101"
    elif(str == "R6"):
        return "110"
    elif(str == "FLAGS"):
        return "111"


def type_a(a):
    list_a = a.split()
    reg1 = return_register(list_a[1])
    reg2 = return_register(list_a[2])
    reg3 = return_register(list_a[3])
    if (list_a[0] == "add"):
        return opcode.add_op +"00"+ reg1 + reg2 + reg3
    elif (list_a[0] == "sub"):
        return opcode.sub_op +"00"+ reg1 + reg2 + reg3
    elif (list_a[0] == "mul"):
        return opcode.mul_op +"00"+ reg1 + reg2 + reg3
    elif (list_a[0] == "xor"):
        return opcode.xor_op +"00"+ reg1 + reg2 + reg3
    elif (list_a[0] == "or"):
        return opcode.or_op + "00"+ reg1 + reg2 + reg3
    elif (list_a[0] == "and"):
        return opcode.and_op + "00"+ reg1 + reg2 + reg3


def type_b(a):
    list_a = a.split()
    reg = return_register(list_a[1])
    immed_value  = int(list_a[2][1:])
    req_bin = bin(immed_value)[2:]
    rev = req_bin[::-1]
    while len(rev) < 8:
        rev = rev +'0'
    req_bin = rev[::-1]

    if(list_a[0] == "mov"):
        return opcode.mov_imm_op + reg + req_bin
    elif(list_a[0] == "rs"):
        return opcode.rs_op + reg + req_bin
    elif(list_a[0] == "ls"):
        return opcode.ls_op + reg + req_bin


def type_c(a):
    list_a = a.split()
    reg1 = return_register(list_a[1])
    reg2 = return_register(list_a[2])
    if(list_a[0] == "mov"):
        return opcode.mov_reg_op +"00000" + reg1 + reg2
    elif(list_a[0] == "div"):
        return opcode.div_op +"00000" + reg1 + reg2
    elif(list_a[0] == "not"):
        return opcode.not_op +"00000" + reg1 + reg2
    elif(list_a[0] == "cmp"):
        return opcode.cmp_op +"00000" + reg1 + reg2
    

def type_d(a, var_dict):
    list_a  = a.split()
    reg = return_register(list_a[1])
    mem_add = var_dict[list_a[2]]
    req_bin = bin(mem_add)[2:]
    rev = req_bin[::-1]
    while len(rev) < 8:
        rev = rev +'0'
    req_bin = rev[::-1]
    if(list_a[0] == "ld"):
        return opcode.ld_op + reg + req_bin
    else:
        return opcode.st_op + reg + req_bin


def type_e(a, label_dict):
    list_a = a.split()
    mem_add = label_dict[list_a[1]]
    req_bin = bin(mem_add)[2:]
    rev = req_bin[::-1]
    while len(rev) < 8:
        rev = rev +'0'
    req_bin = rev[::-1]
    if(list_a[0] == "jmp"):
        return opcode.jmp_op + "000" + req_bin
    elif(list_a[0] == "jlt"):
        return opcode.jlt_op + "000" + req_bin
    elif(list_a[0] == "jgt"):
        return opcode.jgt_op + "000" + req_bin
    else:
        return opcode.je_op + "000" + req_bin


def type_f(s):
    if s == "hlt" :
        return(opcode.hlt_op +"00000000000")
