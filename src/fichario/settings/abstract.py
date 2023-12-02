from abc import ABC
from configparser import NoOptionError, NoSectionError

class Setting(ABC):
    _default = ''
    
    def __set_name__(self, owner, name):
        self._name = name
    
    def __get__(self, obj, obj_type=None) -> str:
        try:
            return obj._parser.get(obj._attributes[self._name], self._name)
        except (NoSectionError, NoOptionError):
            return self._default
    
    def __set__(self, obj, value):
        try:
            obj._parser.set(obj._attributes[self._name], self._name, str(value))
        except NoSectionError:
            obj._parser.add_section(obj._attributes[self._name])
            obj._parser.set(self._owner._attributes[self._name], self._name, str(value))
    
    def __init__(self, default=None):
        if default is not None:
            self._default = default

class BooleanSetting(Setting):
    _default = False
    
    def __get__(self, obj, obj_type=None) -> bool:
        if super().__get__(obj, obj_type) == 'True':
            return True
        return False

class Version(Setting):
    _version = 0
    _subversion = 0
    _revision = 0
    
    @staticmethod
    def decode(value):
        version, subversion, revision = value.split('.')
        return int(version), int(subversion), int(revision)
    
    @staticmethod
    def encode(value):
        return f'{value[0]}.{value[1]}.{value[2]}'
    
    def __set__(self, obj, value):
        if not isinstance(value, str):
            value = self.encode(value)
        self._version, self._subversion, self._revision = self.decode(value)
        super().__set__(obj, value)
    
    def __gt__(self, other):
        if self._version > other._version:
            return True
        if self._subversion > other._subversion:
            return True
        if self._revision > other._revision:
            return True
        return False
    
    def __eq__(self, other):
        if self._version == other._version and self._subversion == other._subversion and self._revision == other._revision:
            return True
        return False
    
    def __init__(self, default='0.0.0', *args, **kwargs):
        super(*args, **kwargs)
        self._version, self._subversion, self._revision = self.decode(default)
