from pathlib import Path
from configparser import NoOptionError, NoSectionError
from . import abstract

last_migration = "0.0.0"

class DBPath(abstract.Setting):
    _default = Path(Path.home(), 'fichario.sqlite3')

class DBMigration(abstract.Setting):
    _default = "0.0.1"
