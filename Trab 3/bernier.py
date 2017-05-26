import numpy as np

def bernier(x,y,q):
    n = len(x)
    a = np.zeros([n,2,2])
    cx = np.zeros(n-1)
    bx = np.zeros(n-1)
    ax = np.zeros(n-1)
    cy = np.zeros(n-1)
    by = np.zeros(n-1)
    ay = np.zeros(n-1)
    w = np.multiply(q,np.pi/180)
    
    for i in range(0,n-1):
        """a[i,0,0] = x[i] + 1
        a[i,0,1] = x[i+1] - 1
        a[i,1,0] = y[i] + 1*np.tan(w[i])
        a[i,1,1] = y[i+1] - 1*np.tan(w[i+1])"""
        a[0,0,0] = x[0] + 1
        a[0,0,1] = x[1] -0.1
        a[0,1,0] = y[0] + 1
        a[0,1,1] = y[1]
        a[1,0,0] = x[1] + 1
        a[1,0,1] = x[2] -1
        a[1,1,0] = y[1] + 1*np.tan(w[2])
        a[1,1,1] = y[2] - 1*np.tan(w[3])
        a[2,0,0] = x[2] + 0.5
        a[2,0,1] = x[3] -0.5
        a[2,1,0] = y[2] + 0.5*np.tan(w[4])
        a[2,1,1] = y[3] - 0.5*np.tan(w[5])
        cx[i]=3*(a[i,0,0]-x[i])
        bx[i]=3*(a[i,0,1]-a[i,0,0])-cx[i]
        ax[i]=(x[i+1]-x[i])-(cx[i]+bx[i])
        cy[i]=3*(a[i,1,0]-y[i])
        by[i]=3*(a[i,1,1]-a[i,1,0])-cy[i]
        ay[i]=(y[i+1]-y[i])-(cy[i]+by[i])
    
    t = np.linspace(0,1,101)
    xx = np.zeros([101,4])
    yy = np.zeros([101,4])
    for j in range(0,n-1):
        for i in range(0,101):
            xx[i,j] = x[j] + t[i]*(cx[j] + t[i]*(bx[j] + t[i]*ax[j]))
            yy[i,j] = y[j] + t[i]*(cy[j] + t[i]*(by[j] + t[i]*ay[j]))
    xxx=np.zeros(407)
    yyy=np.zeros(407)
    xxx[0:101] = xx[0:101,0]
    xxx[101:202] = xx[0:101,1]
    xxx[202:303] = xx[0:101,2]
    xxx[303:404] = xx[0:101,3]
    yyy[0:101] = yy[0:101,0]
    yyy[101:202] = yy[0:101,1]
    yyy[202:303] = yy[0:101,2]
    yyy[303:404] = yy[0:101,3]
    return [xxx,yyy]