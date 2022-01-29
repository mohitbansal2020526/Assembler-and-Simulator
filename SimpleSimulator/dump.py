def print(PC,reg_dict,Flags):
    req_pc = bin(PC)[2:]
    rev = req_pc[::-1]
    while len(rev) < 8:
        rev = rev +'0'
    req_pc = rev[::-1]

    req_r0=bin(reg_dict["000"])[2:]
    rev = req_r0[::-1]
    while len(rev) < 16:
        rev = rev +'0'
    req_r0 = rev[::-1]

    req_r1=bin(reg_dict["001"])[2:]
    rev = req_r1[::-1]
    while len(rev) < 16:
        rev = rev +'0'
    req_r1 = rev[::-1]
    
    req_r2=bin(reg_dict["010"])[2:]
    rev = req_r2[::-1]
    while len(rev) < 16:
        rev = rev +'0'
    req_r2 = rev[::-1]

    req_r3=bin(reg_dict["011"])[2:]
    rev = req_r3[::-1]
    while len(rev) < 16:
        rev = rev +'0'
    req_r3 = rev[::-1]

    req_r4=bin(reg_dict["100"])[2:]
    rev = req_r4[::-1]
    while len(rev) < 16:
        rev = rev +'0'
    req_r4 = rev[::-1]

    req_r5=bin(reg_dict["101"])[2:]
    rev = req_r5[::-1]
    while len(rev) < 16:
        rev = rev +'0'
    req_r5 = rev[::-1]

    req_r6=bin(reg_dict["110"])[2:]
    rev = req_r6[::-1]
    while len(rev) < 16:
        rev = rev +'0'
    req_r6 = rev[::-1]

    return(req_pc + " " + req_r0 + " " + req_r1 + " " + req_r2 + " " + req_r3 + " " + req_r4 + " " + req_r5 + " " + req_r6 + " " + Flags)



