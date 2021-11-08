import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from speachtotext1 import assisatant


class Worker(QObject):
    finished = pyqtSignal()

    def callassistent(self,text_area,speach_button,exit_button,speach_label,message,enter_button):
      assisatant(text_area=text_area,speach_button=speach_button,exit_button=exit_button,speach_label=speach_label,message=message,enter_button=enter_button)
      self.finished.emit()

class GUI():
  def __init__(self):
    self.setupwindow()
    self.runTask()
    sys.exit(self.app.exec_())

  
  def setupwindow(self):
    self.app = QApplication(sys.argv)
    self.text_area = QTextEdit()
    self.text_area.setFocusPolicy(Qt.NoFocus)
    self.message = QLineEdit()
    self.speach_button = QPushButton()
    self.speach_button.setText("Click button to speak")
    self.layout = QVBoxLayout()
    self.speach_label = QLabel()
    self.speach_label.setText("Speack now")
    self.exit_button = QPushButton()
    self.exit_button.setText("Exit")
    self.enter_button = QPushButton()
    self.enter_button.setText("Ok")
    self.message.returnPressed.connect(self.enter_button.click)
    self.layout.addWidget(self.text_area)
    self.layout.addWidget(self.message)
    self.layout.addWidget(self.speach_button)
    self.layout.addWidget(self.speach_label)
    self.layout.addWidget(self.exit_button)
    self.window = QWidget()
    self.window.setLayout(self.layout)
    self.window.show()
    self.speach_label.hide()
    self.exit_button.hide()

  
  def runTask(self):
    # Step 2: Create a QThread object
    self.thread = QThread()
    # Step 3: Create a worker object
    self.worker = Worker()
    # Step 4: Move worker to the thread
    self.worker.moveToThread(self.thread)
    # Step 5: Connect signals and slots
    self.thread.started.connect(lambda:self.worker.callassistent(text_area=self.text_area,speach_button=self.speach_button,exit_button=self.exit_button,speach_label=self.speach_label,message=self.message,enter_button=self.enter_button))
    self.worker.finished.connect(self.thread.quit)
    self.worker.finished.connect(self.worker.deleteLater)
    self.thread.finished.connect(self.thread.deleteLater)
    # Step 6: Start the thread
    self.thread.start()

if __name__ == '__main__':
  p1 = GUI()
  
  