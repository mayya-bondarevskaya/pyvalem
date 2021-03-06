import pyparsing as pp
from .state import State, StateParseError

integer = pp.Word(pp.nums)
molecular_orbital_symbols = ('σ', 'π', 'δ',
                             'sigma', 'pi', 'delta',
                             'σg', 'πg', 'δg',
                             'σu', 'πu', 'δu',
                             'sigmag', 'pig', 'deltag',
                             'sigmau', 'piu', 'deltau',
                            )
                             
greek_letters = {'sigma': 'σ',
                 'pi': 'π',
                 'sigmau':'σu',
                 'pig':'πg',
                 'sigmag':'σg',
                 'piu':'πu'}
molecule_orbital = pp.Group(integer.setResultsName('n')
                +pp.oneOf(molecular_orbital_symbols).setResultsName('symbol')
                +pp.Optional(integer.setResultsName('count'), default='1'))

molecule_config = (molecule_orbital + 
                   pp.ZeroOrMore(pp.Suppress('.') + molecule_orbital) +
                   pp.StringEnd()).leaveWhitespace()
                   
class DiatomicMolecularConfigurationError(StateParseError):
    pass

class MolecularOrbital:
    def __init__(self, n, symbol, count):
        self.n = int(n)
        if symbol in greek_letters.keys():
            self.symbol = greek_letters[symbol]
        else:
            self.symbol = symbol
        self.count = int(count)
        self.validate_molecular_orbital()
        
    def __str__(self):
        return '{:d}{:s}{:d}'.format(self.n, self.symbol, self.count)
    __repr__ = __str__

    def __hash__(self):
        return hash((self.n, self.symbol, self.count))
    def __eq__(self, other):
        return (self.n == other.n and self.symbol == other.symbol and
                self.count == other.count)
    
    def validate_molecular_orbital(self):
        if self.symbol == 'σ':
            if self.count > 2:
                raise DiatomicMolecularConfigurationError('Only two electrons'
                 ' allowed in σ orbital, but received {:d}'.format(self.count))
        else:
            if self.count > 4:
                raise DiatomicMolecularConfigurationError('Only four electrons'
                                       ' allowed in π and δ orbitals, '
                                       'but received {:d}'.format(self.count))
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
            raise DiatomicMolecularConfigurationError('Repeated orbitals '
                                            'in {0}'.format(self.state_str))
            
    @property
    def html(self):
        html_chunks = []
        if self.orbitals:
            for orbital in self.orbitals:
                html_chunks.append('{:d}{:s}<sub>{:d}<\sub>'.format(orbital.n,
                                                orbital.symbol,orbital.count))
        return '.'.join(html_chunks)