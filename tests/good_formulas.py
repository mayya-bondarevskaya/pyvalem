# good_formulas.py
# A dictionary of some valid formulas to be parsed by ChemFormula and
# their properties.
#
# Copyright (C) 2012-2015 Christian Hill
#
# This file is part of PyValem

good_formulas = {
    'Br':
            {'stoichiometric_formula': 'Br',
             'html': 'Br',
             'slug': 'Br',
             'rmm': 79.904,
             'natoms': 1,
             'latex': r'$\mathrm{Br}$'
            },
    '(79Br)':
            {'stoichiometric_formula': '(79Br)',
             'html': '<sup>79</sup>Br',
             'slug': '79Br',
             'rmm': 78.918337,
             'natoms': 1,
             'latex': r'$^{79}\mathrm{Br}$'
            },
    '(2H)+':
            {'stoichiometric_formula': '(2H)+',
             'html': '<sup>2</sup>H<sup>+</sup>',
             'slug': '2H_p',
             'rmm': 2.014102,
             'natoms': 1
            },
    'CH3OH':
            {'stoichiometric_formula': 'H4CO',
             'html': 'CH<sub>3</sub>OH',
             'slug': 'CH3OH',
             'rmm': 32.04186,
             'natoms': 6
            },
    'CH3COOONO2':
            {'stoichiometric_formula': 'H3C2NO5',
             'html': 'CH<sub>3</sub>COOONO<sub>2</sub>',
             'slug': 'CH3COOONO2',
             'rmm': 121.04892,
             'natoms': 11
            },
    'CH(CH3)2CO2H':
            {'stoichiometric_formula': 'H8C4O2',
             'html': 'CH(CH<sub>3</sub>)<sub>2</sub>CO<sub>2</sub>H',
             'slug': 'CH_d__CH3_d__2CO2H',
             'rmm': 88.10512,
             'natoms': 14
            },
    'SiO2.2H2O':
            {'stoichiometric_formula': 'H4O4Si',
             'html': 'SiO<sub>2</sub>2H<sub>2</sub>O',
             'slug': 'SiO2_d_2H2O',
             'rmm': 96.11486,
             'natoms': 9
            },
    'SiO2.2(H2O)': 
            {'stoichiometric_formula': 'H4O4Si',
             'html': 'SiO<sub>2</sub>2(H<sub>2</sub>O)',
             'slug': 'SiO2_d_2_H2O_',
             'rmm': 96.11486,
             'natoms': 9,
            },
    'Co(NH2+)(NH3)5':
            {'stoichiometric_formula': 'H17N6Co+',
             'html': 'Co(NH<sub>2</sub><sup>+</sup>)(NH<sub>3</sub>)'
                     '<sub>5</sub>',
             'slug': 'Co_d__NH2_p_d___NH3_5',
             'rmm': 160.108375,
             'natoms': 24,
             'latex': r'$\mathrm{Co}(\mathrm{N}\mathrm{H}_{2}^{+})(\mathrm{N}\mathrm{H}_{3})_{5}$'
            },
    '2H3+':
            {'stoichiometric_formula': 'H6+2',
             'html': '2H<sub>3</sub><sup>+</sup>',
             'slug': '2H3_p',
             'rmm': 6.04764,
             'natoms': 6
            },
    '3CO3+2':
            {'stoichiometric_formula': 'C3O9+6',
             'html': '3CO<sub>3</sub><sup>2+</sup>',
             'slug': '3CO3_p2',
             'rmm': 180.0267,
             'natoms': 12
            },
    'C2H5·':
            {'stoichiometric_formula': 'H5C2',
             'html': 'C<sub>2</sub>H<sub>5</sub>&#183;',
             'slug': 'C2H5_dot',
             'rmm': 29.0611,
             'natoms': 7
            },
    'CH2(NH+)CH2CO2-':
            {'stoichiometric_formula': 'H5C3NO2',
             'html': 'CH<sub>2</sub>(NH<sup>+</sup>)CH<sub>2</sub>'
                     'CO<sub>2</sub><sup>-</sup>',
             'slug': 'CH2_d__NH_p_d__CH2CO2_m',
             'rmm': 87.0773,
             'natoms': 11
            },
    '(13C)H3CH2OH':
            {'stoichiometric_formula': 'H6C(13C)O',
             'html': '<sup>13</sup>CH<sub>3</sub>CH<sub>2</sub>OH',
             'slug': '13CH3CH2OH',
             'rmm': 47.061095,
             'natoms': 9
            },
    '(1H)3(14N)(16O)2+':
            {'stoichiometric_formula': '(1H)3(14N)(16O)2+',
             'html': '<sup>1</sup>H<sub>3</sub><sup>14</sup>N'
                     '<sup>16</sup>O<sub>2</sub><sup>+</sup>',
             'slug': '1H3-14N-16O2_p',
             'rmm': 49.016379,
             'natoms': 6
            },

    '(S)-CH3C(NH3+)CO2-':
            {'stoichiometric_formula': 'H6C3NO2',
             'html': '(S)-CH<sub>3</sub>C(NH<sub>3</sub><sup>+</sup>)'
                     'CO<sub>2</sub><sup>-</sup>',
             'slug': 'S__CH3C_d__NH3_p_d__CO2_m',
             'rmm': 88.08524,
             'natoms': 12
            },
    '(±)-CHClBrF':
            {'stoichiometric_formula': 'HCFClBr',
             'html': '(±)-CHClBrF',
             'slug': 'pm__CHClBrF',
             'rmm': 147.374043,
             'natoms': 5
            },
    '1,1-C2H4Cl2':
            {'stoichiometric_formula': 'H4C2Cl2',
             'html': '1,1-C<sub>2</sub>H<sub>4</sub>Cl<sub>2</sub>',
             'slug': '1_1__C2H4Cl2',
             'rmm': 98.95916,
             'natoms': 8
            },
    '1,1-D-(+)-CH3CH(Cl)(Br)CH(F)(Cl)CHCl2':
            {'stoichiometric_formula': 'H6C4FCl4Br',
             'html': '1,1-<span style="font-size: 80%;">D</span>-(+)-'
                     'CH<sub>3</sub>CH(Cl)(Br)CH(F)(Cl)CHCl<sub>2</sub>',
             'slug': '1_1_D_p__CH3CH_d__Cl_d___Br_d__CH_d__F_d___Cl_d__CHCl2',
             'rmm': 294.804843,
            },
    #'para-C6H5Cl':
    #        {'stoichiometric_formula': 'H5C6Cl',
    #         'html': 'para-C<sub>6</sub>H<sub>5</sub>Cl',
    #         'slug': 'para__C6H5Cl',
    #         'rmm': 112.5569,
    #         'natoms': 12
    #        },
    'cis-1,2-CHFCHF':
            {'stoichiometric_formula': 'H2C2F2',
             'html': 'cis-1,2-CHFCHF',
             'slug': 'cis_1_2__CHFCHF',
             'rmm': 64.034086,
             'natoms': 6
            },
}
