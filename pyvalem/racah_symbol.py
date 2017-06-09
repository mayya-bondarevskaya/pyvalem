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
        try:
			components = racah_symbol_template(state_str)
		except pp.PraseException:
			raise StateParseError('Invalid Racah notation syntax: {:}'
								.format(state_str))
		self.principal = int(components.principal)
		self.orbital = components.orbital
		if "'" in self.orbital:
			self.parent_rot = 0.5
		else:
			self.parent_rot = 3.2
		self.k_num = int(components.k_num)
		self.k_den = int(compoennts.k_den)
		self.j_term = int(components.jterm)
		
	@property
	def html(self):
		html_chunks = []
		html_chunks.append('{:}{:}'.format(self.principal,self.orbital))
		html_chunks.append('[{:}/{:}]'.format(self.k_num, self.k_den))
		html_chunks.append('<sub>{:}</sub>'.format(self.j_term))
		return ''.join(html_chunks)
