from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout
import sys

from DatePicker import DatePicker

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setFixedSize(640, 480)
    layout = QHBoxLayout()
    window.setLayout(layout)
    datePicker = DatePicker()
    window.layout().addWidget(datePicker)
    window.show()
    sys.exit(app.exec_())
