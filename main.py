"""
    Main  
"""

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtUiTools, QtGui, QtWidgets
from singleLinkedList import SingleLinkedList
from singleLinkedList import ListNode
from mainwindow import Ui_MainWindow
import sys
import os


class mainApp(Ui_MainWindow):
    # Linked list.
    lList = SingleLinkedList()

    def __init__(self, window):
        self.setupUi(window)

        # Connect button to functions.
        self.addPushButton.clicked.connect(self.addUserInputToList)
        self.removePushButton.clicked.connect(self.removeUserInputFromList)
        self.findPushButton.clicked.connect(self.findUserInputFromList)

    def addUserInputToList(self):
        # Get inputPlainTextEdit string
        userInput = self.inputPlainTextEdit.toPlainText()

        # Print list.
        self.label_2.setText("List Before Operation")
        self.beforeTextEdit.setPlainText(str(self.lList.output_list()))
        #  Add user input to list.
        self.lList.add_list_item(ListNode(userInput))
        # Print new/current list.
        self.currentTextEdit.setPlainText(str(self.lList.output_list()))

    def removeUserInputFromList(self):
        # Get inputPlainTextEdit string
        userInput = self.inputPlainTextEdit.toPlainText()

        # Print list.
        self.label_2.setText("List Before Operation")
        self.beforeTextEdit.setPlainText(str(self.lList.output_list()))
        # Remove user input to list.
        self.lList.remove_list_item_by_value(userInput)
        # Print new/current list.
        self.currentTextEdit.setPlainText(str(self.lList.output_list()))

    def findUserInputFromList(self):
        # Get inputPlainTextEdit string
        userInput = self.inputPlainTextEdit.toPlainText()

        # Print current list.
        self.currentTextEdit.setPlainText(str(self.lList.output_list()))
        self.label_2.setText("Element current position")
        # Print position of item in list.
        self.beforeTextEdit.setPlainText("Position: " + str(self.lList.unordered_search(userInput)))
        

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # Create an instance and show the form
    ui = mainApp(MainWindow)

    # show the window and start the app
    MainWindow.show()
    app.exec_()
