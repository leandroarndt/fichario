from pathlib import Path
from . import storage

class DB(object):
    _config: storage.AppSettings
    
    def __init__(self):
        self._config = storage.AppSettings()
    
    def get_db_path(self) -> Path:
        """Returns a Path object to the configured database file.

        Returns:
            Path: Path object to the configured database file
        """
        try:
            return self._config.db_path
        except AttributeError: # Not configured, use default
            return Path(Path.home(), 'fichario.sqlite3')

    def set_db_path(self, path:str|Path):
        """Set database path and moves it to new location or creates it.

        Args:
            path (str | Path): Path to new database location
        """
        self._config.db_path = path

    #TODO: web dav synchronization
    def sync_db(self):
        """Syncs database with web dav storage.
        """
        raise NotImplemented
