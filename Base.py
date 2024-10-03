import icontract
import pint 
ureg=pint.UnitRegistry()

class Base:
    def __init__(self,id,localisation):
        self.id=id
        self.localisation=localisation
        self.drones=[]

    @icontract.snapshot(lambda self: self.drones)
    @icontract.ensure(lambda OLD, self: len(OLD) + 1 == len(self.drones))
    def ajouter_drones(self,drone):
        self.drones.append(drone)
        drone.base=self
