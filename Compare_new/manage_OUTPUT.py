import time
import os
import shutil
import commands
import sys

def process_args(args,parms):
    print(args)

    for ss in args:
        addname=None
        if (':' in ss):
            bb=str.split(ss,':')
            addname=str.strip(bb[0],' ')
            s=bb[1]
            if (addname in parms):
                pp=parms[addname]
                addname=None
            else:
                pp={}
        else:
            s=ss
            pp=parms
        if ('=' in s):
            aa=str.split(s,'=')
            name=str.strip(aa[0],' ')
            value=str.strip(aa[1],' ')
            try:
                v=int(value)
            except ValueError:
                try:
                    v=float(value)
                except:
                    v=value
            if (v=='True'):
                pp[name]=True
            elif (v=='False'):
                pp[name]=False
            else:
                pp[name]=v
        if (addname is not None):
            parms[addname]=pp
    print(parms)
    return(parms)

def print_OUTPUT(name='OUTPUT'):

    ss=str.split(name,'-')
    OO='AOUT'
    if (len(ss)>1):
        if (ss[1] != ''):
            OO='_'+ss[1]+'/AOUT'

    dirs=os.listdir(OO)
    cc=commands.getoutput('grep XXX ' + name + '.txt')

    nn=str.split(cc,' ')
    nna=nn[1]
    nnb=str.split(nna,'/')
    if (len(nnb)==2):
        nnn=nnb[1]
    else:
        nnn=nnb[0]
    ss=nnn
    t=0
    for dd in dirs:
        if ss in dd:
            t+=1
    #sys.stdout.flush()
    #time.sleep(10)
    shutil.copyfile(name+'.txt',OO+'/'+name+'_'+str(t)+'.txt')

def plot_OUTPUT(name='OUTPUT'):
    import commands
    import numpy as np
    import pylab as py
    py.ion()
    bt=np.fromstring(commands.getoutput('grep Train ' + name + '.txt | grep acc | cut -d":" -f2'),sep='\n\t\t\t')
    bv=np.fromstring(commands.getoutput('grep Val ' + name + '.txt | grep acc | cut -d":" -f2'),sep='\n\t\t\t')
    ss='grep aggegate ' + name + '.txt | cut -d"," -f2 | cut -d")" -f1'
    atest=np.fromstring(commands.getoutput(ss),sep='\n\t\t\t')
    if (type(atest) is np.ndarray and atest !=[] ):
        atest=atest[-1]
    ss='grep Post-train ' + name + '.txt | grep acc | cut -d":" -f2'
    atrain=np.fromstring(commands.getoutput(ss),sep='\n\t\t\t')
    if (type(atrain) is np.ndarray and atrain != []):
        atrain=atrain[-1]
    print(atest,atrain)

    print(len(bt))
    py.plot(bt,label='train')
    py.plot(bv,label='val')
    py.plot(len(bt)-2, atest, 'go', markersize=4)
    py.plot(len(bt)-2, atrain, 'bo', markersize=4)
    py.legend(loc=4)
    #py.show()