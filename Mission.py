import icontract
import pint 
ureg=pint.UnitRegistry()


class Mission:
    def __init__(self,id:int,zone,qte_pilules:int,etat,datedebut:str,datefin:str):
        self.id=id
        self.zone=zone
        self.qte_pilules=qte_pilules
        self.etat=etat
        self.datedebut=datedebut
        self.datefin=datefin
        self.drones=[]

    def assigner_drones(drone):
        pass

    def mettre_a_jour_etat(etat):
        pass

    def prevenir_autorite():
        pass
