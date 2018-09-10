from PySide2.QtGui import QIcon
from PySide2.QtCore import \
    Qt, \
    Slot, \
    SLOT, \
    QSize, \
    QPoint, \
    Signal
from PySide2.QtWidgets import \
    QWidget, \
    QDialog, \
    QPushButton, \
    QHBoxLayout, \
    QCalendarWidget


class DatePicker(QWidget):

    selectionChanged = Signal()

    def __init__(self, parent=None):
        super(DatePicker, self).__init__(parent)
        self.button = QPushButton(self)
        icon = QIcon("logo.svg")
        self.button.setIcon(icon)
        self.setFixedSize(32, 32)
        self.button.setFixedSize(32, 32)
        self.button.setIconSize(QSize(22, 22))

        self.__margin__ = 5

        self.dialog = QDialog()
        self.dialog.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.Popup)
        self.dialog.setFixedSize(480, 240)
        self.dialog.setLayout(QHBoxLayout())
        self.calender = QCalendarWidget(self)
        self.dialog.layout().addWidget(self.calender)
        self.dialog.layout().setContentsMargins(0, 0, 0, 0)
        self.dialog.layout().setSpacing(0)

        self.button.clicked.connect(self.showCalender)
        self.calender.selectionChanged.connect(self.__onSelectionChanged__)

    def show(self):
        self.showCalender()

    def close(self):
        self.dialog.close()

    @Slot()
    def showCalender(self):
        print('in show')
        p = self.mapToGlobal(QPoint(0, self.height() + self.__margin__))
        self.dialog.setGeometry(p.x(), p.y(), 0, 0)
        self.dialog.show()

    def setIcon(self, icon):
        if type(icon) is QIcon:
            self.button.setIcon(icon)
        elif type(icon) is str:
            self.button.setIcon(QIcon(icon))
        else:
            raise Exception('Wrong argument type, icon should be either PySide2.QtGui.QIcon or str "string"')

    def icon(self):
        return self.button.icon()

    def setIconSize(self, iconSize):
        self.button.setIconSize(iconSize)
        # if type(iconSize) is QSize:
        #     self.button.setIconSize(iconSize)
        # elif type(iconSize) is int:
        #     self.button.setIcon(QSize(iconSize, iconSize))
        # elif type(type) is iter:
        #     import collections
        #     if isinstance(iconSize, collections.Iterable):
        #         if len(iconSize) == 1:
        #             self.setIconSize(iconSize[0])
        #         elif len(iconSize) == 2:
        #             self.setIconSize(QSize(iconSize[0], iconSize[1]))
        #         else:
        #             raise Exception()
        # else:
        #     raise Exception("Wrong argument type, iconSize should be either PySide2.QtCore.QSize or int value or width and height "
        #                     "or iterable contains one QSize, one int or two int values for width and height respectively")

    def iconSize(self):
        return self.button.iconSize()

    def setFirstDayOfWeek(self, firstDayOfWeek):
        self.calender.setFirstDayOfWeek(firstDayOfWeek)
        # if type(firstDayOfWeek) is Qt.DayOfWeek:
        #     self.calender.setFirstDayOfWeek(firstDayOfWeek)
        # elif type(firstDayOfWeek) is int:
        #     if firstDayOfWeek < 1 or firstDayOfWeek > 7:
        #         raise Exception("Wrong argument, firstDayOfWeek should be from 1 to 7 (Monday --> Sunday)")
        #     self.calender.setFirstDayOfWeek(Qt.DayOfWeek(firstDayOfWeek))
        # else:
        #     raise Exception("Wrong type, firstDayOfWeek should be either PySide2.QtCore.Qt.DayOf or int (1 --> 7) (Monday --> Sunday)")

    def firstDayOfWeek(self):
        self.calender.firstDayOfWeek()

    def selectedDate(self):
        self.calender.selectedDate()

    def setSelectedDate(self, args, kwargs):
        self.calender.setSelectedDate(args, kwargs)

    def minimumDate(self):
        self.calender.minimumDate()

    def setMinimumDate(self):
        self.calender.setMinimumDate()

    def __onSelectionChanged__(self):
        self.selectionChanged.emit()