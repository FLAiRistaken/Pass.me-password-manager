import sys, atexit
from PySide6 import QtWidgets
from package import view

def delete_caches():
    import os
    try:
        os.remove('cache.json')
        print('Cache file deleted... Exiting...')
    except FileNotFoundError:
        print('Cache file not found... Exiting...')

def main():
    atexit.register(delete_caches)
    app = QtWidgets.QApplication(sys.argv)
    login = view.LoginWindow()
    main_w = view.MainWindow()
    login.show()
    if login.exec() == QtWidgets.QDialog.Accepted:
        print("Loading main window...")
        main_w.show()
        login.close()
    app.focusChanged.connect(main_w.on_focus_changed)
    sys.exit(app.exec())
if __name__ == "__main__":
    main()