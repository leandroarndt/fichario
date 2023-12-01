from configparser import ConfigParser
from pathlib import Path
from . import db

class AppSettings(object):
    _parser:ConfigParser = None
    _path = Path(Path.home(), 'fichario.ini')
    db_path = db.DBPath()
    db_migration = db.DBMigration()
    
    # Config sections
    _DB = 'DB'
    _sections = (_DB,)
    
    # Attribute->section mapping
    _attributes = {
        'db_path': _DB,
        'db_migration': _DB,
    }
    
    def save(self):
        with open(self._path, 'w') as f:
            self.__class__._parser.write(f)
    
    def __new__(cls):
        if not cls._parser:
            cls._parser = ConfigParser()
            cls._path = Path(Path.home(), 'fichario.ini')
            cls._parser.read(cls._path, encoding='utf-8')
        for section in cls._sections:
            if not cls._parser.has_section(section):
                cls._parser.add_section(section)
        with open(cls._path, 'w') as f:
            cls._parser.write(f)
        return object.__new__(cls)
