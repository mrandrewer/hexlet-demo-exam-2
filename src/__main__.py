import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    result = app.exec()
    sys.exit(result)


if __name__ == '__main__':
    main()
