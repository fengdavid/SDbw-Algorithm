
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:14:48 2016

@author: Shichen
"""




import time
import numpy as np
import pandas as pd
import xgboost as xgb
from math import log
from collections import Counter
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation,metrics
from sklearn.grid_search import GridSearchCV
import math

wir='D:/'

test=pd.read_csv(wir+'df_cluster2.csv')
center =pd.read_csv(wir+'df_center2.csv')
#center=center.drop(['Cluster'])
'''
test={'a':[1,2,3,4,5],'b':[4,2,3,4,1],'c':[3,1,4,5,2],'Cluster':[1,1,1,2,2]}
test1={'a':[3,1,4,7,0],'b':[1,2,3,4,5],'c':[9,8,7,6,1],'Cluster':[1,1,1,2,2]}

center={'a':[5,3],'b':[5,1],'c':[5,2],'Cluster':[1,2]}
test=pd.DataFrame(test)
center=pd.DataFrame(center)
test1=pd.DataFrame(test1)
'''
class S_Dbw:

    def __init__(self,clusters,centerOfcluster):
        self.clusters=clusters
        self.centerOfcluster=centerOfcluster
        self.diff=self.centerOfcluster.shape[0]
        self.sumt=0
        self.d=self.dev()
        self.des=pd.DataFrame()
        #self.DaS=self.DataScat()

  
    def dev(self):            
        self.sumt=self.centerOfcluster.apply(lambda y:((self.clusters[self.clusters.Cluster==y.Cluster].apply(lambda x: (((x.drop(['Cluster'])-y.drop(['Cluster']))**2).sum()),axis=1).sum()lf.clusters[self.clusters.Cluster==y.Cluster].shape[0]))**(0.5),axis=1).sum()  
        return self.sumtlf.diff
        
        
    def density(self):
        self.des = (self.centerOfcluster.apply(lambda y:(self.clusters[self.clusters.Cluster==y.Cluster].apply(lambda x: 1 if ((x.drop(['Cluster'])-y.drop(['Cluster']))**2).sum()**0.5<self.d else 0,axis=1).sum()),axis=1))
        return self.des.tolist() 
        
    
    def combine2clusters(self,vx,vy,centreX,centreY):
        middle=(centreX+centreY)/2  
        temp=vx.apply(lambda x: 1 if ((x-middle)**2).sum()**0.5<self.d else 0,axis=1).sum()
        temp=temp+vy.apply(lambda x: 1 if ((x-middle)**2).sum()**0.5<self.d else 0,axis=1).sum() 
        return temp

    def Densbw(self):
        t=self.density()
        temp=self.centerOfcluster.apply(lambda x:(self.centerOfcluster.apply(lambda y: self.combine2clusters(self.clusters[self.clusters.Cluster==x.Cluster].drop('Cluster',axis=1),self.clusters[self.clusters.Cluster==y.Cluster].drop('Cluster',axis=1),x.drop('Cluster'),y.drop('Cluster'))/max(t[int(x.Cluster-1)],t[int(y.Cluster-1)]) if x.Cluster!=y.Cluster else 0,axis=1)).sum(),axis=1).sum()
        return temp/(pd.DataFrame(t).shape[0]*(pd.DataFrame(t).shape[0]-1))
    
    def DataScat(self):
        
        std=((self.clusters-self.clusters.mean())**2).sum()lf.clusters.shape[0]
        std=std.drop('Cluster')
        S=(std**2).sum()**0.5
        return S
        
    
    def Scat(self):
        
        V=self.centerOfcluster.apply(lambda x: ((self.clusters[self.clusters.Cluster==x.Cluster]-self.clusters[self.clusters.Cluster==x.Cluster].mean())**2).sum()lf.clusters[self.clusters.Cluster==x.Cluster].shape[0],axis=1)
        V=V.drop('Cluster',axis=1)
        V=V.apply(lambda x: (x**2).sum()**0.5,axis=1)
        r=(Vlf.DataScat()).sum()lf.centerOfcluster.shape[0]
        return r
        
    def SDbw(self):
        return self.DataScat()+self.Densbw()
    
a=S_Dbw(test,center)
p=a.Scat()    

