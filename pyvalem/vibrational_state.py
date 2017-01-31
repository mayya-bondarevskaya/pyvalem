import pyparsing as pp
from .state import State, StateParseError

integer = pp.Word(pp.nums)

vibrational_term = pp.Group(pp.Optional(integer.setResultsName('n'),default=1)+
                            'v' + integer.setResultsName('count'))
vibrational_config = (vibrational_term + 
                      pp.ZeroOrMore(pp.Suppress('+') + vibrational_term) +
                      pp.StringEnd()).leaveWhitespace()

simple_config = (integer.setResultsName('n')+pp.StringEnd()).leaveWhitespace()

class VibrationalTerm:
    def __init__(self, n, count):
        self.n = int(n)
        self.count = int(count)
    
    def __str__(self):
        return '{:d}v{:d}'.format(self.n,self.count)
    __repr__=__str__

class VibrationalState(State):
    def parse_state(self,state_str):
        self.state_str = state_str.replace(' ','')
        
        if '+' in state_str:
            try:
                parse_results = vibrational_config.parseString(self.state_str)
            except pp.ParseException:
                raise StateParseError('Invalid vibrational state configuration'
                                      ' syntax: {0}'.format(self.state_str))
            self.terms = []
            for i, parsed_term in enumerate(parse_results):
                temp_term = VibrationalTerm(n = parsed_term['n'],
                                            count = parsed_term['count'])
                self.terms.append(temp_term)
        else:
            try:
                parse_results = simple_config.parseString(self.state_str)
            except pp.ParseException:
                raise StateParseError('Invalid vibrational state configuration'
                                      ' syntax: {0}'.format(self.state_str))