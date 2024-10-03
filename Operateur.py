import icontract
import pint 
ureg=pint.UnitRegistry()

class Operateur:
    def __init__(self,id:int,basedepart):
        self.id=id
        self.basedepart=basedepart
        self.drones=[]

    def enregistrer_operateur():
        pass
    
    @icontract.snapshot(lambda self: self.drones)
    @icontract.ensure(lambda OLD, self: len(OLD) + 1 == len(self.drones))
    def ajouter_drones(self,drone):
        self.drones.append(drone)
        drone.operateur=self

    def enregistrer_mission():
        pass
