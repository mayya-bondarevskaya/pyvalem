from ..energy_freq_wvln import EnergyFreqWvln
from ..state import State,StateParseError
import unittest

class EnergyFreqWvlnTest(unittest.TestCase):
    def test_energy_input(self):
        e1 = EnergyFreqWvln('200 J')
        e1_energy = e1.energy()
        e1_energy_ev = e1.energy(units = 'eV')
        e1_freq = e1.frequency()
        e1_wvln = e1.wavelength()
        self.assertEqual(e1_energy.value,200)
        self.assertTrue(abs(e1_energy_ev.value-1.2483019294240832e+21) < 0.01)
        self.assertTrue(abs(e1_freq.value-3.018380901366291e+35) < 0.01)
        self.assertTrue(abs(e1_wvln.value-3.9728910007918073e-23) < 0.01)
        
    def test_frequency_input(self):
        pass
    
    def test_wavelength_input(self):
        pass
    
    def test_energy_mol_input(self):
        pass
    
if __name__ == '__main__':
    unittest.main()