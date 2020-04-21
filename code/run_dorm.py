# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 03:09:55 2020

@author: hexie
"""


from main1 import main1
from data_loader import load_dorm
from utils import write_single, write_double
from utils import read_single_true, read_double_true
from utils import read_multiple_true, write_multiple
from plots import scatter_plot
#load data
data1, layers1, pair1, allcomb1, groups1 = load_dorm()

#average over a number
N = 1 


#loop through different ks
KK = range(3,4)

for k in KK:

    dsa=[]
    dda=[]
    daa=[]
    
    for i in range(N):
    
        dorm_single_auc = []
        dorm_double_auc = []
        dorm_all_auc = []
        
        for la in layers1:
            write_single(data1, la)
            main1(la,1,k)
            fpr, tpr, tmp = read_single_true(data1, la,k)
            dorm_single_auc.append(tmp)
        for pa in pair1:
            name = str(pa[0])+"_"+str(pa[1])
            write_double(data1, pa)
            main1(name,2, k)
            fpr, tpr, tmp = read_double_true(data1, pa, k)
            dorm_double_auc.append(tmp)
        for al in allcomb1:
            name = ""
            for j in al :
                name = name + str(j)+"_"
            write_multiple(data1, al)
            main1(name,8,k)
            fpr, tpr, tmp = read_multiple_true(data1, al, k)
            dorm_all_auc.append(tmp)
        
        dsa.append(dorm_single_auc)
        dda.append(dorm_double_auc)
        daa.append(dorm_all_auc)
    
    if N==1:
        dsa1=dsa[0]
        dda1=dda[0]
        daa1=daa[0]
    else:   
        dsa1= [sum(x)/float(N) for x in zip(*dsa)]
        dda1= [sum(x)/float(N) for x in zip(*dda)]
        daa1= [sum(x)/float(N) for x in zip(*daa)]
    
    sing1dict = dict(zip(layers1,dsa1))
    pair1 = [tuple(l) for l in pair1]
    pair1dict = dict(zip(pair1, dda1))
    all1 = [x[0] for x in allcomb1 ]
    all1dict = dict(zip(all1, daa1))
    
    scatter_plot("stanford"+"_K"+str(k)+"_N"+str(N),
                 groups1, pair1dict,dsa1, daa1, layers1, sing1dict, all1dict,
                 plotall=False, ordered1= True, ordered2= False)
    scatter_plot("stanford"+"_K"+str(k)+"_N"+str(N),
                 groups1, pair1dict,dsa1, daa1, layers1, sing1dict, all1dict,
                 plotall=True, ordered1= True, ordered2= False)
    scatter_plot("stanford"+"_K"+str(k)+"_N"+str(N),
                 groups1, pair1dict,dsa1, daa1, layers1, sing1dict, all1dict,
                 plotall=True, ordered1= False, ordered2= True)