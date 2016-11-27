import pyparsing as pp
from .state import State, StateParseError

atom_vLevels = ('v1','v2','v3','v4','v5','v6')

integer = pp.Word(pp.nums)
atom_first_vLevel = pp.oneOf(atom_vLevels).setResultsName('firstVLevel')
atom_first_vLevel_int = integer.setResultsName('firstVLevelInt')
atom_second_vLevel = pp.oneOf(atom_vLevels).setResultsName('secondVLevel')
atom_second_vLevel_int = integer.setResultsName('secondVLevelInt')

atom_term = (pp.Optional(atom_first_vLevel_int)+atom_first_vLevel+
             pp.Optional(atom_second_vLevel_int)+atom_second_vLevel+
             pp.stringEnd())

atom_exc = integer.setResultsName('excLevel')
atom_term_exc = (atom_exc+pp.StringEnd())

class VibrationalState(State):
    def parse_state(self,state_str):
        self.state_str = state_str
        
        if '+' in state_str:
            try:
                components = atom_term.parseString(state_str)
            except pp.ParseException:
                raise StateParseError('Invalid atomic term symbol syntax: {0}'
                                            .format(state_str))
                
            self.first_vLevel = components.firstVLevel
            self.second_vLevel = components.secondVLevel
            if components.firstVLevelInt is not None:
                self.first_vLevel_int = int(components.firstVLevelInt)
            if components.secondVLevelInt is not None:
                self.second_vLevel_int = int(components.secondVLevelInt)
                
        else:
            try:
                components = atom_term_exc.parseString(state_str)
            except pp.ParseException:
                raise StateParseError('Invalid atomic term symbol syntax: {0}'
                                            .format(state_str))
            self.exc_level = int(components.excLevel)