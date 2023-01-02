import sys
from PySide6 import QtWidgets
from package import view

def main():
    app = QtWidgets.QApplication(sys.argv)
    login = view.LoginWindow()
    main_w = view.MainWindow()
    login.show()
    if login.exec() == QtWidgets.QDialog.Accepted:
        print("Loading main window...")
        main_w.show()
        login.close()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
