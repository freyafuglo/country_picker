# worker.py
from PyQt5.QtCore import QObject, pyqtSignal
import requests
from typing import List

API_URL = "https://www.apicountries.com/countries"


class CountryFetcher(QObject):
    """
    A QObject subclass to fetch country data in a background thread.

    Emits:
        finished (list[str]): A signal emitted with a list of country names when the fetch is complete.
    """

    finished = pyqtSignal(list)

    def run(self) -> None:
        """
        Performs the network request to fetch countries.
        Emits the 'finished' signal with a sorted list of country names, or an empty list on error.
        """
        try:
            response = requests.get(API_URL, timeout=10)
            response.raise_for_status() # Raise error for bad status codes
            data = response.json()
            countries: List[str] = sorted([c["name"] for c in data])
            self.finished.emit(countries)
        except Exception as e:
            print(f"Fetch failed: {e}")
            self.finished.emit([])
