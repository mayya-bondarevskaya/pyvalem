#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
from ..atomic_configuration import AtomicConfiguration
from ..atomic_term_symbol import AtomicTermSymbol
from ..generic_excited_state import GenericExcitedState
from ..molecular_term_symbol import MolecularTermSymbol
from ..rotational_state import RotationalState
from ..vibrational_state import VibrationalState
from ..state import State, StateParseError

with codecs.open("pyvalem/tests/qdb_states.txt", encoding='utf-8') as qdb:
    examples = qdb.readlines()

final_data = []
exception_data = []
no_classes_yet_data = []
for item in examples:
    # each entry is pk (ID), state_typeID, state_str
    final_data.append(item.split())

STATE_TYPE_CHOICES = ['ARBITRARY_KEY_VALUE_PAIRS',
                      GenericExcitedState,
                      AtomicConfiguration,
                      AtomicTermSymbol,
                      'MOLECULE_CONFIGURATION',
                      MolecularTermSymbol,
                      VibrationalState,
                      'POLYATOMIC_VIBRATIONAL',
                      'NUCLEAR_SPIN_STATE',
                      'ENERGY_FREQ_WVLN',
                      RotationalState,
                      'RACAH_SYMBOL'
                      ]

for item in final_data:
    class_choice = STATE_TYPE_CHOICES[int(item[1])]
    if type(class_choice) != str:
        try:
            temp = class_choice(item[2].encode('utf-8'))
        except Exception as inst:
            print(inst)
            exception_data.append(item)
    else:
        no_classes_yet_data.append(item)

for item in exception_data:
    print(' '.join(item))
