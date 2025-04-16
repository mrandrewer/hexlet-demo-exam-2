import datetime
from PyQt6 import QtWidgets
from ui.dialog_ui import Ui_Dialog
from repo.partner_edit_item import PartnerEditItem


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent, partner_types, record: PartnerEditItem = None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.set_partner_types(partner_types)
        self.set_fields(record)

    def set_partner_types(self, partner_types):
        self.ui.combo_box_type.addItem("", -1)
        for p_type in partner_types:
            self.ui.combo_box_type.addItem(p_type.name, p_type.id)

    def set_fields(self, record: PartnerEditItem):
        if record is None:
            return
        self.ui.combo_box_type.setCurrentIndex(record.type)
        self.ui.line_edit_name.setText(record.partner_name)
        self.ui.line_edit_director.setText(record.director_name)
        self.ui.line_edit_email.setText(record.email)
        self.ui.line_edit_phone.setText(record.phone)
        self.ui.text_edit_address.setText(record.address)
        self.ui.spin_box_rating.setValue(record.rating)

    def get_field_values(self, record: PartnerEditItem):
        if record is None:
            return
        record.type = self.ui.combo_box_type.currentIndex()
        record.partner_name = self.ui.line_edit_name.text()
        record.director_name = self.ui.line_edit_director.text()
        record.email = self.ui.line_edit_email.text()
        record.phone = self.ui.line_edit_phone.text()
        record.address = self.ui.text_edit_address.toPlainText()
        record.rating = self.ui.spin_box_rating.value()

    def accept(self):
        if self.ui.combo_box_type.currentIndex() <= 0:
            msg = QtWidgets.QErrorMessage(self)
            msg.showMessage('Необходимо заполнить тип партнера!')
            msg.exec()
            return
        if self.ui.line_edit_name.text() == '' or self.ui.line_edit_name.text() == None:
            msg = QtWidgets.QErrorMessage(self)
            msg.showMessage('Необходимо заполнить имя партнера!')
            msg.exec()
            return
        super().accept()
