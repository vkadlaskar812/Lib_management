# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 170)
        self.del_buttonbox = QtWidgets.QDialogButtonBox(Dialog)
        self.del_buttonbox.setGeometry(QtCore.QRect(80, 90, 341, 32))
        self.del_buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.del_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.del_buttonbox.setObjectName("del_buttonbox")
        self.del_dialog = QtWidgets.QTextBrowser(Dialog)
        self.del_dialog.setGeometry(QtCore.QRect(20, 20, 401, 61))
        self.del_dialog.setObjectName("del_dialog")

        self.retranslateUi(Dialog)
        self.del_buttonbox.accepted.connect(Dialog.accept)
        self.del_buttonbox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.del_dialog.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Are you sure you want to delete this book?</span></p></body></html>"))
