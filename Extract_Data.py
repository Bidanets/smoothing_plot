def get_data(line):
        num = 0
        for j in range(3, len(line)):
            if line[j] == ":":
                break
            else:
                num *= 10
                num += int(line[j])
                
        j+=2
        
        Q = float(line[j:len(line)])
        
        return num, Q

def Extract_Data(filename = "Q_log_file.txt"):
    f = open(filename, "r")
    
    cnt = 0  
    iters_lst = []
    Q = []

    for line in f:
        if line[0:3] == "it ":
            cur_it, cur_Q = get_data(line)
            iters_lst.append(cur_it)
            Q.append(cur_Q)

    return iters_lst, Q
            


    