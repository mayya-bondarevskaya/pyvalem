from .state import State, StateParseError
from pyqn.pyqn.quantity import Quantity
from pyqn.pyqn.units import Units
from pyqn.pyqn.dimensions import Dimensions, d_energy, d_length, d_frequency, d_quantity
#This module HAS to be run from above the main Pyvalem folder, such that
#this module can also "see" the pyqn directory

class EnergyFreqWvln(State):
    def parse_state(self,state_str):
        self.state_str = state_str.split()
        self.values = {}
        in_unit = self.state_str[1]
        in_unit_dims = Units(self.state_str[1]).dims
        in_val = float(self.state_str[0])
        if (in_unit_dims == d_energy):
            self.values['energy'] = Quantity(value=in_val,units=in_unit)
            self.values['energy_mol']=self.values['energy'].convert_units_to(self.state_str[1]+'/mol',force='mol')
            self.values['wavelength']=self.values['energy'].convert_units_to('m',force='spec')
            self.values['frequency']=self.values['energy'].convert_units_to('s-1',force='spec')
        elif (in_unit_dims == d_energy/d_quantity):
            self.values['energy_mol']= Quantity(value=in_val,units=in_unit)
            self.values['energy']=self.values['energy_mol'].convert_units_to('J',force='mol')
            self.values['wavelength']=self.values['energy'].convert_units_to('m',force='spec')
            self.values['frequency']=self.values['energy'].convert_units_to('s-1',force='spec')
        elif (in_unit_dims == d_length):
            self.values['wavelength']=Quantity(value=in_val,units=in_unit)
            self.values['energy']=self.values['wavelength'].convert_units_to('J',force='spec')
            self.values['frequency']=self.values['energy'].convert_units_to('s-1',force='spec')
            self.values['energy_mol']=self.values['energy'].convert_units_to(in_unit+'/mol',force='mol')
        elif (in_unit_dims == d_frequency):
            self.values['frequency']=Quantity(value=in_val,units=in_unit)
            self.values['energy']=self.values['frequency'].convert_units_to('J',force='spec')
            self.values['energy_mol']=self.values['energy'].convert_units_to(self.state_str[1]+'/mol',force='mol')
            self.values['wavelength']=self.values['energy'].convert_units_to('m',force='spec')
        else:
            raise StateParseError('Invalid dimensions of units entered')
        
    def energy(self,units='J'):
    """
    Returns the energy as a Quantity with units 'J' by default
    """
        return self.values['energy'].convert_units_to(units)
    
    def frequency(self,units='s-1'):
    """
    Returns the frequency as a Quantity with units 's-1' by default
    """
        return self.values['frequency'].convert_units_to(units)
    
    def wavelength(self,units='m'):
    """
    Returns the wavelength as a Quantity with units 'm' by default
    """
        return self.values['wavelength'].convert_units_to(units)
        
    def energy_per_mol(self,units='J.mol-1'):
    """
    Returns the energy/mol as a Quantity with units 'J/mol' by default
    """
        return self.values['energy_mol'].convert_units_to(units)