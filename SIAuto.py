# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from lib.Penilaian import Ui_Dialog

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import datetime
import platform

class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.array = []

        self.qr = self.centralwidget.frameGeometry()
        self.centerpoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        self.qr.moveCenter(self.centerpoint)
        self.centralwidget.move(self.qr.topLeft())


        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.labels()
        self.entry()
        self.checkBoxes()
        self.radioButton()
        self._date()
        self.buttons()
        self.menuBar(MainWindow)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _date(self):
        x = datetime.datetime.now()

        self.curr_month = x.month
        self.curr_year  = x.year

        sem_ganjil = [7, 8, 9, 10, 11, 12]
        sem_genap  = [1, 2, 3,  4,  5,  6]

        for i in sem_ganjil:
            if i == self.curr_month:
                isGanjil = True
                break
            else:
                isGanjil = False

        for i in sem_genap:
            if i == self.curr_month:
                isGenap = True
                break
            else:
                isGenap = False

        if self.curr_month == 1:
            self.radioButton1.setChecked(True)
            self.curr_year += -1
        elif isGanjil == True:
            print("Tahun Ajaran %i/%i Semester 1" %(self.curr_year, self.curr_year+1))
            self.semester = "ganjil"
            self.radioButton1.setChecked(True)
        elif isGenap == True:
            print("Tahun Ajaran %i/%i Semester 2" %(self.curr_year-1, self.curr_year))
            self.semester = "genap"
            self.curr_year -= 1
            self.radioButton2.setChecked(True)

    """
    GUI PART
    """

    def labels(self):
        self.tahunAjaran = QtWidgets.QLabel(self.centralwidget)
        self.tahunAjaran.setGeometry(QtCore.QRect(330, 10, 160, 17))
        self.tahunAjaran.setObjectName("tahunAjaran")

        self.penilaianLabel = QtWidgets.QLabel(self.centralwidget)
        self.penilaianLabel.setGeometry(QtCore.QRect(270, 140, 151, 17))
        self.penilaianLabel.setObjectName("penilaianLabel")

        self.semesterLabel = QtWidgets.QLabel(self.centralwidget)
        self.semesterLabel.setGeometry(QtCore.QRect(270, 210, 151, 17))
        self.semesterLabel.setObjectName("penilaianLabel")

    def entry(self):
        # Username
        self.usernameForm = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameForm.setGeometry(QtCore.QRect(270, 40, 271, 25))
        self.usernameForm.setTabletTracking(False)
        self.usernameForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usernameForm.setAutoFillBackground(False)
        self.usernameForm.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.usernameForm.setClearButtonEnabled(False)
        self.usernameForm.setObjectName("usernameForm")
        self.usernameForm.setText("")

        # Password
        self.passwordForm = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordForm.setGeometry(QtCore.QRect(270, 80, 271, 25))
        self.passwordForm.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.passwordForm.setAcceptDrops(True)
        self.passwordForm.setText("")
        self.passwordForm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordForm.setObjectName("passwordForm")
        self.passwordForm.setText("")

    def checkBoxes(self):
        # CheckBox 1
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox1.setGeometry(QtCore.QRect(270, 160, 34, 23))
        self.checkBox1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox1.stateChanged.connect(lambda: self._toggleButton(self.checkBox1, "1"))

        # CheckBox 2
        self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox2.setGeometry(QtCore.QRect(330, 160, 34, 23))
        self.checkBox2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox2.stateChanged.connect(lambda: self._toggleButton(self.checkBox2, "2"))

        # CheckBox 3
        self.checkBox3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox3.setGeometry(QtCore.QRect(390, 160, 34, 23))
        self.checkBox3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox3.stateChanged.connect(lambda: self._toggleButton(self.checkBox3, "3"))

        # CheckBox 4
        self.checkBox4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox4.setGeometry(QtCore.QRect(450, 160, 34, 23))
        self.checkBox4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox4.setObjectName("checkBox4")
        self.checkBox4.stateChanged.connect(lambda: self._toggleButton(self.checkBox4, "4"))

        # CheckBox 5
        self.checkBox5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox5.setGeometry(QtCore.QRect(510, 160, 34, 23))
        self.checkBox5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox5.setObjectName("checkBox5")
        self.checkBox5.stateChanged.connect(lambda: self._toggleButton(self.checkBox5, "5"))
        

    def radioButton(self):
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(270, 230, 151, 17))
        self.radioButton1.setObjectName("radioButton1")
        # self.radioButton1.toggled.connect(lambda : self._toggleRadioButton(self.radioButton1, "Ganjil"))

        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton2.setGeometry(QtCore.QRect(350, 230, 151, 17))
        self.radioButton2.setObjectName("radioButton2")
        # self.radioButton2.toggled.connect(lambda : self._toggleRadioButton(self.radioButton2, "Genap"))

    def buttons(self):
        # Sign In Button
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setEnabled(True)
        self.signInButton.setGeometry(QtCore.QRect(270, 280, 271, 25))
        self.signInButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signInButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.signInButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.signInButton.setFlat(False)
        self.signInButton.setObjectName("signInButton")

        self.signInButton.clicked.connect(self._sign_in)

    def menuBar(self, MainWindow):

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
 
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.actionPenilaian = QtWidgets.QAction(MainWindow)
        self.actionPenilaian.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionPenilaian.setObjectName("actionPenilaian")
        self.actionPenilaian.triggered.connect(self.helpWindow)

        self.menuHelp.addAction(self.actionPenilaian)
        self.menubar.addAction(self.menuHelp.menuAction())

    def helpWindow(self):
        self.ui = Ui_Dialog()
        self.ui.Dialog.show()
      
    def retranslateUi(self, MainWindow):
        year = "Tahun ajaran " + str(self.curr_year) + "/" + str(self.curr_year+1)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIAuto Fill Kuesioner"))

        self.tahunAjaran.setText(_translate("MainWindow", year))

        self.usernameForm.setPlaceholderText(_translate("MainWindow", "Username"))
        self.passwordForm.setPlaceholderText(_translate("MainWindow", "Password"))

        self.penilaianLabel.setText(_translate("MainWindow", "Penilaian Kuisioner"))

        self.checkBox1.setText(_translate("MainWindow", "1"))
        self.checkBox2.setText(_translate("MainWindow", "2"))
        self.checkBox3.setText(_translate("MainWindow", "3"))
        self.checkBox4.setText(_translate("MainWindow", "4"))
        self.checkBox5.setText(_translate("MainWindow", "5"))

        self.semesterLabel.setText(_translate("MainWindow", "Semester"))

        self.radioButton1.setText(_translate("MainWindow", "Ganjil"))
        self.radioButton2.setText(_translate("MainWindow", "Genap"))

        self.signInButton.setText(_translate("MainWindow", "Sign In"))

        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

        self.actionPenilaian.setText(_translate("MainWindow", "Penilaian"))

        self.actionPenilaian.setShortcut(_translate("MainWindow", "Ctrl+H"))


    """
    DRIVER PART
    """
    def _toggleButton(self, checkButton, value):
        if checkButton.isChecked() == True:
            self.array.append(value)
        else:
            self.array.remove(value)
        self.array.sort()
        print("List Jawaban: ", end=' ')
        for i in self.array:
            print(i, end=', ')
        print('\n')
        

    def _sign_in(self, widget):
        print("=> Membuka Driver")

        os = platform.system()

        try:
            if os == 'Linux':
                self.driver = webdriver.Chrome("web_driver/chromedriver")
            elif os == 'Windows':
                self.driver = webdriver.Chrome("web_driver/chromedriver.exe")
        except:
            pass


        self.driver.maximize_window()
        self.driver.get("https://sia.unmul.ac.id/home")
        self.driver.implicitly_wait(30)

        # print(self.usernameForm.text())
        # print(self.passwordForm.text())

        username_form = self.driver.find_element_by_id("exampleInputEmail")
        username_form.send_keys(self.usernameForm.text())

        password_form = self.driver.find_element_by_id("exampleInputPassword")
        password_form.send_keys(self.passwordForm.text())

        code_text = self.driver.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(1)").text

        security_code_form = self.driver.find_element_by_css_selector("div.form-group:nth-child(4) > input:nth-child(1)")
        security_code_form.send_keys(code_text)

        sign_button = self.driver.find_elements_by_xpath("/html/body/div/div/div/div/div/form/div[5]/button")[0]
        sign_button.click()

        print("\nBerhasil Login!!!")

        self._after_login()

    def _after_login(self):
        self.action = ActionChains(self.driver)
        
        hasil_studi = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div/ul/li[4]")
        self.action.move_to_element(hasil_studi).click(hasil_studi).perform()

        khs         = self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div/ul/li[4]/ul/li")
        self.action.move_to_element(khs).click(khs).perform()

        self._khs_pages()


    def _khs_pages(self):

        run = True
        
        while (run == True):
            self.action = ActionChains(self.driver)
            

            if (self.radioButton1.isChecked() != False) and (self.curr_month < 7):
                self.driver.execute_script(open("./js/khs_page_jan.js").read())

            elif (self.radioButton2.isChecked() != False) and (self.curr_month < 7):
                self.driver.execute_script(open("./js/khs_page_genap.js").read())
            else:
                self.driver.execute_script(open("./js/khs_page_ganjil.js").read())


            try:
                last = self.driver.find_element_by_partial_link_text("Kuisioner")
                print(last.text)
        
                self.action.move_to_element(last).click(last).perform()

                # Reload Page
                self.driver.refresh()

                # Masuk Ke Kuisoner
                self._kuisioner()

                # Menutup Window Baru
                self.driver.execute_script("window.close();")

                # Handling Current Tab with webdriver
                self._changeTab()

                # Slepp for debug
                # time.sleep(30)

            except NoSuchElementException as exception:
                print(exception)
                print("Tidak ada lagi kuisioner, menutup browser")
                run = False
                self.driver.quit()
            
    def _changeTab(self):
        allTabs = self.driver.window_handles

        for tab in allTabs:
            self.driver.switch_to.window(tab)
            print(self.driver.current_url)

    
    def _kuisioner(self):

        self._changeTab()
        
        self._kuisionerTab("1", 1, 16) # Kesiapan Mengajar
        self._kuisionerTab("2", 17, 23) 
        self._kuisionerTab("3", 24, 27)
        self._kuisionerTab("4", 28, 32)
        self._kuisionerTab("5", 33, 35)

        # Tab Saran
        link = "a[href='#tabs8']"
        elem = "document.querySelector(\""+link+"\").click();"
        self.driver.execute_script(elem)

        # Mengisi saran dengan text kosong
        elemText = "document.querySelector('textarea').value = ' ';"
        self.driver.execute_script(elemText)

        # Submit Kuisioner
        elemSubmit = "document.querySelector('#submit').click();"
        self.driver.execute_script(elemSubmit)

    def _kuisionerTab(self, tabNum, start, pertanyaan):
        link = "a[href='#tabs"+tabNum+"']"
        elem = "document.querySelector(\""+link+"\").click();"
        self.driver.execute_script(elem)
        self._checkingTheBox(start, pertanyaan + 1)


    def _checkingTheBox(self, start, qLen):
        for i in range(start, qLen):
            name = "jawab["+str(i)+"]"
            value = random.choice(self.array)
            elem = "document.querySelector(\"tr input[name='"+name+"'][value='"+value+"']\").checked = true;"
            self.driver.execute_script(elem)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
