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
print f3
print f4
print f5

f6 = ChemFormula('COGh')

