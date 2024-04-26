"""
helpers and utils
=================

Pyzza relies heavily on gtfs_kit and expands its capabilities.
https://mrcagney.github.io/gtfs_kit_docs/

get_expiry:
    will return expiry dates for all agencies
"""

from pathlib import Path
from .constants import ZAZIE_DIR

class Repo:
    """
    defines the Repo object with its properties and methods
    """

    def __init__(self, zazie_dir=ZAZIE_DIR):
        self.reldir = Path(zazie_dir)
        self.latest_release = sorted([
            x for x in self.reldir.iterdir() if x.is_dir()])[-1]

    def get_expiry(self, agency=None):
        """gets expiry date"""
        return agency
