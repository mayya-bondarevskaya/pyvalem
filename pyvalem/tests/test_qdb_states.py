#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
from ..atomic_configuration import AtomicConfiguration
from ..atomic_term_symbol import AtomicTermSymbol
from ..generic_excited_state import GenericExcitedState
from ..key_value_pair import KeyValuePair
from ..molecular_term_symbol import MolecularTermSymbol
from ..racah_symbol import RacahSymbol
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

STATE_TYPE_CHOICES = [KeyValuePair, 			#0
                      GenericExcitedState,		#1
                      AtomicConfiguration,		#2
                      AtomicTermSymbol,			#3
                      'MOLECULE_CONFIGURATION',	#4
                      MolecularTermSymbol,		#5
                      VibrationalState,			#6
                      VibrationalState,			#7
                      'NUCLEAR_SPIN_STATE',		#8
                      'ENERGY_FREQ_WVLN',		#9
                      RotationalState,			#10
                      RacahSymbol				#11
                      ]

for item in final_data:
    class_choice = STATE_TYPE_CHOICES[int(item[1])]
    if type(class_choice) != str:
        try:
            temp = class_choice(item[2].encode('utf-8'))
        except Exception as inst:
            exception_data.append(item)
    else:
        no_classes_yet_data.append(item)

for item in no_classes_yet_data:
    print(' '.join(item))
