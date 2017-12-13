def check_num(q,u,i,c,k,s):
    return (q+u+i+c+k+s)**3 == q*100000+u*10000+i*1000+c*100+k*10+s

def get_quicks():
    res = []
    for q in range(10):
        for u in range(10):
            for i in range(10):
                for c in range(10):
                    for k in range(10):
                        for s in range(10):
                            if check_num(q,u,i,c,k,s):
                                res.append([q,u,i,c,k,s])

    print res

get_quicks()
