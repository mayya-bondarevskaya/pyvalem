import codecs
from ..atomic_configuration import AtomicConfiguration
from ..atomic_term_symbol import AtomicTermSymbol
from ..excited_state import ExcitedState
from ..molecular_term_symbol import MolecularTermSymbol
from ..rotational_state import RotationalState
from ..vibrational_state import VibrationalState
from ..state import State, StateParseError

with codecs.open("pyvalem/tests/qdb_states.txt",encoding='utf-8') as qdb:
    examples = qdb.readlines()

final_data = []
exception_data = []
for item in examples:
    final_data.append(item.split())

STATE_TYPE_CHOICES = ['ARBITRARY_KEY_VALUE_PAIRS',
                      ExcitedState,
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
            temp = class_choice(item[2])
        except Exception as inst:
            exception_data.append(item)
print(exception_data)