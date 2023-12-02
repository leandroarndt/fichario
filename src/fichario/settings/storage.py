from configparser import ConfigParser
from pathlib import Path
from . import abstract

class AppSettings(object):
    _parser:ConfigParser = None
    _path = Path(Path.home(), 'fichario.ini')
    db_path = abstract.Setting(Path(Path.home(), 'fichario.sqlite3'))
    db_migration = abstract.Version()
    use_dav = abstract.BooleanSetting()
    dav_url = abstract.Setting()
    dav_user = abstract.Setting()
    dav_password = abstract.Setting()
    use_google_drive = abstract.BooleanSetting()
    sync_path = abstract.Setting(Path(Path.home(), 'fichario synchronization'))
    
    # Config sections
    _DB = 'DB'
    _REMOTE = 'REMOTE'
    _SYNC = 'SYNC'
    _sections = (_DB, _REMOTE, _SYNC)
    
    # Attribute->section mapping
    _attributes = {
        'db_path': _DB,
        'db_migration': _DB,
        'use_dav': _REMOTE,
        'dav_url': _REMOTE,
        'dav_user': _REMOTE,
        'dav_password': _REMOTE, # In Android, it should be FS encrypted
        'use_google_drive': _REMOTE, # Google Drive credentials are stored in a separate file
        'sync_path': _SYNC,
    }
    
    def save(self):
        with open(self._path, 'w') as f:
            self.__class__._parser.write(f)
    
    def __new__(cls):
        modified = False
        if not cls._parser:
            cls._parser = ConfigParser()
            cls._path = Path(Path.home(), 'fichario.ini')
            cls._parser.read(cls._path, encoding='utf-8')
        for section in cls._sections:
            if not cls._parser.has_section(section):
                cls._parser.add_section(section)
                modified = True
        if modified:
            with open(cls._path, 'w') as f:
                cls._parser.write(f)
        return object.__new__(cls)
