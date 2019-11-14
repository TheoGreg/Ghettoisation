#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:39:42 2019

@author: theophanegregoir
"""
import random 
import numpy as np
import matplotlib.pyplot as plt
import math

#Déclaration des variables 
N_v = 1000
accep_v = 1.0
accep_v_b = 0.4
accep_v_r = 0.4
tab_vert = np.zeros((N_v,2))
N_r = 1000
accep_r = 1
accep_r_b = 0.4
accep_r_v = 0.4
tab_rouge = np.zeros((N_r,2))
N_b = 1000
accep_b = 1.0
accep_b_v = 0.4
accep_b_r = 0.4
tab_bleu = np.zeros((N_b,2))
generations = 10
Rayon = 0.1

#Fonction Satisfaction

def satisfactionVert(k, t_b, t_r, t_v, Rayon):
    
    x_k = t_v[k][0]
    y_k = t_v[k][1]
    test = True 
    
    while test :
        compte_vert = -1 #Prise En Compte Du Point
        compte_rouge = 0
        compte_bleu = 0
        
        #AnalyseVert
        for j in range(len(t_v)):
            distance = math.sqrt((t_v[j][0]-x_k)**2 + (t_v[j][1]-y_k)**2)
            #Test d'appartenance au cercle
            if (distance <= Rayon) :
                compte_vert += 1

        #AnalyseBleu
        for j in range(len(t_b)):
            distance = math.sqrt((t_b[j][0]-x_k)**2 + (t_b[j][1]-y_k)**2)
            #Test d'appartenance au cercle
            if (distance <= Rayon) :
                compte_bleu += 1
        
        #AnalyseRouge
        for j in range(len(t_r)):
            distance = math.sqrt((t_r[j][0]-x_k)**2 + (t_r[j][1]-y_k)**2)
            #Test d'appartenance au cercle
            if (distance <= Rayon) :
                compte_rouge += 1
                
        #Décision de déménagement
        if (compte_rouge + compte_bleu + compte_vert == 0):
            test = False 
        else : 
            if (((float(compte_rouge)/float(compte_rouge + compte_bleu + compte_vert)) < accep_v_r) and ((float(compte_bleu)/float(compte_rouge + compte_bleu + compte_vert)) < accep_v_b)) :
                test = False 
            else : 
                x_k = random.random()
                y_k = random.random()
            
    t_v[k][1] = y_k
    t_v[k][0] = x_k

def satisfactionBleu(k, t_b, t_r, t_v, Rayon):
    
    x_k = t_b[k][0]
    y_k = t_b[k][1]
    test = True 
    
    while test :
        compte_bleu = -1 #Prise En Compte Du Point
        compte_rouge = 0
        compte_vert = 0
        
        #AnalyseVert
        for j in range(len(t_v)):
            distance = math.sqrt((t_v[j][0]-x_k)**2 + (t_v[j][1]-y_k)**2)
            #Test d'appartenance au cercle
            if (distance <= Rayon) :
                compte_vert += 1
                
        #AnalyseBleu
        for j in range(len(t_b)):
            distance = math.sqrt((t_b[j][0]-x_k)**2 + (tab_bleu[j][1]-y_k)**2)
            #Test d'appartenance au cercle
            if (distance <= Rayon) :
                compte_bleu += 1
        
        #AnalyseRouge
        for j in range(len(t_r)):
            distance = math.sqrt((t_r[j][0]-x_k)**2 + (t_r[j][1]-y_k)**2)
            #Test d'appartenance au cercle
            if (distance <= Rayon) :
                compte_rouge += 1
                
        #Décision de déménagement
        if (compte_rouge + compte_bleu + compte_vert == 0):
            test = False 
        else : 
            if (((float(compte_rouge)/float(compte_rouge + compte_bleu + compte_vert)) < accep_b_r) and ((float(compte_vert)/float(compte_rouge + compte_bleu + compte_vert)) < accep_b_v)) :
                test = False 
            else : 
                x_k = random.random()
                y_k = random.random()
            
    t_b[k][1] = y_k
    t_b[k][0] = x_k
    
def satisfactionRouge(k, t_b, t_r, t_v, Rayon):
    
    x_k = t_r[k][0]
    y_k = t_r[k][1]
    test = True 
    
    while test :
        compte_rouge = -1 #Prise En Compte Du Point
        compte_bleu = 0
        compte_vert = 0

        #AnalyseVert
        for j in range(len(t_v)):
            distance = math.sqrt((t_v[j][0]-x_k)**2 + (t_v[j][1]-y_k)**2)
            #Test d'appartenance au cercle
            if (distance <= Rayon) :
                compte_vert += 1
        
        #AnalyseBleu
        for j in range(len(t_b)):
            distance = math.sqrt((t_b[j][0]-x_k)**2 + (tab_bleu[j][1]-y_k)**2)
            #Test d'appartenance au cercle
            if (distance <= Rayon) :
                compte_bleu += 1
        
        #AnalyseRouge
        for j in range(len(t_r)):
            distance = math.sqrt((t_r[j][0]-x_k)**2 + (t_r[j][1]-y_k)**2)
            #Test d'appartenance au cercle
            if (distance <= Rayon) :
                compte_rouge += 1
                
        #Décision de déménagement
        if (compte_rouge + compte_bleu + compte_vert == 0):
            test = False 
        else :
            if (((float(compte_bleu)/float(compte_rouge + compte_bleu + compte_vert)) < accep_r_b) and ((float(compte_vert)/float(compte_rouge + compte_bleu + compte_vert)) < accep_r_v)) :
                test = False 
            else : 
                x_k = random.random()
                y_k = random.random()
            
    t_r[k][1] = y_k
    t_r[k][0] = x_k


#Initialisation des coordonnées
for i in range(N_r):
    tab_rouge[i][0] = random.random()
    tab_rouge[i][1] = random.random()
for i in range(N_b):
    tab_bleu[i][0] = random.random()
    tab_bleu[i][1] = random.random()
for i in range(N_v):
    tab_vert[i][0] = random.random()
    tab_vert[i][1] = random.random()
    
    
#Affichage de départ
fig = plt.figure()
ax = plt.axes()
ax.scatter(tab_rouge[:,0],tab_rouge[:,1], c = 'r')
ax.scatter(tab_bleu[:,0],tab_bleu[:,1], c = 'b')
ax.scatter(tab_vert[:,0],tab_vert[:,1], c = 'g')

    
#Lancement du process
for h in range(generations):
    
    #Passage sur tous les points
    for k in range(max(N_r,N_b,N_v)):
        if (k < N_r) :
            satisfactionRouge(k, tab_bleu, tab_rouge, tab_vert, Rayon)
        if (k < N_b) :
            satisfactionBleu(k, tab_bleu, tab_rouge, tab_vert, Rayon)
        if (k < N_v) :
            satisfactionVert(k, tab_bleu, tab_rouge, tab_vert, Rayon)
    
    #Affichage du tour
    fig = plt.figure()
    ax = plt.axes()
    ax.scatter(tab_rouge[:,0],tab_rouge[:,1], c = 'r')
    ax.scatter(tab_bleu[:,0],tab_bleu[:,1], c = 'b')
    ax.scatter(tab_vert[:,0],tab_vert[:,1], c = 'g')
                
            

