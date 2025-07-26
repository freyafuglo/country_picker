# gui.py
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout

def run_app():
    app = QApplication([]) # creates an instance of the application

    window = QWidget()
    window.setWindowTitle("Country Picker") # main window

    layout = QVBoxLayout() # initializes a vertical layout

    combo = QComboBox() # the dropdown menu used to populate with country names
    label = QLabel("Selected: <country>") # the label that gets updated when a user picks a country

    layout.addWidget(combo) # adds both widgets to the vertical layout
    layout.addWidget(label)

    window.setLayout(layout) # applies the layout to the main window
    window.show() # displays the window
    app.exec_() # starts the event loop
