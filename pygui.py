# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 592)
        self.central = QtWidgets.QWidget(MainWindow)
        self.central.setObjectName("central")
        self.drop_Shadow_layout = QtWidgets.QVBoxLayout(self.central)
        self.drop_Shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_Shadow_layout.setSpacing(0)
        self.drop_Shadow_layout.setObjectName("drop_Shadow_layout")
        self.drop_frame = QtWidgets.QFrame(self.central)
        self.drop_frame.setStyleSheet("background-color: rgb(1, 67, 93);\n"
"border-radius: 10px;")
        self.drop_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_frame.setObjectName("drop_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.drop_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color: none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Romantic")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("TH Baijam")
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(60, 231, 195);")
        self.label_title.setScaledContents(False)
        self.label_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title)
        self.frame_btns = QtWidgets.QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_maximize.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_maximize.setFont(font)
        self.btn_maximize.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 255, 127,150);\n"
"}")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_3.addWidget(self.btn_maximize)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_minimize.setFont(font)
        self.btn_minimize.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 170, 0,150);\n"
"}")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 0, 0,150);\n"
"}")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.title_bar)
        self.content = QtWidgets.QFrame(self.drop_frame)
        self.content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.content.setStyleSheet("background-color: none;")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content)
        self.stackedWidget.setStyleSheet("backgroud-color: none;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_content_home = QtWidgets.QFrame(self.page_home)
        self.frame_content_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_home.setObjectName("frame_content_home")
        self.frame_circle_1 = QtWidgets.QFrame(self.frame_content_home)
        self.frame_circle_1.setGeometry(QtCore.QRect(30, 80, 250, 250))
        self.frame_circle_1.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_circle_1.setStyleSheet("QFrame{\n"
"    border-radius: 125px;\n"
"    border: 5px solid rgb(60,231,195)\n"
"}\n"
"QFrame:hover{\n"
"    border: 5px solid rgb(105,95,148)\n"
"}")
        self.frame_circle_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle_1.setObjectName("frame_circle_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_circle_1)
        self.verticalLayout_6.setContentsMargins(11, 20, -1, 20)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.frame_circle_1)
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
"color: rgb(218, 218, 218);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.humid = QtWidgets.QLabel(self.frame_circle_1)
        self.humid.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(50)
        self.humid.setFont(font)
        self.humid.setStyleSheet("border: none;\n"
"color: rgb(0, 170, 255);")
        self.humid.setAlignment(QtCore.Qt.AlignCenter)
        self.humid.setObjectName("humid")
        self.verticalLayout_6.addWidget(self.humid)
        self.label_3 = QtWidgets.QLabel(self.frame_circle_1)
        self.label_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: none;\n"
"color: rgb(0, 170, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_circle_2 = QtWidgets.QFrame(self.frame_content_home)
        self.frame_circle_2.setGeometry(QtCore.QRect(290, 80, 250, 250))
        self.frame_circle_2.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_circle_2.setStyleSheet("QFrame{\n"
"    border-radius: 125px;\n"
"    border: 5px solid rgb(60,231,195)\n"
"}\n"
"QFrame:hover{\n"
"    border: 5px solid rgb(105,95,148)\n"
"}")
        self.frame_circle_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle_2.setObjectName("frame_circle_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_circle_2)
        self.verticalLayout_7.setContentsMargins(11, 20, -1, 20)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_circle_2)
        self.label_5.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: none;\n"
"color: rgb(218, 218, 218);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.frame_circle_2)
        self.label_6.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: none;\n"
"color: rgb(0, 255, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.label_12 = QtWidgets.QLabel(self.frame_circle_2)
        self.label_12.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border: none;\n"
"color: rgb(0, 255, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.frame_circle_3 = QtWidgets.QFrame(self.frame_content_home)
        self.frame_circle_3.setGeometry(QtCore.QRect(550, 80, 250, 250))
        self.frame_circle_3.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_circle_3.setStyleSheet("QFrame{\n"
"    border-radius: 125px;\n"
"    border: 5px solid rgb(60,231,195)\n"
"}\n"
"QFrame:hover{\n"
"    border: 5px solid rgb(105,95,148)\n"
"}")
        self.frame_circle_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle_3.setObjectName("frame_circle_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_circle_3)
        self.verticalLayout_8.setContentsMargins(11, 20, -1, 20)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_circle_3)
        self.label_9.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: none;\n"
"color: rgb(218, 218, 218);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.TempDS = QtWidgets.QLabel(self.frame_circle_3)
        self.TempDS.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtCn BT")
        font.setPointSize(50)
        self.TempDS.setFont(font)
        self.TempDS.setStyleSheet("border: none;\n"
"color: rgb(255, 170, 255);")
        self.TempDS.setAlignment(QtCore.Qt.AlignCenter)
        self.TempDS.setObjectName("TempDS")
        self.verticalLayout_8.addWidget(self.TempDS)
        self.label_11 = QtWidgets.QLabel(self.frame_circle_3)
        self.label_11.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border: none;\n"
"color: rgb(255, 170, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.onsw = QtWidgets.QPushButton(self.frame_content_home)
        self.onsw.setGeometry(QtCore.QRect(210, 400, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.onsw.setFont(font)
        self.onsw.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 246, 246);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 246, 246,150);\n"
"}")
        self.onsw.setObjectName("onsw")
        self.label_18 = QtWidgets.QLabel(self.frame_content_home)
        self.label_18.setGeometry(QtCore.QRect(210, 10, 391, 51))
        self.label_18.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:3px solid rgba(0,0,0,20);\n"
