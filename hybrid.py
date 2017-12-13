#Hybrid method of increment method and newton raphson method

x= 0
nt=1
dft= 3/(4*nt)
for it in range(1,nt+1,1):
    fit= dft*it
    while True:
        gx= x/(x+1)-fit
        dgx= 1.0/(1+x)**2 
        dx= -(gx/dgx) 
        x= x+dx
        if abs(gx)>10**-8:
            continue
        else:            
            print('the value of x is {0} with error of {1}'. format(x,dgx))
            break
        
