#pyqt

import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv) # application

window = QWidget() # window
layout = QHBoxLayout() # layout of the window

# grade marking function
def search():
    try: # catch errors
        target = int(entry.text()) # parse integer entry
        lst = [1,2,3,4,5]
        mid = (len(lst)-1)//2
        while True:
            if target == lst[mid]:
                msg.setText("Found")
                return
            elif target < lst[mid]:
                if mid//2 == mid:
                    msg.setText("Not Found")
                    return
                mid = mid//2
            elif target > lst[mid]:
                if (len(lst)-mid)//2 + mid == mid:
                    msg.setText("Not Found")
                    return
                mid = (len(lst)-mid)//2 + mid
                
    except Exception as e:
        # error text
        msg.setText("Error")
        
#to make button
leftButton = QPushButton("Search")

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
leftButton.clicked.connect(search)

#set the title of the window
window.setWindowTitle('Binary Search')
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
