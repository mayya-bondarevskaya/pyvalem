import pyparsing as pp
from .state import State, StateParseError

integer = pp.Word(pp.nums)
molecular_orbital_symbols = ('σ','π',
                             'SIGMA','PI',
                             'σu','πg',
                             'SIGMAu','PIg',
                             'σg','πu',
                             'SIGMAg','PIu')
greek_letters = {'SIGMA': 'σ',
                 'PI': 'π',
                 'SGIMAu':'σu',
                 'PIg':'πg',
                 'SIGMAg':'σg',
                 'PIu':'πu'}
molecule_orbital = pp.Group(integer.setResultsName('n')
                            +pp.oneOf(molecular_orbital_symbols).setResultsName('symbol'))

molecule_config = (molecule_orbital + pp.Optional(integer.setResultsName('count')) + 
                   pp.ZeroOrMore(pp.Suppress('.') +
                                 molecule_orbital + pp.Optional(integer) +
                                 pp.StringEnd())
                   ).leaveWhitespace()
                   
class DiatomicMolecularConfigurationError(StateParseError):
    pass

class MolecularOrbital:
    def __init__(self, n, symbol, count):
        self.n = n;

class DiatomicMolecularConfiguration(State):
    def parse_state(self, state_str):
        self.state_str = state_str
        
        try:
            parse_results = molecule_config.parseString(state_str)
        except pp.ParseException:
            raise StateParseError('Invalid diatomic molecular electronic '
                                  'configuration syntax: {0}'.format(state_str))
        
        self.orbital = []
        for i, parsed_orbital in enumerate(parse_results):
            temp_oribital = MolecularOrbital()