#pyqt

import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv) # application

window = QWidget() # window
layout = QHBoxLayout() # layout of the window

# grade marking function
def grade():
    try: # catch errors
        intScore = int(entry.text()) # parse integer entry
        strGrade = None # string for letter grade
        # assign grade with if else statement
        if intScore < 50:
            strGrade = "N"
        elif intScore < 60:
            strGrade = "D"
        elif intScore < 70:
            strGrade = "C"
        else:
            strGrade = "B"
        # check for boundary error
        if intScore > 100 or intScore < 0:
            raise "boundary error"
        # set label text
        msg.setText("Grade: {}".format(strGrade))
    except Exception as e:
        # error text
        msg.setText("Error")
        
#to make button
leftButton = QPushButton("Mark")

#make a label called msg which starts of as blank 
msg = QLabel("")
#make a text field
entry = QLineEdit()

#add the left button to the layout
layout.addWidget(leftButton)
#add the label called msg to the layout
layout.addWidget(msg)
#add the text field to the layout
layout.addWidget(entry)
#add the layout to the window
window.setLayout(layout)

#call to subroutine "greeting" when left button is clicked
leftButton.clicked.connect(grade)

#set the title of the window
window.setWindowTitle('Grade Marker')
#setting dimensions of the window
window.setGeometry(200, 100, 280, 80)
#setting position of window relative to the screen (19 pixels from left, 15 from top)
window.move(19, 15)
#label called helloMsg as "heading" text
#helloMsg = QLabel('<h2>Hello World!</h2>', parent=window)
#setting position of label relative to window (160 from left of window, 15 from top of window)
#helloMsg.move(160, 15)

window.show() # show window
sys.exit(app.exec()) # run app and exit with error code
