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
                            +pp.oneOf(molecular_orbital_symbols).setResultsName('symbol')
                            +pp.Optional(integer.setResultsName('count')))

molecule_config = (molecule_orbital + 
                   pp.ZeroOrMore(pp.Suppress('.') +
                                 molecule_orbital + 
                                 pp.StringEnd())
                   ).leaveWhitespace()
                   
class DiatomicMolecularConfigurationError(StateParseError):
    pass

class MolecularOrbital:
    def __init__(self, n, symbol, count=1):
        self.n = n
        if symbol in greek_letters.keys():
            self.symbol = greek_letters[symbol]
        else:
            self.symbol = symbol
        self.count = count
        
    def __str__(self):
        pass
    
    def validate_molecular_orbital(self):
        pass

class DiatomicMolecularConfiguration(State):
    def parse_state(self, state_str):
        self.state_str = state_str
        
        try:
            parse_results = molecule_config.parseString(state_str)
        except pp.ParseException:
            raise StateParseError('Invalid diatomic molecular electronic '
                                  'configuration syntax: {0}'.format(state_str))
        
        self.orbitals = []
        for i, parsed_orbital in enumerate(parse_results):
            temp_orbital = MolecularOrbital(n = parsed_orbital['n'],
                                             symbol = parsed_orbital['symbol'],
                                             count = parsed_orbital['count'])
            self.orbitals.append(temp_orbital)
        
        if len(self.orbitals) != len(set(self.orbitals)):
            raise DiatomicMolecularConfigurationError('Repeated orbitals in {0}'.format(self.state_str))
            
            
            
            
            
            
            
            
            
            
            
            