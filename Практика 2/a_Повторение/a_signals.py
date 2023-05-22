"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""
import time

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initSignals()

    def initUI(self) -> None:
        """

        :return:
        """

        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()
        self.lineEditMirror.setReadOnly(True)

        self.pushButtonMirror = QtWidgets.QPushButton('Отзеркалить')

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEditInput)
        layoutLineEdit.addWidget(self.lineEditMirror)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addWidget(self.pushButtonMirror)

        self.setLayout(layoutMain)



    def initSignals(self) -> None:
        """

        :return:
        """

        # self.pushButtonMirror.clicked.connect(self.mirrorText)
        # self.lineEditInput.textChanged.connect(self.mirrorText)
        self.pushButtonMirror.clicked.connect(lambda signal_data: print(time.ctime(), self.pushButtonMirror, signal_data))
        self.lineEditInput.textChanged.connect(lambda signal_data: print(time.ctime(), self.lineEditInput, signal_data))
        self.lineEditMirror.textChanged.connect(lambda signal_data: print(time.ctime(), self.lineEditMirror, signal_data))




    def mirrorText(self) -> None:
        """

        :return:
        """

        sours_text = self.lineEditInput.text()
        self.lineEditMirror.setText(sours_text[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
