from .state import State, StateParseError
from pyqn.quantity import Quantity
from pyqn.units import Units
from pyqn.dimensions import d_energy, d_frequency, d_length
from scipy.constants import c, hbar, pi
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
        if self.units.dims == d_length:
            w = self.wavelength()
            new_quantity = Quantity(value = 2*pi*hbar*c/w.value,
                                    units = 'J',
                                    sd = 2*pi*hbar*c*w.sd/w.value**2)
            q = new_quantity.convert_units_to(units)
        else:
            q = self.quantity.convert_units_to(units, force = 'spec')
        result = EnergyFreqWvln(str(q))
        result.set_sd(q.sd)
        return result
    
    def frequency(self, units='s-1'):
        if self.units.dims == d_length:
            w = self.wavelength()
            new_quantity = Quantity(value = c/w.value,
                                    units = 's-1',
                                    sd = c*w.sd/w.value**2)
            q = new_quantity.convert_units_to(units)
        else:
            q = self.quantity.convert_units_to(units, force='spec')
        result = EnergyFreqWvln(str(q))
        result.set_sd(q.sd)
        return result
    
    def wavelength(self, units='m'):
        if self.units.dims == d_frequency:
            f = self.frequency()
            new_quantity = Quantity(value = c/f.value, 
                                    units = 'm', 
                                    sd = c*f.sd/f.value**2)
            q = new_quantity.convert_units_to(units)
        elif self.units.dims == d_energy:
            e = self.energy()
            new_quantity = Quantity(value = hbar/e.value,
                                    units = 'm',
                                    sd = hbar*e.sd/e.value**2)
            q = new_quantity.convert_units_to(units)
        else:
            q = self.quantity.convert_units_to(units, force='spec')
        result = EnergyFreqWvln(str(q))
        result.set_sd(q.sd)
        return result
    
    @property
    def value(self):
        return self.quantity.value
    
    @property
    def units(self):
        return self.quantity.units
        
    @property
    def sd(self):
        return self.quantity.sd
        
    def set_sd(self, sd):
        self.quantity.sd = sd
        return
    
    def __str__(self):
        if self.sd:
            return '{} ± {} {}'.format(self.value, self.sd, self.units)
        else:
            return '{} {}'.format(self.value, self.units)
    __repr__ = __str__
    
    @property
    def html(self):
        return self.state_str
        
    def check_if_energy_freq_or_wvln(self):
        allowed_dims = [d_energy, d_frequency, d_length]
        comparisons = [self.quantity.units.dims == d for d in allowed_dims]
        if not any(comparisons):
            raise EnergyFreqWvlnError('Entered string must have units' \
                        'of energy, frequency or wavelength')
