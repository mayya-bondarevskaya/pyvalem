import pyparsing as pp
from .state import State, StateParseError

integer = pp.Word(pp.nums)
atom_int = integer.setResultsName('int')
state_term = ((atom_int + '*' + pp.StringEnd())).leaveWhitespace()

class GenericExcitedState(State):
    def parse_state(self,state_str):
        self.state_str = state_str
        
        if '*' in state_str:
            if state_str.count('*') == len(state_str):
                if len(state_str) > 3:
                    raise StateParseError('Invalid excited state value: {0}'
                                    ' Can be *, **, or ***'.format(state_str))
            else:
                try:
                    components = state_term.parseString(state_str)
                    self.int_n = int(components.int)
                except pp.ParseException:
                    raise StateParseError(
                'Invalid excited state value syntax: {0} has to be of form'
                ' n* with n = integer'.format(state_str)
                                         )
        else:
            raise StateParseError('Invalid excited state value syntax: {0}'
                                  ' Must have a * term.'.format(state_str))
