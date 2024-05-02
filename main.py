"""
helpers and utils
=================

Pyzza relies heavily on gtfs_kit and expands its capabilities.
https://mrcagney.github.io/gtfs_kit_docs/
"""

from datetime import datetime
from pathlib import Path
import pandas as pd
import gtfs_kit as gk
from .constants import ZAZIE_DIR


class Repo:
    """
    defines the Repo object with its properties and methods
    """

    def __init__(self, zazie_dir=ZAZIE_DIR):
        # reldir hosts all releases of zazie
        self.reldir = Path(zazie_dir)
        # latest release: based on release timestamp
        self.latest_release = sorted([
            x for x in (self.reldir/'releases').iterdir() if x.is_dir()])[-1]
        # get a feed list
        zip_dir = self.latest_release/'otp/graphs/current'
        # load feeds in a list
        self.feeds = [
            gk.read_feed(azip, dist_units='m')
            for azip in (zip_dir).glob('*.zip')
            if can_be_feed(azip)]

    def summary_to_markdown(self, dest=None):
        """exports feed summaries as markdown"""
        dest = self.latest_release if dest is None else dest
        sd = datetime.now().strftime("%Y%m%d")
        descriptions = pd.concat(
            [f.describe(sample_date=sd).set_index('indicator').T for f in self.feeds],
            ignore_index=True).set_index('agencies')
        with open(dest/'synthese.md', 'w', encoding="utf-8") as f:
            f.write(descriptions.to_markdown())
        return f'summary printed:\n {dest/"otp/graphs/current/synthese.md"}'


def can_be_feed(some_zip):
    """will return true if zome_zip contains required files"""
    required_files = set([
        'agency.txt', 'stops.txt', 'routes.txt',
        'trips.txt', 'stop_times.txt'])
    return required_files.issubset(gk.list_feed(some_zip)['file_name'])
