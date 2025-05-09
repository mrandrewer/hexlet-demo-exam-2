# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(569, 640)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(103, 186, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 232, 211))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 186, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 232, 211))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 232, 211))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        Dialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_type = QtWidgets.QLabel(parent=Dialog)
        self.label_type.setObjectName("label_type")
        self.verticalLayout.addWidget(self.label_type)
        self.combo_box_type = QtWidgets.QComboBox(parent=Dialog)
        self.combo_box_type.setObjectName("combo_box_type")
        self.verticalLayout.addWidget(self.combo_box_type)
        self.label_name = QtWidgets.QLabel(parent=Dialog)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.line_edit_name = QtWidgets.QLineEdit(parent=Dialog)
        self.line_edit_name.setObjectName("line_edit_name")
        self.verticalLayout.addWidget(self.line_edit_name)
        self.label_director = QtWidgets.QLabel(parent=Dialog)
        self.label_director.setObjectName("label_director")
        self.verticalLayout.addWidget(self.label_director)
        self.line_edit_director = QtWidgets.QLineEdit(parent=Dialog)
        self.line_edit_director.setObjectName("line_edit_director")
        self.verticalLayout.addWidget(self.line_edit_director)
        self.label_email = QtWidgets.QLabel(parent=Dialog)
        self.label_email.setObjectName("label_email")
        self.verticalLayout.addWidget(self.label_email)
        self.line_edit_email = QtWidgets.QLineEdit(parent=Dialog)
        self.line_edit_email.setObjectName("line_edit_email")
        self.verticalLayout.addWidget(self.line_edit_email)
        self.label_phone = QtWidgets.QLabel(parent=Dialog)
        self.label_phone.setObjectName("label_phone")
        self.verticalLayout.addWidget(self.label_phone)
        self.line_edit_phone = QtWidgets.QLineEdit(parent=Dialog)
        self.line_edit_phone.setObjectName("line_edit_phone")
        self.verticalLayout.addWidget(self.line_edit_phone)
        self.label_address = QtWidgets.QLabel(parent=Dialog)
        self.label_address.setObjectName("label_address")
        self.verticalLayout.addWidget(self.label_address)
        self.text_edit_address = QtWidgets.QTextEdit(parent=Dialog)
        self.text_edit_address.setObjectName("text_edit_address")
        self.verticalLayout.addWidget(self.text_edit_address)
        self.label_rating = QtWidgets.QLabel(parent=Dialog)
        self.label_rating.setObjectName("label_rating")
        self.verticalLayout.addWidget(self.label_rating)
        self.spin_box_rating = QtWidgets.QSpinBox(parent=Dialog)
        self.spin_box_rating.setMinimum(1)
        self.spin_box_rating.setMaximum(10)
        self.spin_box_rating.setObjectName("spin_box_rating")
        self.verticalLayout.addWidget(self.spin_box_rating)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Редактирование партнера"))
        self.label_type.setText(_translate("Dialog", "Тип"))
        self.label_name.setText(_translate("Dialog", "Нименование"))
        self.label_director.setText(_translate("Dialog", "Директор"))
        self.label_email.setText(_translate("Dialog", "EMail"))
        self.label_phone.setText(_translate("Dialog", "Телефон"))
        self.label_address.setText(_translate("Dialog", "Адрес"))
        self.label_rating.setText(_translate("Dialog", "Рейтинг"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
