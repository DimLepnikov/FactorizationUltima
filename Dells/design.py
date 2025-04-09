# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QSize(500, 700))
        icon = QIcon()
        icon.addFile(u":/icons/calculate_24dp_000000_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_2.addWidget(self.radioButton, 4, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_2.addWidget(self.radioButton_2, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QSize(0, 35))
        self.btn_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QSize(0, 35))
        self.btn_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setMinimumSize(QSize(0, 35))
        self.btn_0.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_0.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_0, 5, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMinimumSize(QSize(0, 35))
        self.btn_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QSize(0, 35))
        self.btn_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QSize(0, 35))
        self.btn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QSize(0, 35))
        self.btn_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_C = QPushButton(self.centralwidget)
        self.btn_C.setObjectName(u"btn_C")
        sizePolicy.setHeightForWidth(self.btn_C.sizePolicy().hasHeightForWidth())
        self.btn_C.setSizePolicy(sizePolicy)
        self.btn_C.setMinimumSize(QSize(0, 35))
        self.btn_C.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_C.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_C, 5, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QSize(0, 35))
        self.btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_ans = QPushButton(self.centralwidget)
        self.btn_ans.setObjectName(u"btn_ans")
        sizePolicy.setHeightForWidth(self.btn_ans.sizePolicy().hasHeightForWidth())
        self.btn_ans.setSizePolicy(sizePolicy)
        self.btn_ans.setMinimumSize(QSize(0, 35))
        self.btn_ans.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ans.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_ans, 5, 2, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QSize(0, 35))
        self.btn_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QSize(0, 35))
        self.btn_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.btn_6, 2, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 12, 0, 1, 2)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_2.addWidget(self.radioButton_3, 3, 0, 1, 1)

        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy1)
        self.lbl_temp.setStyleSheet(u"font-size: 25pt;")
        self.lbl_temp.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lbl_temp, 5, 0, 1, 1)

        self.le_entry_dells = QTextEdit(self.centralwidget)
        self.le_entry_dells.setObjectName(u"le_entry_dells")
        self.le_entry_dells.setStyleSheet(u"font-size: 16px; border: 1px solid #ccc; border-radius: 4px;")
        self.le_entry_dells.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_entry_dells, 8, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dells", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e-\u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u041f\u043e\u043b\u043b\u0430\u0440\u0434\u0430", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u0440\u043e\u0431\u043d\u043e\u0433\u043e \u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.btn_C.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_ans.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_ans.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0424\u0435\u0440\u043c\u0430", None))
        self.lbl_temp.setText("")
    # retranslateUi

