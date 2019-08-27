# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_image2text.ui'
#
# Created: Tue Jul 10 20:15:37 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_image2textWidget(object):
    def setupUi(self, image2textWidget):
        image2textWidget.setObjectName("image2textWidget")
        # image2textWidget.resize(611, 330)
        image2textWidget.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(image2textWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(image2textWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonOpen = QtWidgets.QPushButton(image2textWidget)
        self.pushButtonOpen.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButtonOpen.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButtonOpen.setObjectName("pushButtonOpen")


        self.horizontalLayout.addWidget(self.pushButtonOpen)
        # self.horizontalLayout.addWidget(self.pushButtonOpen1)

        self.pushButtonCapture = QtWidgets.QPushButton(image2textWidget)
        self.pushButtonCapture.setMinimumSize(QtCore.QSize(120, 60))
        self.pushButtonCapture.setMaximumSize(QtCore.QSize(120, 60))
        self.pushButtonCapture.setObjectName("pushButtonCapture")
        self.horizontalLayout.addWidget(self.pushButtonCapture)

        self.pushButtonCapture1 = QtWidgets.QPushButton(image2textWidget)
        self.pushButtonCapture1.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButtonCapture1.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButtonCapture1.setObjectName("pushButtonCapture1")
        self.horizontalLayout.addWidget(self.pushButtonCapture1)


        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(image2textWidget)
        QtCore.QMetaObject.connectSlotsByName(image2textWidget)

    def retranslateUi(self, image2textWidget):
        _translate = QtCore.QCoreApplication.translate
        image2textWidget.setWindowTitle(_translate("image2textWidget", "Form"))
        self.pushButtonOpen.setText(_translate("image2textWidget", "Open"))
        self.pushButtonCapture.setText(_translate("image2textWidget", "cap"))

