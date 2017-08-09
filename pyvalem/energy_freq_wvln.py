from .state import State, StateParseError
from pyqn.pyqn.quantity import Quantity
from pyqn.pyqn.units import Units
from pyqn.pyqn.dimensions import d_energy, d_frequency, d_length
#This module HAS to be run from above the main Pyvalem folder, such that
#this module can also "see" the pyqn directory

class EnergyFreqWvlnError(Exception):
    def __init__(self, error_str):
        self.error_str = error_str
    def __str__(self):
        return self.error_str

class EnergyFreqWvln(State):
    def parse_state(self,state_str):
        self.quantity = Quantity.parse(state_str)
        self.check_if_energy_freq_or_wvln()
        
    def energy(self, units='J'):
        return self.quantity.convert_units_to(units, force='spec')
    
    def frequency(self, units='s-1'):
        return self.quantity.convert_units_to(units, force='spec')
    
    def wavelength(self, units='m'):
        return self.quantity.convert_units_to(units, force='spec')
    
    @property
    def html(self):
        return self.state_str
        
    def check_if_energy_freq_or_wvln(self):
        allowed_dims = [d_energy, d_frequency, d_length]
        comparisons = [self.quantity.units.dims == d for d in allowed_dims]
        if not any(comparisons):
            raise EnergyFreqWvlnError('Entered string must have units' \
                        'of energy, frequency or wavelength')
