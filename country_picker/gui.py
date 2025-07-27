# gui.py
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout
from PyQt5.QtCore import QThread
from country_picker.worker import CountryFetcher  # Background data fetcher

def run_app():
    """Launches the Country Picker GUI application."""
    app = QApplication([])

    # ------ Main Window Setup ------
    window = QWidget()
    window.setWindowTitle("Country Picker")
    window.setMinimumSize(300, 150)

    layout = QVBoxLayout()  # Initializes a vertical layout

    # Dropdown menu used to populate with country names
    combo = QComboBox()

    # The label that gets updated when a user picks a country
    label = QLabel("Please select a country.")

    # Add both widgets to the vertical layout
    layout.addWidget(combo)
    layout.addWidget(label)

    window.setLayout(layout)  # Apply the layout to the main window
    window.show()             # Display the window

    # ------ Label Update Logic ------
    def on_country_changed(index: int):
        """
        Updates the label when the selected country changes.

        Parameters:
        index (int): Index of the selected item in the combo box.
        """
        selected_country = combo.itemText(index)
        label.setText(f"Selected: {selected_country}")

    # Connect signal to update label when selection changes
    # currentIndexChanged SIGNAL emits the new index (an int)
    combo.currentIndexChanged.connect(on_country_changed)

    # ------ Background Fetching of Country Data ------
    fetcher = CountryFetcher()        # Create instance of the worker
    thread = QThread()                # Create a new thread
    fetcher.moveToThread(thread)      # Move the worker to the background thread

    # When the thread starts, run the fetcher
    thread.started.connect(fetcher.run)

    def on_fetch_finished(countries: list):
        """
        Callback when country data is fetched.

        Populates the combo box and stops the background thread.
        """
        combo.addItems(countries)  # Populate combo box with fetched countries
        thread.quit()              # Stop the thread
        thread.wait()              # Wait for cleanup

    # Connect fetcher's finished signal to combo box population
    fetcher.finished.connect(on_fetch_finished)

    thread.start()  # Start the background thread

    app.exec_()  # Start the Qt event loop
