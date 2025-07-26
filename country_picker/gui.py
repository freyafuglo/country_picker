# gui.py
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout
from country_picker.data import fetch_country_names

def run_app():
    app = QApplication([]) # creates an instance of the application

    window = QWidget()
    window.setWindowTitle("Country Picker") # main window

    layout = QVBoxLayout() # initializes a vertical layout

    combo = QComboBox() # the dropdown menu used to populate with country names
    label = QLabel("Selected: <country>") # the label that gets updated when a user picks a country

    # adds both widgets to the vertical layout
    layout.addWidget(combo)
    layout.addWidget(label)

    window.setLayout(layout) # applies the layout to the main window
    window.show() # displays the window


    # fetch country names from API
    countries = fetch_country_names()
    combo.addItems(countries)  # Populate combo box

    # update label when selection changes
    def on_country_changed(index):
        selected_country = combo.itemText(index)
        label.setText(f"Selected: {selected_country}")

    # currentIndexChanged SIGNAL emits the new index (an int)
    # automatically when the user changes the selection.
    combo.currentIndexChanged.connect(on_country_changed)


    app.exec_() # starts the event loop
