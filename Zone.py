import icontract
import pint 
ureg=pint.UnitRegistry()


zones=[]

class Zone:
    def __init__(self,id,coordonnee,nb_pilules):
        self.id=id
        self.coordonnee=coordonnee
        self.nb_pilules=nb_pilules
        self.priorité=0
    
    def calcul_priorite(self,):
        pass        #self.nb_pilules, zones

    def ajouter_zone(self):
        zones.append(self)
    
