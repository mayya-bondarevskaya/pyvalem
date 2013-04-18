from pyvalem.chem_formula import ChemFormula

f0 = ChemFormula('H2O')
print f0.stoichiometric_formula(), f0.rmm
f1 = ChemFormula('C2F4H2')
print f1.stoichiometric_formula(), f1.rmm
print f1.stoichiometric_formula('hill')
print f1.stoichiometric_formula('alphabetical')

f2 = ChemFormula('NO+')
f3 = ChemFormula('OH-')
f4 = ChemFormula('CoN6H18-2')
f5 = ChemFormula('Cu+2')
print f2
print f3, f3.html
print f4, f4.html
print f5, f5.html

f6 = ChemFormula('CO(16O)')
f7 = ChemFormula('(14N)(1H)(16O)2(18O)(16O)')
print f7, f7.stoichiometric_formula(), f7.html, f7.rmm

f8 = ChemFormula('CH3CH2OH')
print f8
print f8.stoichiometric_formula()
print f8.stoichiometric_formula('hill')
print f8.stoichiometric_formula('alphabetical')

carbonate = ChemFormula('CO3-2')
print carbonate
print carbonate.html
ethanol = ChemFormula('CH3CH2OH')
print ethanol.rmm
