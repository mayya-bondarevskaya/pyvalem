# state.py
# Version 1.2
# A base class representing an atomic or molecular state.
# Various derived classes will create their versions of State
# objects by parsing text strings.
#
# Copyright (C) 2012-2016 Christian Hill
# xn.hill@gmail.com
# http://christianhill.co.uk/projects/pyvalem
#
# This file is part of PyValem
#
# PyValem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyValem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyValem.  If not, see <http://www.gnu.org/licenses/>


class StateParseError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

class State:
    def __init__(self, state_str):
        self.state_str = state_str
        self.parse_state(state_str)

    def __str__(self):
        return self.state_str
    __repr__ = __str__

    @property
    def html(self):
        return str(self)

