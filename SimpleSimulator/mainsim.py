import sys
import dump
import matplotlib.pyplot as plt
file1 = open('inputfile.txt', 'w')
file1.truncate(0)
for line in sys.stdin:
    file1.write(line)
file1.close()
file1 = open('inputfile.txt', 'r')
memory = file1.read().splitlines()
for i in range(0,len(memory) - 1):
    if(memory[i][-1] == "\n"):
        memory[i] = memory[i][0:-1]
temp0=256-len(memory)
for i in range(0,temp0):
    memory.append("0000000000000000")
reg_dict={"000":0,"001":0,"010":0,"011":0,"100":0,"101":0,"110":0}
FLAGS="0000000000000000"
PC=0
cycle=0
data=[]
halted=False
while(not halted):
    instruction=memory[PC]
    if instruction[:5]=="00000":     #add
        FLAGS="0000000000000000"
        reg_dict[instruction[7:10]]=reg_dict[instruction[10:13]] + reg_dict[instruction[13:]]
        if reg_dict[instruction[7:10]]>65535:
            FLAGS="0000000000001000"
            reg_dict[instruction[7:10]]=int(bin(reg_dict[instruction[7:10]])[-16:],2)
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="00001":     #sub
        FLAGS="0000000000000000"
        if reg_dict[instruction[13:]]>reg_dict[instruction[10:13]]:
            reg_dict[instruction[7:10]]=0
            FLAGS="0000000000001000"
        else:
            reg_dict[instruction[7:10]]=reg_dict[instruction[10:13]] - reg_dict[instruction[13:]]
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="00110":     #mul
        FLAGS="0000000000000000"
        reg_dict[instruction[7:10]]=reg_dict[instruction[10:13]] * reg_dict[instruction[13:]]
        if reg_dict[instruction[7:10]]>65535:
            FLAGS="0000000000001000"
            reg_dict[instruction[7:10]]=int(bin(reg_dict[instruction[7:10]])[-16:],2)
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="01010":     #Exlusive or
        FLAGS="0000000000000000"
        reg_dict[instruction[7:10]]=reg_dict[instruction[10:13]] ^ reg_dict[instruction[13:]]
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="01011":     #or
        FLAGS="0000000000000000"
        reg_dict[instruction[7:10]]=reg_dict[instruction[10:13]] | reg_dict[instruction[13:]]
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="01100":     #and
        FLAGS="0000000000000000"
        reg_dict[instruction[7:10]]=reg_dict[instruction[10:13]] & reg_dict[instruction[13:]]
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    elif instruction[:5]=="00010":     #move immediate
        FLAGS="0000000000000000"
        reg_dict[instruction[5:8]]=int(instruction[8:],2)
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="01000":     #right shift
        FLAGS="0000000000000000"
        reg_dict[instruction[5:8]]= reg_dict[instruction[5:8]] >> int(instruction[8:],2)
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1

    elif instruction[:5]=="01001":     #left shift
        FLAGS="0000000000000000"
        reg_dict[instruction[5:8]]= reg_dict[instruction[5:8]] << int(instruction[8:],2)
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="00011":     #move reg
        if instruction[13:]=="111":
            reg_dict[instruction[10:13]]=int(FLAGS,2)
        else:
            reg_dict[instruction[10:13]]=reg_dict[instruction[13:]]
        FLAGS="0000000000000000"
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1

    elif instruction[:5]=="00111":     #div
        FLAGS="0000000000000000"
        reg_dict["000"]=reg_dict[instruction[10:13]] // reg_dict[instruction[13:]]
        reg_dict["001"]=reg_dict[instruction[10:13]] % reg_dict[instruction[13:]]
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1

    elif instruction[:5]=="01101":     #not
        FLAGS="0000000000000000"
        temp=bin(reg_dict[instruction[13:]])[2:]
        rev = temp[::-1]
        while len(rev) < 16:
            rev = rev +'0'
        temp = rev[::-1]
        temp1=""
        for i in range(0,len(temp)):
            if temp[i]=="0":
                temp1=temp1+"1"
            else:
                temp1=temp1+"0"
        temp1=int(temp1,2)
        reg_dict[instruction[10:13]]=temp1
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="01110":     #cmp
        if reg_dict[instruction[10:13]]==reg_dict[instruction[13:]]:
            FLAGS="0000000000000001"
        elif reg_dict[instruction[10:13]]>reg_dict[instruction[13:]]:
            FLAGS="0000000000000010"
        elif reg_dict[instruction[10:13]]<reg_dict[instruction[13:]]:
            FLAGS="0000000000000100"
        else:
            FLAGS="0000000000000000"
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="00100":     #load
        FLAGS="0000000000000000"
        pos=int(instruction[8:],2)
        val=memory[pos]
        reg_dict[instruction[5:8]]=int(val,2)
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        data.append([cycle,pos])
        PC=PC+1
        cycle=cycle+1

    elif instruction[:5]=="00101":     #store
        FLAGS="0000000000000000"
        pos=int(instruction[8:],2)
        temp3=bin(reg_dict[instruction[5:8]])[2:]
        rev = temp3[::-1]
        while len(rev) < 16:
            rev = rev +'0'
        temp3 = rev[::-1]
        memory[pos]=temp3
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        data.append([cycle,pos])
        PC=PC+1
        cycle=cycle+1
    
    elif instruction[:5]=="01111":     #unconditional jump
        FLAGS="0000000000000000"  
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        cycle=cycle+1
        PC=int(instruction[8:],2)

    elif instruction[:5]=="10000":     #jump if less than
        flag_value = FLAGS 
        FLAGS="0000000000000000" 
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        cycle=cycle+1
        if flag_value == "0000000000000100": 
            PC=int(instruction[8:],2)
        else:
            PC=PC+1
    
    elif instruction[:5]=="10001":     #jump if greater than
        flag_value = FLAGS 
        FLAGS="0000000000000000" 
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        cycle=cycle+1
        if flag_value=="0000000000000010":
            PC=int(instruction[8:],2)
        else:
            PC=PC+1
    

    elif instruction[:5]=="10010":     #jump if equal 
        flag_value = FLAGS 
        FLAGS="0000000000000000" 
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        cycle=cycle+1
        if flag_value=="0000000000000001":     
            PC=int(instruction[8:],2)
        else:
            PC=PC+1
    elif instruction[:5]=="10011":    #hlt
        halted=True
        FLAGS="0000000000000000"
        ans=dump.print(PC,reg_dict,FLAGS)
        print(ans)
        data.append([cycle,PC])
        PC=PC+1
        cycle=cycle+1

for i in memory:
    print(i)
x,y=zip(*data)
plt.scatter(x,y)
plt.savefig('image.png')
