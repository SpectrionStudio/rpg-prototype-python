#Code jeu vidéo Elyas , Cléo , Kylian 

#Points importants pour le code et différentes catégories de codage. 

'''
Catégories : 



- Menu dont : 
Objets 
Statistiques des personnages : 
hp
force
Spectrion
vitesse
chance
défense
etat

Présentation des personnages 
possibilité de changement de personnages 
équipements 

- Système de commerce 

- Combat :
Parer 
Esquiver
Attaque spéciale

- Déplacement banal :
droite 
gauche
haut
bas
saut

- intéraction :
Objet
Personnage

'''

class personnages :
    def __init__(self): 
         self.personnages = {
            "katsu": {"hp": 140 , "etat":'vivant' , "force":75 , "defense":85 , "spectrion":35 , "chance":65 , "vitesse":105},
            "raiju": {"hp": 125, "etat":'vivant', "force":60 , "defense":75 , "spectrion":50 , "chance":110 , "vitesse":115}, 
            "satoshi": {"hp": 155, "etat":'vivant', "force":80 , "defense":70 , "spectrion":20 , "chance":60 , "vitesse":95},
            "riyo": {"hp": 175, "etat":'vivant', "force":85 , "defense":90 , "spectrion":65 , "chance":80 , "vitesse":75},
            "kaen": {"hp": 220, "etat":'vivant', "force":85 , "defense":110 , "spectrion":50 , "chance":60 , "vitesse":80},
            "yoshiteru": {"hp": 190, "etat":'vivant', "force":105 , "defense":85 , "spectrion":55 , "chance":65 , "vitesse":75},
            "sumiye": {"hp": 115, "etat":'vivant', "force":50 , "defense":65 , "spectrion":120 , "chance":55 , "vitesse":80},
            "kana": {"hp": 130, "etat":'vivant', "force":90 , "defense":70 , "spectrion":25 , "chance":75 , "vitesse":100},
            "takeshi": {"hp": 135, "etat":'vivant', "force":75 , "defense":100 , "spectrion":80 , "chance":70 , "vitesse":95},
            "shun": {"hp": 155, "etat":'vivant', "force":80 , "defense":95 , "spectrion":110 , "chance":45 , "vitesse":130},
            "osamu": {"hp": 2500, "etat":'vivant'},
            "sayuri": {"hp": 1250, "etat":'vivant'},
            "tsuneo": {"hp": 180, "etat":'vivant'},
            "yoshio": {"hp": 140, "etat":'vivant'},
        }
    def etat_personnage(self , nom) :
        if  nom in self.personnages : 
            perso = self.personnages[nom]
            hp = perso["hp"]
            if hp <= 0 :
                perso["etat"] = "mort"
                print(f"{nom.capitalize()} est maintenant mort")
    
    def afficher_stats(self , nom): 
     if nom in self.personnages :
         perso = self.personnages[nom] 
         print(f"\nStats de {nom.capitalize()} :")
         print(f" - HP : {perso['hp']}")
         print(f" - Force : {perso['force']}")
         print(f" - Defense : {perso['defense']}")
         print(f" - Vitesse : {perso['vitesse']}")
         print(f" - Spectrion : {perso['spectrion']}")
         print(f" - Chance : {perso['chance']}")
         
class item : 
    def __init__(self):
        self.item = {
            "Fiole" : {"spectrion" : 15},
            "Super Fiole" : {"spectrion" : 30},
            "Méga Fiole" : {"spectrion" : 50},
            "Anti Poison" : {"prix": 20}

        }



    
jeu = personnages()
jeu.afficher_stats("raiju")


        