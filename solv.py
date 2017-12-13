g=lambda x,y: 3*x+4*y-24
f=lambda x,y: 4*x+3*y-25
x=1;
while(True):
    for y in range(x):
        if f(x,y)==0 and g(x,y)==0:
            print("x=%d, y=%d, f=%d, g=%d" %(x,y,f(x,y),g(x,y)))
            print(x,y)
            break
        else:
            print("x=%d, y=%d, f=%d, g=%d" %(x,y,f(x,y),g(x,y)))
    else:
        x=x+1
        continue
    break
