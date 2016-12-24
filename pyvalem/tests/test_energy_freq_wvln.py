from ..energy_freq_wvln import EnergyFreqWvln
from ..state import State,StateParseError
import unittest

class EnergyFreqWvlnTest(unittest.TestCase):
    def test_energy_input(self):
        e1 = EnergyFreqWvln('200 J')
        e1_energy = e1.energy()
        self.assertEqual(e1_energy.value,200)
        
    def test_frequency_input(self):
        pass
    
    def test_wavelength_input(self):
        pass
    
    def test_energy_mol_input(self):
        pass
    
if __name__ == '__main__':
    unittest.main()