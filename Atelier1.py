# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:29:38 2021

@author: notta
"""
#EXERCICE 1

def salaire():
    '''calcule le salaire mensuel d'un employe en fonction du salaire horaire et du nombre d'heures travailléés'''
    SALAIRE_H=10 #salaire horaire float
    heures=210 #heures de travail int
    h_sup_50=0 #heures sups a 50% int
    h_sup_25=0 #heures sups a 25% int
    h_normal=heures #heures au taux normal int
    if heures>160:
        h_sup_25=heures-160 #maj heures sups a 25%
        h_normal=160
        if heures>200:
            h_sup_50=heures-200 #maj heures sup a 25%
            h_sup_25=heures=40 #maj heures sup a 50%
    salaire=(h_normal*SALAIRE_H)+(h_sup_25*SALAIRE_H*1.25)+(h_sup_50*SALAIRE_H*1.5)
    return salaire # float

#print(salaire())

#EXERCICE 2

def caracteres():
    '''determine si un caractere est en majuscule, minuscule, ou un caractere special'''
    caractere='Z' #char
    code=ord(caractere) #int
    res='caractere special' #string
    if code>47 and code<58:
        res="chiffre"
    if code>64 and code<91:
        res="majuscule"
    if code>96 and code<123:
        res="minuscule"
    return res
  
#print(caracteres())

#EXERCIE 3

def impots():
    '''determine si une personne est imosable ou non, base sur l age et le sexe'''
    sexe='f' #char m=homme, f=femme
    age=65 #int
    imposable=False #booleen
    if sexe=='m' and age>20:
        imposable=True
    elif sexe=='f'and age>=18 and age<=35:
        imposable=True
    return(imposable)

#print(impots())

#EXERCICE 4

def reprographie():
    '''retourne la facture totale des photocopies'''
    x=int(input("nombre de photocopies: ")) #nb de photocopies int
    copies_8=0 #nb de copies a 8 centimes int
    copies_9=0 #nb de copies a 9 centimes int
    copies_10=x #nb de copies a 10 centimes int
    if x>10:
        copies_9=x-10
        copies_10=10
    if x>30:
        copies_8=x-30
        copies_9=20
    facture=copies_10*0.1 + copies_9*0.09 + copies_8*0.08
    return facture

#print("total: {}€".format(reprographie()))

#EXERCICE 5

def portuaire():
    '''calcule les frais portuaires d'un voilier'''
    ###constantes
    TAXES_TAB=[100,150,250]
    ####saisie des informations#####
    nom=input("nom du bateau: ") #str
    longueur=float(input("longueur du bateau: ")) #float
    categorie=int(input("categorie (1,2 ou 3): ")) #int
    ####cout mensuel d'une place au port######
    res=100
    if longueur>=5:
        res=200
        if longueur>10:
            res=400
            if longueur>12:
                res=600
    cout_m=res #cout mensuel
    ####taxe speciale annuelle#####
    taxe= TAXES_TAB[categorie-1] #categorie 1 => indice 0 => 100€
    ####cout annuel#####
    cout_a=cout_m*12 + taxe
    print("le cout annuel d'une place au port pour le voilier {} est de {} euros".format(nom, cout_a))
    
#portuaire()

#EXERCICE 6

def concessionnaire():
    '''calcule les frais d'exploitation d'une voiture'''
    CARBURANT='D' #str D pour diesel, E pour essence
    CYLINDREE=2000 #int cylindree de la voiture
    KM=10000 #int km parcourus en un an 
    P_CARB=1 #float prix du carburant
    conso=8 #float consommation en l/100km
    res=0
    if CARBURANT=='E':
        if CYLINDREE>2000:
            conso=10
        res=(KM/100)*conso*P_CARB*1.5
    else:
        res=(KM/100)*conso*P_CARB*1.7
    return res
        
#print(concessionnaire())
        
#EXERCICE 7

def elections():
    '''determine si le candidat est elu, battu ou en ballotage'''
    #saisie des candidats
    candidats=[] #float, liste des scores
    etat='en ballotage defavorable'
    maxi=0 #score maximal parmis les candidats
    #saisie des candidats
    for i in range(0,4):
        x=-1
        while x<0: #verifie que le score est positif
            x=int(input("candidat {}:".format(i+1)))
        candidats.append(x)
    #selection du premier candidat
    candidat=candidats[0]
    #recherche du score maximum
    for j in range(0,4):
        if candidats[j]>maxi:
            maxi=candidats[j]
    if maxi>=50: #pas de deuxieme tour
        if candidat>=50:
            etat='elu'
        else:
            etat='elimine'
    else: #deuxieme tour possible si score minimum atteint
        if candidat<12.5:
            etat='elimine'
        else:
            if candidat==maxi:
               etat='en ballotage favorable'
    print("le candidat est {}".format(etat))
               
            
#elections()

#EXERCICE 8

def assurance():
    '''calcule le tarif du client'''
    #saisie des donnees
    age=int(input("age: "))
    permis=int(input("anciennete du permis: ") )
    nb_accidents=int(input("nombre d'accidents responsable: ")) #nombres d accidents
    anciennete=int(input("anciennete dans la compagnie: "))
    tab_tarifs=["refus","rouge","orange","vert","bleu"] #score=0 => refus
    score=3 #initialisation du score (plus haute valeur possible sans bonus)
    if anciennete>1:
        score+=1
    if age<25:
        score-=1
    if permis<2:
        score-=1 
    if score-nb_accidents>0:
        score-=nb_accidents #soustraction = score - nb_accidents
    else:
        score=0
    return tab_tarifs[score]

#print(assurance())
    
    
        
    

        
    
    

