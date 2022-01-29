import regvalue
def check_error(str):
    s=str.split()
    if s[0][-1]==":":
        s.pop(0)
    if s[0]!="add" and s[0]!="sub" and s[0]!= "mov" and s[0]!="ld" and s[0]!="st" and s[0]!="mul" and s[0]!="div" and s[0]!="rs" and s[0]!="ls" and s[0]!="xor" and s[0]!="or" and s[0]!="and" and s[0]!="not" and s[0]!="cmp" and s[0]!="jmp" and s[0]!="jlt" and s[0]!="jgt" and s[0]!="je" :
        return(-1)
    if s[0]=="add" or s[0]=="sub" or s[0]=="mul" or s[0]=="xor" or s[0]=="or"  or s[0]=="and":
        if len(s)!=4:
            return(-2)
        else:
            if s[1]=="FLAGS" or s[2]=="FLAGS" or s[3]=="FLAGS":
                return(-5)
            if s[1] in regvalue.reg_list and s[2] in regvalue.reg_list and s[3] in regvalue.reg_list:
                return(0)
            else:
                return(-3)
    if s[0]=="mov":
        if len(s)!=3:
            return(-2)
        if s[1]=="FLAGS":
            return(-5)
        if s[1] in regvalue.reg_list:
            if s[2] in regvalue.reg_list or s[2]=="FLAGS":
                return(0)
    if s[0]=="mov" or s[0]=="rs" or s[0]== "ls" : #typeb
        if len(s)!=3:
            return(-2)
        else:
            if s[1]=="FLAGS":
                return(-5)
            if s[1] not in regvalue.reg_list: 
                return(-3)
            if s[2][0]!="$":
                return(-2)
            for i in range(1,len(s[2])-1):
                if s[2][i]!="0" and s[2][i]!="1" and s[2][i]!="2" and s[2][i]!="3" and s[2][i]!="4" and s[2][i]!="5" and s[2][i]!="6" and s[2][i]!="7" and s[2][i]!="8" and s[2][i]!="9" :
                    return(-4)
            int_s=int(s[2][1:])
            if int_s<0 or int_s>255:
                return(-4)  
            else:
                return(0)
    if s[0]=="div" or s[0]=="not" or s[0]=="cmp": #type c
        if len(s)!=3:
            return(-2)
        if s[1]=="FLAGS" or s[2]=="FLAGS":
            return(-5)
        if s[1] not in regvalue.reg_list or s[2] not in regvalue.reg_list:
            return(-3)
        return 0
    
    if s[0]=="ld" or s[0]=="st":
        if len(s)!=3:
            return(-2)
        if s[1]=="FLAGS":
            return(-5)
        if s[1] not in regvalue.reg_list:
            return(-3)
        if s[2] in regvalue.reg_list or s[2][0]=="$":
            return(-2)
        return(0)
    if s[0]=="jmp" or s[0]=="jlt" or s[0]=="jgt" or s[0]=="je" :
        if len(s)!=2:
            return(-2)
        if s[1][0]=="$":
            return(-2)
        return(0)
def print_error(i,l):
    l=l+1
    if i==-1:
        return("Typo error in instruction name in line no "+ str(l))
    if i==-2:
        return("Intruction used as wrong type in line no " + str(l))
    if i==-3:
        return("Typo in register value in line no " + str(l))
    if i==-4:
        return("Illegal use of immediate value in line no " + str(l))
    if i==-5:
        return("Illegal use of FLAGS register in line no " +str(l))
