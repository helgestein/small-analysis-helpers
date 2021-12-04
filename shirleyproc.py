def steshirproc(y,iterations=100):
  #calculates the shirley background like I belive it to be correct
  y_ = y#np.flipud(y)
    le = len(y_)
    a,b = y_[0],y_[-1]
    u = np.linspace(a,a,le)
    for k in range(iterations):
        for i in range(le):
            p = np.trapz(y_[0:i]-u[0:i])
            q = np.trapz(y_[i:]-u[i:])
            u[i] = (a-b)*q/(p+q)+b
    return u
