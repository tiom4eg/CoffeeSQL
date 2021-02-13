from PyQt5 import QtWidgets, QtCore
import sys
import sqlite3


class UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 300)
        self.searchLabel = QtWidgets.QLabel(Form)
        self.searchLabel.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.searchLabel.setObjectName("searchLabel")
        self.searchValue = QtWidgets.QLineEdit(Form)
        self.searchValue.setGeometry(QtCore.QRect(120, 10, 201, 20))
        self.searchValue.setObjectName("searchValue")
        self.searchParameter = QtWidgets.QComboBox(Form)
        self.searchParameter.setGeometry(QtCore.QRect(330, 10, 131, 22))
        self.searchParameter.setObjectName("searchParameter")
        self.searchParameter.addItem("")
        self.searchParameter.addItem("")
        self.searchParameter.addItem("")
        self.searchParameter.addItem("")
        self.searchParameter.addItem("")
        self.searchParameter.addItem("")
        self.resultLabel = QtWidgets.QLabel(Form)
        self.resultLabel.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.resultLabel.setObjectName("resultLabel")
        self.resultText = QtWidgets.QTextBrowser(Form)
        self.resultText.setGeometry(QtCore.QRect(10, 100, 451, 192))
        self.resultText.setObjectName("resultText")
        self.searchTrigger = QtWidgets.QPushButton(Form)
        self.searchTrigger.setGeometry(QtCore.QRect(120, 40, 201, 23))
        self.searchTrigger.setObjectName("searchTrigger")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Кофе"))
        self.searchLabel.setText(_translate("Form", "Поиск по параметру:"))
        self.searchParameter.setItemText(0, _translate("Form", "ID"))
        self.searchParameter.setItemText(1, _translate("Form", "Grade"))
        self.searchParameter.setItemText(2, _translate("Form", "DegreeOfRoasting"))
        self.searchParameter.setItemText(3, _translate("Form", "IsGrinded"))
        self.searchParameter.setItemText(4, _translate("Form", "Price"))
        self.searchParameter.setItemText(5, _translate("Form", "PackageVolume"))
        self.resultLabel.setText(_translate("Form", "Результат поиска:"))
        self.searchTrigger.setText(_translate("Form", "Искать"))


class Application(QtWidgets.QWidget, UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.searchTrigger.clicked.connect(self.search)

    def search(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        data = []
        try:
            if self.searchParameter.currentText() in ('ID', 'Price', 'PackageVolume', 'IsGrinded'):
                data = list(cur.execute(
                f"""SELECT * FROM Coffee WHERE {self.searchParameter.currentText()}={self.searchValue.text()}"""))
            else:
                data = list(cur.execute(
                f"""SELECT * FROM Coffee WHERE {self.searchParameter.currentText()}='{self.searchValue.text()}'"""))
        except sqlite3.OperationalError:
            pass
        if data:
            text = f"Найдено {len(data)} результатов:\n"
            for i in range(len(data)):
                text += "--------------------\n"
                text += f"ID: {data[i][0]}\n"
                text += f"Сорт: {data[i][1].lower()}\n"
                text += f"Степень обжарки: {data[i][2].lower()}\n"
                text += f"Текстура: {'молотый' if data[i][3] else 'цельный'}\n"
                text += f"Описание вкуса: {data[i][4].lower()}\n"
                text += f"Цена: {data[i][5]} рублей за упаковку\n"
                text += f"Объем упаковки: {data[i][6]} грамм\n"
            self.resultText.setText(text)
        else:
            self.resultText.setText("Не найдено результатов, удовлетворяющих запросу.")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

