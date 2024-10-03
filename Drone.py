import icontract
import pint 
ureg=pint.UnitRegistry()

class Drone:
    def __init__(self,id,charge_medicament:int,autonomie:int,position:str):
        self.id=id
        self.charge_medicament=charge_medicament
        self.autonomie=autonomie
        self.position=position
        self.operateur=None
        self.base=None
        self.chemin=[]
    
    def effectuer_mission():
        pass

    def mettreajourposition():
        pass

    def calcul_chemin_optimal():
        pass

