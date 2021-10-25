from qtpy import QtWidgets, QtCore
import sys

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__()
        self.setWindowTitle("Hello world!")
        
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        layout = QtWidgets.QVBoxLayout()
        widget.setLayout(layout)
        
        self.label = QtWidgets.QLabel("A qt GUI", self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.label)
        
        self.greet_button = QtWidgets.QPushButton("Greet", self)
        self.greet_button.clicked.connect(self.greet)
        layout.addWidget(self.greet_button)
        
        self.close_button = QtWidgets.QPushButton("Close", self)
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)
        
    def greet(self, widget, callback_data=None):
        print("Greetings!")
        
    def quit(self):
        self.app.exit()
        
app = QtWidgets.QApplication(sys.argv)
      
if __name__ == "__main__": 
    win = MainWindow(app)
    win.show()
    app.exec_()