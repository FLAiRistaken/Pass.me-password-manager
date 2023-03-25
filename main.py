import sys, atexit
from PySide6 import QtWidgets
from package import view

def delete_cache():
    import os
    try:
        os.remove('cache.json')
        print('Cache file deleted... Exiting...')
    except FileNotFoundError:
        print('Cache file not found... Exiting...')

def main():
    atexit.register(delete_cache)
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