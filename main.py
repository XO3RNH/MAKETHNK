from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from const import *
import sys


class Main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(825, 613)
        main.setStyleSheet("background-color: #f0f0f0;")

        self.logoBar = QGraphicsView(main)
        self.logoBar.setGeometry(QRect(0, 0, 831, 81))
        self.logoBar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0,"
                                   " y1:0, x2:1, y2:0, stop:0 #F0F0F0, stop:0.343284 #fceabb,"
                                   " stop:0.636816 #fad677, stop:1 #f8b500);")
        self.logoBar.setFrameShape(QFrame.StyledPanel)
        self.logoBar.setFrameShadow(QFrame.Plain)
        self.logoBar.setObjectName("logoBar")

        self.generateButton = QPushButton(main)
        self.generateButton.setGeometry(QRect(230, 540, 361, 41))
        self.generateButton.setAutoFillBackground(False)
        self.generateButton.setStyleSheet("QPushButton {\n"
                                          "    background-color: qlineargradient(spread:pad, x1:0,"
                                          " y1:0, x2:1, y2:0, stop:0 #f0f0f0, stop:0.343284 #fceabb,"
                                          " stop:0.636816 #fad677, stop:1 #f8b500);\n"
                                          "    border-style: outset;\n"
                                          "    color: #404040;\n"
                                          "    font: 10pt \"Sitka\";\n"
                                          "    padding: 2px;\n"
                                          "    border-width: 1px;\n"
                                          "    border-radius: 10px;\n"
                                          "    border-color: #404040;\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: qlineargradient(spread:pad, x1:0,"
                                          " y1:0, x2:1, y2:0, stop:0 #c8c8c8, stop:0.343284 #f2c293,"
                                          " stop:0.636816 #d29a4f, stop:1 #d08d00);\n}")
        self.generateButton.setDefault(False)
        self.generateButton.setFlat(False)
        self.generateButton.setObjectName("generateButton")
        self.generateButton.clicked.connect(lambda: self.generate())

        self.radioButton1 = QRadioButton(main)
        self.radioButton1.setGeometry(QRect(50, 200, 340, 61))
        self.radioButton1.setStyleSheet("color: #404040;\n"
                                        "font: 9pt \"Sitka\";")
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton2 = QRadioButton(main)
        self.radioButton2.setGeometry(QRect(500, 200, 340, 61))
        self.radioButton2.setStyleSheet("color: #404040;\n"
                                        "font: 9pt \"Sitka\";")
        self.radioButton2.setObjectName("radioButton2")
        self.radioButton3 = QRadioButton(main)
        self.radioButton3.setGeometry(QRect(50, 270, 340, 61))
        self.radioButton3.setStyleSheet("color: #404040;\n"
                                        "font: 9pt \"Sitka\";")
        self.radioButton3.setObjectName("radioButton3")
        self.radioButton4 = QRadioButton(main)
        self.radioButton4.setGeometry(QRect(500, 270, 340, 61))
        self.radioButton4.setStyleSheet("color: #404040;\n"
                                        "font: 9pt \"Sitka\";")
        self.radioButton4.setObjectName("radioButton4")

        self.label = QLabel(main)
        self.label.setGeometry(QRect(260, 100, 351, 41))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                 "color: #404040;\n"
                                 "font: 16pt \"Sitka\";")
        self.label.setObjectName("label")

        self.logo = QLabel(main)
        self.logo.setGeometry(QRect(30, 20, 201, 41))
        self.logo.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                "color: #404040;\n"
                                "font: 16pt \"Sitka\";")
        self.logo.setObjectName("logo")

        self.retranslateUi(main)
        QMetaObject.connectSlotsByName(main)

    def generate(self):
        if self.radioButton1.isChecked() or self.radioButton2.isChecked() or self.radioButton3.isChecked() or self.radioButton4.isChecked():
            htmlFile = 'template.html'
            cssFile = 'style.css'
            jsFile = 'script.js'

            message = QMessageBox()
            message.setWindowTitle("MAKETHNK")
            message.setText("The template has been successfully generated!")
            message.setIcon(QMessageBox.Information)

            if self.radioButton1.isChecked():
                with open(htmlFile, mode='w') as f:
                    f.write(defaultHTML)
                with open(cssFile, 'w') as f:
                    f.write(defaultStyle)
                with open(jsFile, 'w') as f:
                    f.write(defaultScript)
                message.exec_()
            elif self.radioButton2.isChecked():
                with open(htmlFile, mode='w') as f:
                    f.write(bootstrapHTML)
                with open(jsFile, 'w') as f:
                    f.write(defaultScript)
                message.exec_()
            elif self.radioButton3.isChecked():
                with open(htmlFile, mode='w') as f:
                    f.write(businessCardHTML)
                with open(cssFile, 'w') as f:
                    f.write(businessCardStyle)
                with open(jsFile, 'w') as f:
                    f.write(defaultScript)
                message.exec_()
            elif self.radioButton4.isChecked():
                with open(htmlFile, mode='w') as f:
                    f.write(sigInHTML)
                with open(cssFile, 'w') as f:
                    f.write(sigInStyle)
                with open(jsFile, 'w') as f:
                    f.write(defaultScript)
                message.exec_()
        else:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("You didn't choose a template!")
            error.setIcon(QMessageBox.Critical)
            error.exec_()

    def retranslateUi(self, main):
        _translate = QCoreApplication.translate
        main.setWindowTitle(_translate("main", "MAKETHNK"))
        self.generateButton.setText(_translate("main", "Generate"))
        self.radioButton1.setText(_translate("main", "Standard template"))
        self.radioButton2.setText(_translate("main", "Standard template with Bootstrap"))
        self.radioButton3.setText(_translate("main", "Business card website template (Bootstrap)"))
        self.radioButton4.setText(_translate("main", "Sig-in form template (Bootstrap)"))
        self.label.setText(_translate("main", "Choose your template"))
        self.logo.setText(_translate("main", "MAKETHNK"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Images\logo.png'))
    dialog = QDialog()
    main = Main()
    main.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())