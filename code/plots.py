# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:32:58 2020

@author: hexie
"""
import matplotlib.pyplot as plt
import numpy as np
def scatter_plot(name, groups, pair_dict, singlep, allp, layers, 
                 sing1dict, all1dict, plotall, ordered1, ordered2):
    maxx=[]
    minx=[]
    
    if plotall == False:
        if ordered1 ==True:
            inv_sin = {v: k for k, v in sing1dict.iteritems()}
            neworder = inv_sin.keys()
            neworder.sort()
            layers= [inv_sin[x] for x in neworder]
            singlep = [sing1dict[y] for y in layers] 
            allp = [all1dict[z] for z in layers ]
        
        if ordered2 ==True:
            inv_all = {v: k for k, v in all1dict.iteritems()}
            neworder = inv_all.keys()
            neworder.sort()
            layers= [inv_all[x] for x in neworder]
            singlep = [sing1dict[y] for y in layers] 
            allp = [all1dict[z] for z in layers ]
        
        
        
        
        for x in layers:
            groupID = groups[x]
            tmp = {key: pair_dict[key] for key in pair_dict.keys() if key[0]==x}
            maxtmp = {key: tmp[key] for key in tmp.keys() if groups[key[1]]==groupID}
            mintmp = {key: tmp[key] for key in tmp.keys() if groups[key[1]]!=groupID}
            maxx.append(np.mean(maxtmp.values()))
            minx.append(np.mean(mintmp.values()))
        
        fig=plt.figure(tight_layout=True)
        ax=fig.add_axes([0,0,1,1])
        rr = ax.scatter(layers, singlep, color='r', s=50, marker='^')
        gg = ax.scatter(layers, allp, color='g', s=50, marker='^')
        bb = ax.scatter(layers, maxx, color='b', s=25, marker='o')
        yy = ax.scatter(layers, minx, color='y', s=25, marker='o')
        
        plt.legend((rr, gg, bb, yy),
                   ('single', 'all', 'similar', 'notsimilar'),
                   scatterpoints=1,
                   loc='lower right',
                   ncol=3,
                   fontsize=8)
        
        plt.xticks(rotation=90)
        #ax.xaxis.label.set_rotation(90)
        ax.set_xlabel('layer')
        ax.set_ylabel('AUC')
        ax.set_title(str(name))
    
        if ordered1 == True:
            path =r"C:\Users\hexie\Desktop\MURI_LINK\result\scatter\\"
            plt.savefig(path + str(name)+"_order1" + ".png",bbox_inches="tight")
            plt.show()               
        if ordered2 == True:
            path =r"C:\Users\hexie\Desktop\MURI_LINK\result\scatter\\"
            plt.savefig(path + str(name)+"_order2" + ".png",bbox_inches="tight")
            plt.show()
        if ordered1 == False and ordered2 == False:
            path =r"C:\Users\hexie\Desktop\MURI_LINK\result\scatter\\"
            plt.savefig(path + str(name)+"_order2" + ".png",bbox_inches="tight")
            plt.show()

    if plotall == True:
        
        if ordered1 ==True:
            inv_sin = {v: k for k, v in sing1dict.iteritems()}
            neworder = inv_sin.keys()
            neworder.sort()
            layers= [inv_sin[x] for x in neworder]
            singlep = [sing1dict[y] for y in layers] 
            allp = [all1dict[z] for z in layers ]
        
        if ordered2 ==True:
            inv_all = {v: k for k, v in all1dict.iteritems()}
            neworder = inv_all.keys()
            neworder.sort()
            layers= [inv_all[x] for x in neworder]
            singlep = [sing1dict[y] for y in layers] 
            allp = [all1dict[z] for z in layers ]
        
        
        fig=plt.figure(tight_layout=True)
        ax=fig.add_axes([0,0,1,1])
        rr = ax.scatter(layers, singlep, color='r', s=50, marker='^')
        gg = ax.scatter(layers, allp, color='g', s=50, marker='^')
        for x in layers:
            groupID = groups[x]
            tmp = {key: pair_dict[key] for key in pair_dict.keys() if key[0]==x}
            maxtmp = {key: tmp[key] for key in tmp.keys() if groups[key[1]]==groupID}
            mintmp = {key: tmp[key] for key in tmp.keys() if groups[key[1]]!=groupID}
            
            list_max= [x]*len(maxtmp.values())
            list_min= [x]*len(mintmp.values())
            bb = ax.scatter(list_max, maxtmp.values(), color='b', s=25, marker='o')
            yy = ax.scatter(list_min, mintmp.values(), color='y', s=25, marker='o')
        
        plt.legend((rr, gg, bb, yy),
                   ('single', 'all', 'similar', 'notsimilar'),
                   scatterpoints=1,
                   loc='lower right',
                   ncol=3,
                   fontsize=8)
        plt.xticks(rotation=90)
        #ax.xaxis.label.set_rotation(90)
        ax.set_xlabel('layer')
        ax.set_ylabel('AUC')
        ax.set_title(str(name))
        
        if ordered1 == True:
            path =r"C:\Users\hexie\Desktop\MURI_LINK\result\scatter\\"
            plt.savefig(path + str(name)+"_all"+"_order1" + ".png",bbox_inches="tight")
            plt.show()               
        if ordered2 == True:
            path =r"C:\Users\hexie\Desktop\MURI_LINK\result\scatter\\"
            plt.savefig(path + str(name)+"_all"+"_order2" + ".png",bbox_inches="tight")
            plt.show()
        if ordered1 == False and ordered2 == False:
            path =r"C:\Users\hexie\Desktop\MURI_LINK\result\scatter\\"
            plt.savefig(path + str(name)+"_all"+"_order2" + ".png",bbox_inches="tight")
            plt.show()
