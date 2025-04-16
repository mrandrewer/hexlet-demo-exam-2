import os
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import pyqtSlot
from ui.widget import Widget
from ui.dialog import Dialog
from ui.main_window_ui import Ui_MainWindow
from repo import repository as repository
from repo.partner_edit_item import PartnerEditItem


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_setup = Ui_MainWindow()
        ui_setup.setupUi(self)
        self.ui = ui_setup
        icon_path = os.path.normpath(
            os.path.dirname(
                os.path.abspath(__file__)
            ) + "/Лого.png"
        )
        icon = QtGui.QIcon(icon_path)
        self.setWindowIcon(icon)
        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        pic = QtWidgets.QGraphicsPixmapItem()
        self.image_qt = QtGui.QImage(icon_path)
        pic.setPixmap(QtGui.QPixmap.fromImage(self.image_qt))
        self.scene.setSceneRect(0, 0, 48, 48)
        self.scene.addItem(pic)
        self.load_partner_types()
        self.load_records()
        self.ui.list_records.itemDoubleClicked.connect(self.edit_member)
        self.ui.button_add.clicked.connect(self.add_member)

    # Данная функция предназначена для обработки ошибок
    # Это декоратор, оборачивающий обработчики действий пользователя,
    # и отображающий окно ошибки если что-то пошло не так
    def catch_error(operation_name):
        def decorate(f):
            def applicator(*args, **kwargs):
                try:
                    return f(*args,**kwargs)
                except Exception as ex:
                    msg_text = F'При выполнении операции "{operation_name}" произошла ошибка'
                    print(F'{msg_text} {ex}')
                    msg = QtWidgets.QErrorMessage()
                    msg.showMessage(msg_text)
                    msg.exec()
            return applicator
        return decorate

    @catch_error('Загрузка типов партнеров')
    def load_partner_types(self):
        self.partner_types = repository.get_partner_types()

    @catch_error('Загрузка спиcка записей')
    def load_records(self):
        self.ui.list_records.clear()
        self.records = repository.get_records()
        for record in self.records:
            widget = Widget(self, record)
            item = QtWidgets.QListWidgetItem(self.ui.list_records)
            item.setSizeHint(widget.sizeHint())
            item.setData(100, record.id)
            self.ui.list_records.setItemWidget(item, widget)

    @pyqtSlot()
    def edit_member(self):
        self.edit_member_int()

    @catch_error('Изменение записи')
    def edit_member_int(self):
        item = self.ui.list_records.selectedItems()[0]
        record = repository.get_record_by_id(item.data(100))
        dlg = Dialog(self, self.partner_types, record)
        dlg.setWindowTitle("Изменение записи")
        dlg_result = dlg.exec()
        if dlg_result == 1:
            dlg.get_field_values(record)
            repository.update_record_by_id(record)
            self.load_records()

    @pyqtSlot()
    def add_member(self):
        self.add_member_int()

    @catch_error('Добавление записи')
    def add_member_int(self):
        dlg = Dialog(self, self.partner_types)
        dlg.setWindowTitle("Добавление записи")
        dlg_result = dlg.exec()
        if dlg_result == 1:
            member = PartnerEditItem()
            dlg.get_field_values(member)
            repository.create_record(member)
            self.load_records()
