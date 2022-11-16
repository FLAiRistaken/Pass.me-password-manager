
from package.ui import loginScreen5, createAccScreen
from package import accountCreator, dbConnect, authenitcation
from PySide6.QtWidgets import QWidget, QApplication, QDialog
from PySide6.QtCore import Qt, QCoreApplication, QRegularExpression, Signal
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QRegularExpressionValidator

class LoginWindow(QtWidgets.QDialog, loginScreen5.Ui_Login):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.center()
        self.oldPos = self.pos() 
        
        self.btnCreate.clicked.connect(self.showCreate)
        self.btnLogin.clicked.connect(self.loginButton)
        
        
    def showCreate(self, checked):
        self.w = CreateWindow()
        self.w.show()
        self.close()    
    
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept
    
    def loginButton(self):
        emailval = self.lineEdit_Email.text()
        passval = self.lineEdit_MastPassword.text()
        auth = authenitcation.authentication(emailval, passval)
        if auth.authenticated == True:
            print("Logging in...")
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, "Login Failed", "Logging in failed, please try again"
            )


        

class CreateWindow(QWidget, createAccScreen.Ui_Create):
    def __init__(self, parent=None):
        super(CreateWindow, self).__init__(parent)
        self.setupUi(self)  
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        rx = QRegularExpression("[^@]+@[^@]+\.[^@]+")
        le_email_validator = QRegularExpressionValidator(rx, self.lineEdit_Email)
        self.lineEdit_Email.setValidator(le_email_validator)
        
        self.center()
        self.oldPos = self.pos()
        
        self.btnLogin.clicked.connect(self.showLogin)
        self.btnCreate.clicked.connect(self.createAccButton)
        
    def showLogin(self, checked):
        self.w = LoginWindow()
        self.w.show()
        self.close()   
    
    def createAccButton(self):
        emailval = self.lineEdit_Email.text()
        passval = self.lineEdit_MastPassword.text()
        nameval = self.lineEdit_Name.text() 
        hintval = self.lineEdit_PassHint.text()
        ac = accountCreator.accountCreator(emailval,passval, nameval, hintval)
        db = dbConnect.dbConnect()
        db.new_user( ac.acc)
        
          
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept      
    



def main():
    import sys    
    
    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    if login.exec() == QtWidgets.QDialog.Accepted:
        print("Loading main window...")
    sys.exit(app.exec())    
        
if __name__ == "__main__": main()