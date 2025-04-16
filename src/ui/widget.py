from PyQt6 import QtWidgets
from ui.widget_ui import Ui_Form as Ui_Widget
from repo.partner_list_item import PartnerListItem


class Widget(QtWidgets.QWidget):
    def __init__(self, parent, record: PartnerListItem):
        super().__init__(parent)
        ui_setup = Ui_Widget()
        ui_setup.setupUi(self)
        self.ui = ui_setup
        self.set_fields(record)

    def set_fields(self, record: PartnerListItem):
        self.ui.label_name.setText(record.partner_display_name)
        self.ui.label_discount.setText(record.discount_display_value)
        self.ui.label_director.setText(record.director_name)
        self.ui.label_phone.setText(record.phone)
        self.ui.label_rating.setText(record.rating_display_value)
