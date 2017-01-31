from .state import State, StateParseError
from pyqn.pyqn.quantity import Quantity
from pyqn.pyqn.units import Units
from pyqn.pyqn.dimensions import Dimensions, d_energy, d_length, d_frequency, d_quantity
#This module HAS to be run from above the main Pyvalem folder, such that
#this module can also "see" the pyqn directory

class EnergyFreqWvln(State):
    def parse_state(self,state_str):
        self.state_str = state_str
        state_str_split = state_str.split()
        self.quantity = Quantity(value = float(state_str_split[0]),units = state_str_split[1])
        
    def energy(self,units='J'):
        return self.quantity.convert_units_to(units,force='spec')
    
    def frequency(self,units='s-1'):
        return self.quantity.convert_units_to(units,force='spec')
    
    def wavelength(self,units='m'):
        return self.quantity.convert_units_to(units,force='spec')
    
    @property
    def html(self):
        return self.state_str