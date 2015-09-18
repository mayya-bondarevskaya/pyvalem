# pyvalem
A Python package for handling chemical formulae for atoms, isotopes, molecules and isotopologues.

A very quick overview:

    In [1]: from pyvalem.chem_formula import ChemFormula

    In [2]: ethanol = ChemFormula('CH3CH2OH')

    In [3]: ethanol.rmm
    Out[3]: 46.068439999999995

    In [4]: ethanol.stoichiometric_formula()
    Out[4]: 'H6C2O'

    In [5]: ethanol.stoichiometric_formula('alphabetical')
    Out[5]: 'C2H6O'

    In [6]: ethanol.stoichiometric_formula('hill')
    Out[6]: 'C2H6O'

    In [7]: ethanol.html
    Out[7]: 'CH<sub>3</sub>CH<sub>2</sub>OH'

    In [8]: ethanol.slug
    Out[8]: 'CH3CH2OH'

    In [9]: ethanol.natoms
    Out[9]: 9

    In [10]: ethanol.charge
    Out[10]: 0

For more information and examples, see http://christianhill.co.uk/projects/pyvalem
