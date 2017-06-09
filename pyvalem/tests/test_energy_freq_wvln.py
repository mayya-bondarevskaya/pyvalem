from ..energy_freq_wvln import EnergyFreqWvln
from ..state import State, StateParseError
import unittest

class EnergyFreqWvlnTest(unittest.TestCase):
    def test_energy_input(self):
        e1 = EnergyFreqWvln('200 J')
        e1_energy = e1.energy()
        e1_energy_ev = e1.energy(units = 'eV')
        e1_freq = e1.frequency()
        e1_wvln = e1.wavelength()
        self.assertEqual(e1_energy.value,200)
        self.assertAlmostEqual(e1_energy_ev.value, 1.2483019294240832e+21)
        self.assertAlmostEqual(e1_freq.value, 3.018380901366291e+35)
        self.assertAlmostEqual(e1_wvln.value, 3.9728910007918073e-23)
        
        e2 = EnergyFreqWvln('2.0e25 eV')
        e2_energy_j = e2.energy()
        e2_energy_ev = e2.energy(units = 'eV')
        e2_freq = e2.frequency()
        e2_wvln =e2.wavelength(units = 'nm')
        self.assertAlmostEqual(e2_energy_j.value, 3204352.9740000004)
        self.assertAlmostEqual(e2_energy_ev.value, 2.0e25)
        self.assertAlmostEqual(e2_freq.value, 4.835978908978938e+39)
        self.assertAlmostEqual(e2_wvln.value, 6.365272546882531e-10)
        
    def test_frequency_input(self):
        f1 = EnergyFreqWvln('25e13 s-1')
        f1_energy = f1.energy()
        f1_freq = f1.frequency()
        f1_wvln = f1.wavelength()
        self.assertAlmostEqual(f1_energy.value, 1.65651724e-19)
        self.assertAlmostEqual(f1_freq.value, 25e13)
        self.assertAlmostEqual(f1_wvln.value, 3.2905812177262413e-44)
    
    def test_wavelength_input(self):
        w1 = EnergyFreqWvln('23.05e-6 m')
        w1_energy = w1.energy()
        w1_freq = w1.frequency()
        w1_wvln = w1.wavelength()
        self.assertAlmostEqual(w1_energy.value, 1.1603640772125929e+20)
        self.assertAlmostEqual(w1_freq.value, 1.7512103846450052e+53)
        self.assertAlmostEqual(w1_wvln.value, 2.305e-05)
        
    def test_html(self):
        e1 = EnergyFreqWvln('25e13 s-1')
        e2 = EnergyFreqWvln('23.05e-6 m')
        e3 = EnergyFreqWvln('2.0e25 eV')
        e4 = EnergyFreqWvln('200 J')
        
        self.assertEqual(e1.html, '25e13 s-1')
        self.assertEqual(e2.html, '23.05e-6 m')
        self.assertEqual(e3.html, '2.0e25 eV')
        self.assertEqual(e4.html, '200 J')
    
if __name__ == '__main__':
    unittest.main()
