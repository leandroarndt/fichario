from abc import ABC
from configparser import NoOptionError, NoSectionError

class Setting(ABC):
    
    def __set_name__(self, owner, name):
        self._name = name
    
    def __get__(self, obj, obj_type=None) -> str:
        try:
            return obj._parser.get(obj._attributes[self._name], self._name)
        except (NoSectionError, NoOptionError):
            return self._default
    
    def __set__(self, obj, value):
        try:
            obj._parser.set(obj._attributes[self._name], self._name, value)
        except NoSectionError:
            obj._parser.add_section(obj._attributes[self._name])
            obj._parser.set(self._owner._attributes[self._name], self._name, value)