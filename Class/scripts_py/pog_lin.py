import os
import sys
import numpy as np

pfile='/pog_lin'
nt=str(50000)
update='sgd'
eta=str(10)
ne=str(200)
use_existing='True'
for j in np.arange(0,1,1):

    seed=np.random.randint(0,200000)
    sd=' seed='+str(seed)+' '
    # ss='python runber.py start_class.py net=_pars' + pfile +' hinge=1. num_train='+nt+' eta_init='+eta+ \
    #     ' eta_current='+eta+' batch_size=100 num_epochs='+ne+' update='+update+ \
    #     ' force_global_prob=[1.,-1.]'+sd+'pog_OUT'+str(j)
    # os.system(ss)
    ss='python runber.py start_class.py net=_pars'+pfile+' output_net=junk hinge=1. num_train='+nt+' use_existing='+use_existing+' eta_init='+eta+ \
       ' eta_current='+eta+' batch_size=100 start=1 mult=1 mod_net=_MODS/mod_pog_s update='+update+' num_epochs='+ne+\
       ' force_global_prob=[1.,1.]'+sd+'pogRs_OUT'+str(j)
    os.system(ss)
    ss='python runber.py start_class.py net=_pars'+pfile+' output_net=junk hinge=1. num_train='+nt+' use_existing='+use_existing+' eta_init='+eta+ \
       ' eta_current='+eta+' batch_size=100 start=1 mult=1 mod_net=_MODS/mod_pog_s update='+update+' num_epochs='+ne+\
       ' force_global_prob=[1.,0]'+sd+'pogRRs_OUT'+str(j)
    os.system(ss)



