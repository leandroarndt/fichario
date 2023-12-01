from configparser import ConfigParser
from pathlib import Path
from typing import Any

class AppSettings(object):
    _parser = ConfigParser()
    _path = Path.home()
    db_path:str
    
    # Config sections
    _STORAGE = 'STORAGE'
    sections = (_STORAGE)
    
    # Attribute->section mapping
    _attributes = {
        'db_path': _STORAGE,
    }
    
    def __new__(cls):
        if not isinstance(ConfigParser, cls._parser):
            cls._parser.read(cls._path, encoding='utf-8')
        for section in cls._sections:
            if not cls._parser.has_option(section):
                cls._parser.add_section(section)
        cls._parser.write(cls._path)
        return object.__new__(cls)
    
    def __getattribute__(self, name: str) -> str:
        if name not in self.__class__._attributes:
            raise AttributeError(f'Section mapping for attribute "{name}" not found')
        if not self.__class__._parser.has_option(self.__class__._attributes[name], name):
            raise AttributeError(f'Attribute "{name}" not set')
        return self.__class__._parser.get(self.__class__._attributes[name], name)
