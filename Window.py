# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 210, 351, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.start_auto_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.start_auto_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_auto_btn.setFont(font)
        self.start_auto_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_auto_btn.setStyleSheet("padding: 5px;")
        self.start_auto_btn.setObjectName("start_auto_btn")
        self.gridLayout_2.addWidget(self.start_auto_btn, 0, 0, 1, 1)
        self.next_step_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.next_step_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.next_step_btn.setFont(font)
        self.next_step_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_step_btn.setStyleSheet("padding:5px;")
        self.next_step_btn.setObjectName("next_step_btn")
        self.gridLayout_2.addWidget(self.next_step_btn, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 320, 451, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(510, 320, 501, 311))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 170, 351, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.apply_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.apply_btn.setFont(font)
        self.apply_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apply_btn.setStyleSheet("padding: 5px;")
        self.apply_btn.setObjectName("apply_btn")
        self.horizontalLayout.addWidget(self.apply_btn)
        self.clear_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clear_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clear_btn.setFont(font)
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_btn.setStyleSheet("padding: 5px;")
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.reset_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reset_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reset_btn.setFont(font)
        self.reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_btn.setStyleSheet("padding:5px;")
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout.addWidget(self.reset_btn)
        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setGeometry(QtCore.QRect(20, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.log_label.setFont(font)
        self.log_label.setStyleSheet("")
        self.log_label.setObjectName("log_label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(560, 640, 446, 33))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.max_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_check.setFont(font)
        self.max_check.setChecked(True)
        self.max_check.setObjectName("max_check")
        self.horizontalLayout_2.addWidget(self.max_check)
        self.avg_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avg_check.setFont(font)
        self.avg_check.setChecked(True)
        self.avg_check.setObjectName("avg_check")
        self.horizontalLayout_2.addWidget(self.avg_check)
        self.min_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_check.setFont(font)
        self.min_check.setChecked(True)
        self.min_check.setObjectName("min_check")
        self.horizontalLayout_2.addWidget(self.min_check)
        self.show_more_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.show_more_btn.setFont(font)
        self.show_more_btn.setObjectName("show_more_btn")
        self.horizontalLayout_2.addWidget(self.show_more_btn)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(680, 20, 331, 291))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 351, 149))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.population_label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.population_label_3.setFont(font)
        self.population_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.population_label_3.setObjectName("population_label_3")
        self.gridLayout.addWidget(self.population_label_3, 2, 0, 1, 1)
        self.population_label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.population_label_2.setFont(font)
        self.population_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.population_label_2.setObjectName("population_label_2")
        self.gridLayout.addWidget(self.population_label_2, 1, 0, 1, 1)
        self.pop_size = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pop_size.setFont(font)
        self.pop_size.setAccelerated(True)
        self.pop_size.setMaximum(1000)
        self.pop_size.setProperty("value", 50)
        self.pop_size.setObjectName("pop_size")
        self.gridLayout.addWidget(self.pop_size, 0, 1, 1, 1)
        self.cross_prob = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cross_prob.setFont(font)
        self.cross_prob.setAccelerated(True)
        self.cross_prob.setMaximum(1.0)
        self.cross_prob.setSingleStep(0.01)
        self.cross_prob.setProperty("value", 1.0)
        self.cross_prob.setObjectName("cross_prob")
        self.gridLayout.addWidget(self.cross_prob, 1, 1, 1, 1)
        self.mutate_prob = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mutate_prob.setFont(font)
        self.mutate_prob.setAccelerated(True)
        self.mutate_prob.setDecimals(3)
        self.mutate_prob.setMaximum(1.0)
        self.mutate_prob.setSingleStep(0.0001)
        self.mutate_prob.setProperty("value", 0.001)
        self.mutate_prob.setObjectName("mutate_prob")
        self.gridLayout.addWidget(self.mutate_prob, 2, 1, 1, 1)
        self.population_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.population_label.setFont(font)
        self.population_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.population_label.setObjectName("population_label")
        self.gridLayout.addWidget(self.population_label, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(470, 70, 92, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.current_max = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_max.setFont(font)
        self.current_max.setStyleSheet("color: green;")
        self.current_max.setFrameShape(QtWidgets.QFrame.Box)
        self.current_max.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.current_max.setText("")
        self.current_max.setTextFormat(QtCore.Qt.AutoText)
        self.current_max.setAlignment(QtCore.Qt.AlignCenter)
        self.current_max.setObjectName("current_max")
        self.verticalLayout.addWidget(self.current_max)
        self.current_min = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_min.setFont(font)
        self.current_min.setStyleSheet("color: red;")
        self.current_min.setFrameShape(QtWidgets.QFrame.Box)
        self.current_min.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.current_min.setText("")
        self.current_min.setTextFormat(QtCore.Qt.AutoText)
        self.current_min.setAlignment(QtCore.Qt.AlignCenter)
        self.current_min.setObjectName("current_min")
        self.verticalLayout.addWidget(self.current_min)
        self.current_avg = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_avg.setFont(font)
        self.current_avg.setStyleSheet("color: blue;")
        self.current_avg.setFrameShape(QtWidgets.QFrame.Box)
        self.current_avg.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.current_avg.setLineWidth(1)
        self.current_avg.setText("")
        self.current_avg.setTextFormat(QtCore.Qt.AutoText)
        self.current_avg.setAlignment(QtCore.Qt.AlignCenter)
        self.current_avg.setObjectName("current_avg")
        self.verticalLayout.addWidget(self.current_avg)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(380, 70, 92, 151))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.current_max_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_max_2.setFont(font)
        self.current_max_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.current_max_2.setObjectName("current_max_2")
        self.verticalLayout_3.addWidget(self.current_max_2)
        self.current_min_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_min_2.setFont(font)
        self.current_min_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.current_min_2.setObjectName("current_min_2")
        self.verticalLayout_3.addWidget(self.current_min_2)
        self.current_avg_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_avg_2.setFont(font)
        self.current_avg_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.current_avg_2.setObjectName("current_avg_2")
        self.verticalLayout_3.addWidget(self.current_avg_2)
        self.current_max_for_2 = QtWidgets.QLabel(self.centralwidget)
        self.current_max_for_2.setGeometry(QtCore.QRect(570, 70, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.current_max_for_2.setFont(font)
        self.current_max_for_2.setObjectName("current_max_for_2")
        self.current_min_for_2 = QtWidgets.QLabel(self.centralwidget)
        self.current_min_for_2.setGeometry(QtCore.QRect(570, 120, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.current_min_for_2.setFont(font)
        self.current_min_for_2.setObjectName("current_min_for_2")
        self.current_max_for = QtWidgets.QLabel(self.centralwidget)
        self.current_max_for.setGeometry(QtCore.QRect(600, 70, 71, 46))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_max_for.setFont(font)
        self.current_max_for.setStyleSheet("color: orange;")
        self.current_max_for.setFrameShape(QtWidgets.QFrame.Box)
        self.current_max_for.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.current_max_for.setText("")
        self.current_max_for.setTextFormat(QtCore.Qt.AutoText)
        self.current_max_for.setAlignment(QtCore.Qt.AlignCenter)
        self.current_max_for.setObjectName("current_max_for")
        self.current_min_for = QtWidgets.QLabel(self.centralwidget)
        self.current_min_for.setGeometry(QtCore.QRect(600, 120, 71, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_min_for.setFont(font)
        self.current_min_for.setStyleSheet("color: orange;")
        self.current_min_for.setFrameShape(QtWidgets.QFrame.Box)
        self.current_min_for.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.current_min_for.setText("")
        self.current_min_for.setTextFormat(QtCore.Qt.AutoText)
        self.current_min_for.setAlignment(QtCore.Qt.AlignCenter)
        self.current_min_for.setObjectName("current_min_for")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_auto_btn.setText(_translate("MainWindow", "Start Auto"))
        self.next_step_btn.setText(_translate("MainWindow", "Next step"))
        self.apply_btn.setText(_translate("MainWindow", "Apply"))
        self.clear_btn.setText(_translate("MainWindow", "Stop"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.log_label.setText(_translate("MainWindow", "Iteration no. 0"))
        self.max_check.setText(_translate("MainWindow", "Maximum"))
        self.avg_check.setText(_translate("MainWindow", "Average"))
        self.min_check.setText(_translate("MainWindow", "Minimum"))
        self.show_more_btn.setText(_translate("MainWindow", "Show more history"))
        self.population_label_3.setText(_translate("MainWindow", "Mutation probability:"))
        self.population_label_2.setText(_translate("MainWindow", "Crossing probability:"))
        self.population_label.setText(_translate("MainWindow", "Population size:"))
        self.label.setText(_translate("MainWindow", "Current population:"))
        self.current_max_2.setText(_translate("MainWindow", "Maximum:"))
        self.current_min_2.setText(_translate("MainWindow", "Minimum: "))
        self.current_avg_2.setText(_translate("MainWindow", "Average:  "))
        self.current_max_for_2.setText(_translate("MainWindow", "x = "))
        self.current_min_for_2.setText(_translate("MainWindow", "x = "))

