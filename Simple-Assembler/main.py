import binary_converter
import error
import opcode
import regvalue
import sys

def main_fun():
    final_answer = []

    file1 = open('inputfile.txt', 'w')
    file1.truncate(0)
    for line in sys.stdin:
        file1.write(line)
    file1.close()
    file1 = open('inputfile.txt', 'r')
    inp_list = file1.read().splitlines()

    for i in range(0,len(inp_list) - 1):
        if(inp_list[i][-1] == "\n"):
            inp_list[i] = inp_list[i][0:-1]
    var_dict = {}
    label_dict = {}
    counter = -1
    counter_var = 0
    check_var = -1
    if "hlt" in inp_list[0:-1]:
        return "hlt is not the last instruction !"
    
    

    if(inp_list[-1] != "hlt"):
        last_label = inp_list[-1].split()
        if(len(last_label)==2 ):
            if(last_label[0][-1] == ":" and last_label[1]=="hlt" ):
                pass
        else:
            return "missing hlt instruction !"

    for i in inp_list:
        lis = i.split()
        if(i==""):
            pass
        elif(lis[0] == "var"):
            pass
        elif(lis[0][-1] == ":" ):
            counter += 1
            label_dict[lis[0][0:-1]] = counter
        else:
            counter += 1
    
    for line,j in enumerate(inp_list):
        lis1 = j.split()
        if(j==""):
            pass
        elif(lis1[0] == "var"):
            if(check_var == -1):  
                counter_var += 1
                var_dict[lis1[1]] = counter + counter_var
            else:
                return ("variable not defined in starting error in line no "+str(line+1))
        else:
            check_var+=1

    for k in range(0,len(inp_list)):
        ins=inp_list[k].split()
        if ins[0][-1]==":":
            ins.pop(0)
        if inp_list[k]=="" or ins[0]=="var":
            pass
        elif ins[0]=="hlt":
            ans=binary_converter.type_f(ins[0])
            final_answer.append(ans)
        else:
            err = error.check_error(inp_list[k])
            if(err == 0):
                
                if ins[0][-1]==":":
                    ins.pop(0)
                if ins[0]=="add" or ins[0]=="sub" or ins[0]=="mul" or ins[0]=="xor" or ins[0]=="or"  or ins[0]=="and":
                    par=" ".join(ins)
                    ans=binary_converter.type_a(par)
                    final_answer.append(ans)
                elif ins[0]=="rs" or ins[0]== "ls" :
                    par=" ".join(ins)
                    ans=binary_converter.type_b(par)
                    final_answer.append(ans)
                elif ins[0]=="mov":
                    if ins[2] in regvalue.reg_list or ins[2] == "FLAGS":
                        par=" ".join(ins)
                        ans=binary_converter.type_c(par)
                        final_answer.append(ans)
                    else:
                        par=" ".join(ins)
                        ans=binary_converter.type_b(par)
                        final_answer.append(ans)
                elif ins[0]=="div" or ins[0]=="not" or ins[0]=="cmp":
                        par=" ".join(ins)
                        ans=binary_converter.type_c(par)
                        final_answer.append(ans)
                elif ins[0]=="ld" or ins[0]=="st":
                    if ins[2] not in var_dict.keys():
                        return("Undefined variable used in line no " +str(k+1))
                    else:
                        par=" ".join(ins)
                        ans=binary_converter.type_d(par,var_dict)
                        final_answer.append(ans)

                elif ins[0]=="jmp" or ins[0]=="jlt" or ins[0]=="jgt" or ins[0]=="je" :
                    if ins[1] not in label_dict.keys():
                        return("Undefined Label used in line no " +str(k+1))
                    else:
                        par=" ".join(ins)
                        ans=binary_converter.type_e(par,label_dict)
                        final_answer.append(ans)
            
            
            else:
                return error.print_error(err,k)
    return(final_answer)
            
a=main_fun()
if isinstance(a,str)==True:
    print(a)
else:
    for i in a:
        print(i)