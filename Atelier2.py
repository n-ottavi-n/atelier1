# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:54:44 2021

@author: notta
"""

import random
from math import sqrt
from datetime import date


#EXERCICE 1

def message_imc(imc):
    """renvoie une chaine decrivant l'imc"""
    TAB_IMC=['denutriton ou famine','maigreur','corpulence normale','surpoids','obesite modere','obesite severe','obesite morbide']
    if imc>40:
        etat=6
    elif imc>35:
        etat=5
    elif imc>30:
        etat=4
    elif imc>25:
        etat=3
    elif imc>18.5:
        etat=2
    elif imc>16.5:
        etat=1
    else:
        etat=0
    return TAB_IMC[etat]

def test_message_imc():
    """test de la fonction message_imc avec des valeurs aleatoires"""
    for i in range(10):
        imc=random.randint(10,50)
        print(imc, message_imc(imc))

#test_message_imc()

#EXERCICE 2

def est_bissextile(annee):
    """renvoie True si l'annee est bissextile
    inputs:
        annee: int l'annee a tester
    outputs:
        boolean: true si l'annee est bissextile, False sinon"""
    return (annee%4==0 and annee%100!=0) or annee%400==0 

def test_est_bissextile():
    """test de la fonction est_bissextile()
    output:
        String, format: aaaa True/False"""
    annee=2021
    for i in range(20):
        print(annee,est_bissextile(annee))
        annee+=1
        
#test_est_bissextile()

#EXERCICE 3

def discriminant(a,b,c):
    """calcule le delta en fonction de a,b,c
    inputs: a,b,c: int
    output: float: discriminant du polynome"""
    return (b**2)-4*a*c

def racine_unique(a,b):
    """retourne la racine dans le cas delta=0
    inputs: a,b: int
    output: float: racine du polynome"""
    return -b/(2*a)

def racine_double(a,b,delta,num):
    """retourne une des racines au choix
    inputs:
        a,b,num: int
        delta: float
    outputs:
        float: une des racines du polynome
        Boolean: False si num !=1 ou 2"""
    if num==1: #premiere racine
        return(-b+sqrt(delta))/(2*a)
    elif num==2: #deuxieme racine
        return(-b-sqrt(delta))/(2*a)
    else:
        return False
    
def str_equation(a,b,c):
    """affiche une equation du second degree sous forme de string"""
    #tests sur le premier terme
    if a<0:
        if a==-1: #n'affiche pas le -1
            str1='-x^2'
        else: #cas general negatif
            str1='-'+str(-a)+'x^2'
    else:
        if a==1: #n'affiche pas le 1
            str1='x^2'
        else: #cas general positif
            str1=str(a)+"x^2"
    #tests sur le second terme
    if b<0:
        if b==-1: #n'affiche pas le 1
            str2='-x'
        else: #affiche -bx au lieu de +-bx
            str2='-'+str(-b)+'x'
    elif b==0: #n'affiche pas le second terme
        str2=''
    elif b==1: #n'affiche pas le 1
        str2='+x'
    else:
        str2='+'+str(b)+'x' #cas general positif
    #tests sur le troisieme terme
    if c<0: #affiche -c au lieu de +-c
        str3='-'+str(-c)
    elif c==0: #n'affiche pas le troisieme terme
        str3=''
    else: #cas general positif
        str3='+'+str(c)
    return str1+str2+str3+"=0"
        

#print(str_equation(-3, -2, 4))

def solution_equation(a,b,c):
    """donne les racines de l'equation si elles existent"""
    msg="solution de l'equation "+ str_equation(a, b, c)
    delta=discriminant(a,b,c)
    if delta>0:
        res='Deux racines:\n x1: {} \n x2: {}'.format(racine_double(a, b, delta, 1),racine_double(a, b, delta, 2))        
    elif delta==0:
        res='Racine unique: x= {}'.format(racine_unique(a, b))
    else:
        res="Pas de racine reelle"
    print(msg)
    return res

#print(solution_equation(0,1,1))

def equation(a,b,c):
    """appelle solution_equation()"""
    print(solution_equation(a, b, c))
    

def test_equation():
    """test de la finction equation"""
    for i in range(10):
        a=random.randint(-10, 10)
        b=random.randint(-10, 10)
        c=random.randint(-10, 10)
        if a!=0:
            equation(a,b,c)
            print('#########################')
            
#test_equation()   

#EXERCICE4

def date_est_valide(jour,mois,annee):
    res=False
    if jour>0 and jour<32 and mois>0 and mois<13 and annee>0: 
        #test des mois
        if mois<8:#cas de janvier a juillet inclus
            if mois==2: #cas fevrier
                    if est_bissextile(annee):
                        if jour<30:
                            res=True
                    elif jour<29:
                        res=True
                        
            elif mois%2==0:#mois paire=30 jours (vrai jusqu'a juillet inclus)
                if jour<31:
                    res=True            
            else: #mois impaire
                res=True
        
        else:#cas de aout a decembre
            if mois%2==0:#mois paires=31jours
                res=True
            elif jour<31: #mois impaires                
                res=True
    return res
  
    
    
#print(date_est_valide(29,2,2021))       

def saisie_date_naissance():
    """saisie au clavier d'une date de naissance"""
    jour=int(input("jour: "))
    mois=int(input("mois: "))    
    annee=int(input("annee (aaaa):"))
    return date(annee,mois,jour)

def age(date_n):
    """renvoie l'age de la personne"""
    annee_n=date_n.year #annee de naissance
    mois_n=date_n.month #mois de naissance
    jour_n=date_n.day #jour de naissance
    aujourdhui=date_n.today()#date d'aujourd'hui
    
    annee=aujourdhui.year#annee courante
    mois=aujourdhui.month#mois courant
    jour=aujourdhui.day#jour courant
    
    age=annee-annee_n
    if mois<mois_n:
        age-=1
    elif mois==mois_n:
        if jour<jour_n:
            age-=1
        elif jour==jour_n:
            print("joyeux anniversaire")
    return age

def est_majeur(date_naissance):
    """retourne True si la personne est majeure"""
    return age(date_naissance)>=18

def test_acces():
    """donne l'acces aux majeurs uniquement"""
    print("entrez votre date de naissance")
    date_n=saisie_date_naissance()
    age_1=age(date_n)
    msg="Desole vous avez {} ans, acces interdit".format(age_1)
    if est_majeur(date_n):
        msg="Bonjour, vous avez {} ans, acces autorise".format(age_1)            
    print(msg)

#test_acces()