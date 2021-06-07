print("*** Converting hh.mm.ss to seconds ***")
h,m,s = map(int,input("Enter hh mm ss : ").split())
if m>=0 and m<=59:
    n = (h*60*60)+(m*60)+s
    if n >= 0 and n<=999:
        if h<10 and m<10 and s<10:
            print("0%d:0%d:0%d = %d seconds"%(h,m,s,n))
        elif h<10 and m<10:
            print("0%d:0%d:%d = %d seconds"%(h,m,s,n))
        elif m<10 and s<10: 
            print("%d:0%d:0%d = %d seconds"%(h,m,s,n))
        elif h<10 and s<10: 
            print("0%d:%d:0%d = %d seconds"%(h,m,s,n))        
        elif h<10:
            print("0%d:%d:%d = %d seconds"%(h,m,s,n))
        elif m<10:   
            print("%d:0%d:%d = %d seconds"%(h,m,s,n))
        elif s<10:
            print("%d:%d:0%d = %d seconds"%(h,m,s,n))
        else :
            print("%d:%d:%d = %d seconds"%(h,m,s,n))
    else:
        if h<10 and m<10 and s<10:
            print("0%d:0%d:0%d = %d,%d seconds"%(h,m,s,n/1000,n%1000)) 
        elif h<10 and m<10:
            print("0%d:0%d:%d = %d,%d seconds"%(h,m,s,n/1000,n%1000)) 
        elif m<10 and s<10: 
            print("%d:0%d:0%d = %d,%d seconds"%(h,m,s,n/1000,n%1000)) 
        elif h<10 and s<10: 
            print("0%d:%d:0%d = %d,%d seconds"%(h,m,s,n/1000,n%1000))         
        elif h<10:
            print("0%d:%d:%d = %d,%d seconds"%(h,m,s,n/1000,n%1000)) 
        elif m<10:   
            print("%d:0%d:%d = %d,%d seconds"%(h,m,s,n/1000,n%1000)) 
        elif s<10:
            print("%d:%d:0%d = %d,%d seconds"%(h,m,s,n/1000,n%1000)) 
        else :
            print("%d:%d:%d = %d,%d seconds"%(h,m,s,n/1000,n%1000))  
else : print("mm(%d) is invalid!"%m)