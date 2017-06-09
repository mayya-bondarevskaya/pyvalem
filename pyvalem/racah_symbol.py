import pyparsing as pp
from .state import State, StateParseError

integer = pp.Word(pp.nums)
atom_principal = integer.setResultsName('principal')

orbital_labels = ('s', "s'", 
				  'p', "p'",
				  'd', "d'",
				  'f', "f'")
atom_orbital = pp.OneOf(orbital_labels).setResultsName('orbital')

atom_k_term = integer.setResultsName('k_num') + pp.Suppress('/') + 
				integer.setResultsName('k_den')

atom_j_term = integer.setResultsName('jterm')

racah_symbol_template = atom_principal + atom_orbital + 
						pp.Suppress('[') + atom_k_term + 
						pp.Suppress(']_') + atom_j_term

class RacahSymbol(State):
    """The RacahSymbol class representing an atomic state

    It hasn't been written yet.

    """

    def parse_state(self, state_str):
        # nothing to see here, for now... Mayya to write this?
        pass
