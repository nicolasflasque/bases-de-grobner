def precede(u,v):
    prec=True
    
    lu,lv=len(u),len(v)
    
    if(lu!=lv):
        prec=False
    else:
        cpt=0
        while(cpt < len(u) and u[cpt]<=v[cpt]):
            cpt=cpt+1
            
        if (cpt<len(u)):
            prec=False
    
    return prec

def lexorder(u,v):
    order=0
    cpt=0
    
    while (cpt<len(u) and u[cpt]==v[cpt]):
        cpt=cpt+1
    
    if (cpt < len(u)):
        if (u[cpt]<v[cpt]):
            order=-1
        else:
            order=1
    
    return order
    
    
def lexinf(u,v):
    return lexorder(u,v)==-1
    
def lexsup(u,v):
    return lexorder(u,v)==1
    
def lexequ(u,v):
    return lexorder(u,v)==0

def positif(u):
    nulvec=[0]*len(u)
    
    return precede(nulvec,u)

def isnull(u):
    nulvec=[0]*len(u)
    
    return precede(u,nulvec) and precede(nulvec,u)

def star(u):
    star=[0]*len(u)
    cpt=0
    
    while(cpt < len(u) and u[cpt]==0):
        cpt=cpt+1
    
    if (cpt < len(u)):
        signe=2*(u[cpt]>0)-1
        for i in range(0,len(u)):
            star[i]=signe*u[i]

    return star
    
def plus(u):
    uplus=list(u)
    
    for i in range(0,len(u)):
        if(u[i]<0):
            uplus[i]=0
    
    return uplus

def sub(u,v):
    return [u[i]-v[i] for i in range(0,len(u))]

def reduce(u,v):
 #  print('reduction de',u,'par',v)
    uet=star(u)
    uetp=plus(uet)
    vp=plus(v)
    neg=(u!=uet)
    lc=[]
    if (precede(vp,uetp)):
        for i in range(0,len(vp)):
            if (vp[i]>0):
                coef=uetp[i]//vp[i]
                lc=lc+[coef]
            
        beta=min(lc)
            
        if (neg==True) :
            beta = -1*beta
        
        reduit=[u[i]-beta*v[i] for i in range(0,len(u))]
        reduced=True
#       print('reste :',reduit,'avec quotient=',beta)
    else:
#       print('pas reductible')
        reduced=False
        reduit=u
    
    return reduced,reduit
    
def reducefromset(u,S):
    reduced=False
    for v in S:
        red,u=reduce(u,v)
        reduced=reduced or red
    return reduced,u
    
def buchberger(S):
    G=[]
    for i in range(0,len(S)):
        for j in range(0,len(S)):
            if (i!=j):
                G=G+[[S[i],S[j]]]
    
    while(len(G)>0):
        couple=G.pop(0)
#       print('couple ',couple[0],'|',couple[1])
        u=sub(couple[0],couple[1])
        r,w=reducefromset(u,S)
        
        if (r==True) and isnull(w)==False and (star(w) not in S):
            for v in S:
                G.append([v,star(w)])
            S.append(star(w))
        
    return S
    
def testbuch():
    v1=[1,2,-1,0,0]
    v2=[3,4,0,-1,0]
    v3=[2,5,0,0,-1]
    S=[v1,v2,v3]
    base=buchberger(S)
    print(base)
    b=[12,19,0,0,0]
    r,x=reducefromset(b,base)
    print('reduction de  :',b,'=',x)
    return