"color: rgb(218, 218, 218);\n"
"padding-bottom:7px")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_content_home)
        self.label_19.setGeometry(QtCore.QRect(30, 10, 141, 51))
        self.label_19.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:3px solid rgba(0,0,0,20);\n"
"color: rgb(218, 218, 218);\n"
"padding-bottom:7px")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_content_home)
        self.label_20.setGeometry(QtCore.QRect(640, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:3px solid rgba(0,0,0,20);\n"
"color: rgb(218, 218, 218);\n"
"padding-bottom:7px")
        self.label_20.setObjectName("label_20")
        self.offsw = QtWidgets.QPushButton(self.frame_content_home)
        self.offsw.setGeometry(QtCore.QRect(400, 400, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.offsw.setFont(font)
        self.offsw.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(0, 246, 246);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 246, 246,150);\n"
"}")
        self.offsw.setObjectName("offsw")
        self.label_21 = QtWidgets.QLabel(self.frame_content_home)
        self.label_21.setGeometry(QtCore.QRect(210, 340, 391, 51))
        self.label_21.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:3px solid rgba(0,0,0,20);\n"
"color: rgb(218, 218, 218);\n"
"padding-bottom:7px")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.frame_content_home)
        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QtWidgets.QWidget()
        self.page_credits.setObjectName("page_credits")
        self.frame_content_credits = QtWidgets.QFrame(self.page_credits)
        self.frame_content_credits.setGeometry(QtCore.QRect(700, 360, 120, 80))
        self.frame_content_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_credits.setObjectName("frame_content_credits")
        self.stackedWidget.addWidget(self.page_credits)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.content)
        self.credit = QtWidgets.QFrame(self.drop_frame)
        self.credit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.credit.setStyleSheet("background-color: none;")
        self.credit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credit.setObjectName("credit")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.credit)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fram_grip = QtWidgets.QFrame(self.credit)
        self.fram_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fram_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fram_grip.setObjectName("fram_grip")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fram_grip)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_credits = QtWidgets.QLabel(self.fram_grip)
        font = QtGui.QFont()
        font.setFamily("Romantic")
        font.setPointSize(8)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(200, 120, 183);")
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_3.addWidget(self.label_credits)
        self.horizontalLayout_2.addWidget(self.fram_grip)
        self.frame_label_credits = QtWidgets.QFrame(self.credit)
        self.frame_label_credits.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_label_credits.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_label_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_credits.setObjectName("frame_label_credits")
        self.horizontalLayout_2.addWidget(self.frame_label_credits)
        self.verticalLayout.addWidget(self.credit)
        self.drop_Shadow_layout.addWidget(self.drop_frame)
        MainWindow.setCentralWidget(self.central)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p>Electronic Enginnering</p></body></html>"))
        self.btn_maximize.setText(_translate("MainWindow", "💓"))
        self.btn_minimize.setText(_translate("MainWindow", "🩸"))
        self.btn_close.setText(_translate("MainWindow", "🌡"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Humidity</p><p>( DHT22 )</p></body></html>"))
        self.humid.setText(_translate("MainWindow", "97"))
        self.label_3.setText(_translate("MainWindow", "%"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Temperature</p><p>( DHT 22 )</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "93"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" vertical-align:super;\">o</span>C</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Temperature</p><p>( DS18B20 )</p></body></html>"))
        self.TempDS.setText(_translate("MainWindow", "37.5"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" vertical-align:super;\">o</span>C</p></body></html>"))
        self.onsw.setText(_translate("MainWindow", "ON"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">นาย กิตตินันท์ อ้นสันเทียะ</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">B61314xx</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">24/10/64</span></p></body></html>"))
        self.offsw.setText(_translate("MainWindow", "OFF"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">ON-OFF LED</span></p></body></html>"))
        self.label_credits.setText(_translate("MainWindow", "By: Kittinan O."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
