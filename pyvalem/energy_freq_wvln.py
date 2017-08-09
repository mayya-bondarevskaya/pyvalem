from .state import State, StateParseError
from pyqn.quantity import Quantity
from pyqn.units import Units
#This module HAS to be run from above the main Pyvalem folder, such that
#this module can also "see" the pyqn directory

class EnergyFreqWvln(State):
    def parse_state(self,state_str):
        self.quantity = Quantity.parse(state_str)
        
    def energy(self, units='J'):
        return self.quantity.convert_units_to(units, force='spec')
    
    def frequency(self, units='s-1'):
        return self.quantity.convert_units_to(units, force='spec')
    
    def wavelength(self, units='m'):
        return self.quantity.convert_units_to(units, force='spec')
    
    @property
    def html(self):
        return self.state_str
