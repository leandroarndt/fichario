from pathlib import Path
from configparser import NoOptionError, NoSectionError
from . import abstract

last_migration = "0.0.0"

class DBPath(abstract.Setting):
    _default = Path(Path.home(), 'fichario.sqlite3')

class DBMigration(abstract.Setting):
    _version = 0
    _subversion = 0
    _revision = 0
    
    def __set__(self, obj, value):
        self._version, self._subversion, self._revision = value.split('.')
        self._version = int(self._version)
        self._subversion = int(self._subversion)
        self._revision = int(self._revision)
        
    def __get__(self, obj, objtype=None):
        return f'{self._version}.{self._subversion}.{self._revision}'
    
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
