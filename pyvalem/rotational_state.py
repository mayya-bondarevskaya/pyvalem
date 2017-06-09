import pyparsing as pp
from .state import State, StateParseError
from .utils import parse_fraction

integer = pp.Word(pp.nums)
atom_Jstr = (integer+pp.Optional(pp.Suppress('/')+integer) + pp.StringEnd()
            ).setResultsName('Jstr')

class RotationalState(State):
    def parse_state(self, state_str):

        if state_str.startswith('J='):
            state_str = state_str[2:]

        self.J = None
        if state_str not in ('*', '**', '***'):
            try:
                components = atom_Jstr.parseString(state_str)
            except pp.ParseException:
                raise StateParseError('Invalid rotational state value syntax: '
                                      '{0}'.format(state_str))
            
            self.J = parse_fraction(components.Jstr)
            
            if self.J is not None:
                self.validate_J()

        self.state_str = 'J={}'.format(state_str)
    
    def validate_J(self):
        if self.J % 0.5 != 0:
            raise StateParseError('Invalid rotational state value: {}.'
                    'Must be a multiple of 1/2.'.format(self.state_str))
