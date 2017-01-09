import pyparsing as pp
from .state import State, StateParseError

integer = pp.Word(pp.nums)
molecular_orbital_symbols = ('σ','π',
                             'σu','πg',
                             'σg','πu')
molecule_orbital = pp.Group(integer.setResultsName('n')
                            +pp.oneOf(molecular_orbital_sumbols).setResultsName('symbol'))

molecule_config = (molecule_orbital + pp.Optional(integer.setResultsName('count'))
                   pp.ZeroOrMore(pp.Suppress('.') +
                                 molecule_orbital + pp.Optional(integer)
                                 pp.StringEnd())
                   ).leaveWhitespace()
                   
class DeatomicMolecularConfigurationError(StateParseError):
    pass

class DiatomicMolecularConfiguration(State):
    