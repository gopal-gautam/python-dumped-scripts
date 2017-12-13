# initial condition
x = 0
nt=10
dft= 3.0/(4*nt)
it=1
#for it in range(1,nt,1):
while it<= nt :
    print "Loop: "+str(it)
    fit=(dft* it)
    print "fit = "+str(fit)
    gx= 1/(x+1)- fit
    print "gx = "+str(gx)
    dgx= 1.0/(1+x)**2
    print "dgx = "+str(dgx)
    dx= -(gx/dgx)
    print "dx = "+str(dx)
    x= x+dx
    print "x = "+str(x)
    it*= 10
print ('the value of x is {0} with error of {1}'. format(x,dgx))

    
    

    
