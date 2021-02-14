from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import sqlite3


class AddDialogUI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 251, 341, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.inputLabel = QtWidgets.QLabel(Dialog)
        self.inputLabel.setGeometry(QtCore.QRect(120, 10, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputLabel.setFont(font)
        self.inputLabel.setObjectName("inputLabel")
        self.gradeLabel = QtWidgets.QLabel(Dialog)
        self.gradeLabel.setGeometry(QtCore.QRect(10, 50, 51, 20))
        self.gradeLabel.setObjectName("gradeLabel")
        self.degreeLabel = QtWidgets.QLabel(Dialog)
        self.degreeLabel.setGeometry(QtCore.QRect(10, 80, 111, 21))
        self.degreeLabel.setObjectName("degreeLabel")
        self.isGrindedLabel = QtWidgets.QLabel(Dialog)
        self.isGrindedLabel.setGeometry(QtCore.QRect(10, 105, 61, 31))
        self.isGrindedLabel.setObjectName("isGrindedLabel")
        self.tasteLabel = QtWidgets.QLabel(Dialog)
        self.tasteLabel.setGeometry(QtCore.QRect(10, 140, 91, 31))
        self.tasteLabel.setObjectName("tasteLabel")
        self.priceLabel = QtWidgets.QLabel(Dialog)
        self.priceLabel.setGeometry(QtCore.QRect(10, 170, 51, 41))
        self.priceLabel.setObjectName("priceLabel")
        self.volumeLabel = QtWidgets.QLabel(Dialog)
        self.volumeLabel.setGeometry(QtCore.QRect(10, 210, 101, 21))
        self.volumeLabel.setObjectName("volumeLabel")
        self.gradeValue = QtWidgets.QLineEdit(Dialog)
        self.gradeValue.setGeometry(QtCore.QRect(50, 50, 113, 20))
        self.gradeValue.setObjectName("gradeValue")
        self.degreeValue = QtWidgets.QLineEdit(Dialog)
        self.degreeValue.setGeometry(QtCore.QRect(110, 80, 113, 21))
        self.degreeValue.setObjectName("degreeValue")
        self.isGrindedValue = QtWidgets.QSpinBox(Dialog)
        self.isGrindedValue.setGeometry(QtCore.QRect(70, 110, 42, 22))
        self.isGrindedValue.setObjectName("isGrindedValue")
        self.isGrindedValue.setMinimum(0)
        self.isGrindedValue.setMaximum(1)
        self.tasteValue = QtWidgets.QLineEdit(Dialog)
        self.tasteValue.setGeometry(QtCore.QRect(100, 145, 271, 21))
        self.tasteValue.setObjectName("tasteValue")
        self.priceValue = QtWidgets.QSpinBox(Dialog)
        self.priceValue.setGeometry(QtCore.QRect(50, 181, 60, 21))
        self.priceValue.setObjectName("priceValue")
        self.priceValue.setMinimum(49)
        self.priceValue.setMaximum(99999)
        self.priceValue.setSingleStep(50)
        self.priceValue.setValue(499)
        self.volumeValue = QtWidgets.QSpinBox(Dialog)
        self.volumeValue.setGeometry(QtCore.QRect(110, 210, 80, 21))
        self.volumeValue.setObjectName("volumeValue")
        self.volumeValue.setMinimum(50)
        self.volumeValue.setMaximum(50000)
        self.volumeValue.setSingleStep(50)
        self.volumeValue.setValue(750)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Coffee"))
        self.inputLabel.setText(_translate("Dialog", "Введите данные:"))
        self.gradeLabel.setText(_translate("Dialog", "Сорт:"))
        self.degreeLabel.setText(_translate("Dialog", "Степень обжарки:"))
        self.isGrindedLabel.setText(_translate("Dialog", "Молотый?:"))
        self.tasteLabel.setText(_translate("Dialog", "Описание вкуса:"))
        self.priceLabel.setText(_translate("Dialog", "Цена:"))
        self.volumeLabel.setText(_translate("Dialog", "Объем упаковки:"))


class AddDialog(QtWidgets.QDialog, AddDialogUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def getValues(self):
        if self.exec_() == QtWidgets.QDialog.Accepted:
            newGrade = self.gradeValue.text()
            newDegree = self.degreeValue.text()
            newIsGrinded = self.isGrindedValue.value()
            newTaste = self.tasteValue.text()
            newPrice = self.priceValue.value()
            newVolume = self.volumeValue.value()
            return (newGrade, newDegree, newIsGrinded, newTaste, newPrice, newVolume)
        else:
            return None


class ApplicationUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 492)
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
        self.resultLabel.setGeometry(QtCore.QRect(10, 80, 111, 21))
        self.resultLabel.setObjectName("resultLabel")
        self.searchTrigger = QtWidgets.QPushButton(Form)
        self.searchTrigger.setGeometry(QtCore.QRect(120, 40, 201, 23))
        self.searchTrigger.setObjectName("searchTrigger")
        self.resultTable = QtWidgets.QTableWidget(Form)
        self.resultTable.setGeometry(QtCore.QRect(10, 100, 681, 291))
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(7)
        self.resultTable.setHorizontalHeaderLabels(
            ["ID", "Сорт", "Степень обжарки", "Молотый?", "Описание вкуса", "Цена", "Объем упаковки"])
        self.resultTable.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.resultInfo = QtWidgets.QLabel(Form)
        self.resultInfo.setGeometry(QtCore.QRect(16, 399, 271, 31))
        self.resultInfo.setText("")
        self.resultInfo.setObjectName("resultInfo")
        self.createNewTrigger = QtWidgets.QPushButton(Form)
        self.createNewTrigger.setGeometry(QtCore.QRect(240, 440, 231, 41))
        self.createNewTrigger.setObjectName("createNewTrigger")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Better Coffee"))
        self.searchLabel.setText(_translate("Form", "Поиск по параметру:"))
        self.searchParameter.setItemText(0, _translate("Form", "ID"))
        self.searchParameter.setItemText(1, _translate("Form", "Сорт"))
        self.searchParameter.setItemText(2, _translate("Form", "Степень обжарки"))
        self.searchParameter.setItemText(3, _translate("Form", "Молотый?"))
        self.searchParameter.setItemText(4, _translate("Form", "Цена"))
        self.searchParameter.setItemText(5, _translate("Form", "Объем упаковки"))
        self.resultLabel.setText(_translate("Form", "Результат поиска:"))
        self.searchTrigger.setText(_translate("Form", "Искать"))
        self.createNewTrigger.setText(_translate("Form", "Добавить элемент"))


class Application(QtWidgets.QWidget, ApplicationUI):
    def __init__(self):
        super().__init__()
        self.currentData = []
        self.setupUi(self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.searchTrigger.clicked.connect(self.search)
        self.createNewTrigger.clicked.connect(self.createNew)
        self.resultTable.itemChanged.connect(self.changeItem)

    def search(self):
        data = []
        try:
            if self.searchParameter.currentText() in ('ID', 'Price', 'PackageVolume', 'IsGrinded'):
                data = list(map(list, self.cur.execute(
                    f"""SELECT * FROM Coffee WHERE {["ID", "Grade", "DegreeOfRoasting", "IsGrinded", "Price", "PackageVolume"][self.searchParameter.currentIndex()]}={self.searchValue.text()}""")))
            else:
                data = list(map(list, self.cur.execute(
                    f"""SELECT * FROM Coffee WHERE {["ID", "Grade", "DegreeOfRoasting", "IsGrinded", "Price", "PackageVolume"][self.searchParameter.currentIndex()]}='{self.searchValue.text()}'""")))
        except sqlite3.OperationalError:
            pass
        if data:
            self.resultInfo.setText(f"Найдено {len(data)} подходящих вариантов.")
            self.resultTable.setColumnCount(7)
            self.resultTable.setRowCount(len(data))
            for i in range(len(data)):
                for j in range(7):
                    self.resultTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))
                    if j == 0:
                        item = self.resultTable.item(i, j)
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        else:
            self.resultInfo.setText("Не найдено подходящих вариантов.")
        self.currentData = data

    def createNew(self):
        newDialog = AddDialog()
        newValues = newDialog.getValues()
        if newValues:
            self.cur.execute("""INSERT INTO Coffee(Grade, DegreeOfRoasting, IsGrinded, TasteDescription, Price, PackageVolume) VALUES(?, ?, ?, ?, ?, ?);""", newValues)
            self.con.commit()

    def changeItem(self):
        for i in range(len(self.currentData)):
            for j in range(7):
                if self.resultTable.item(i, j).text() != str(self.currentData[i][j]):
                    if j in (1, 2, 4):
                        self.cur.execute(f"""UPDATE Coffee SET {["ID", "Grade", "DegreeOfRoasting", "IsGrinded", "TasteDescription", "Price", "PackageVolume"][j]}='{self.resultTable.item(i, j).text()}' WHERE ID={self.resultTable.item(i, 0).text()}""")
                    else:
                        self.cur.execute(
                            f"""UPDATE Coffee SET {["ID", "Grade", "DegreeOfRoasting", "IsGrinded", "TasteDescription", "Price", "PackageVolume"][j]}={self.resultTable.item(i, j).text()} WHERE ID={self.resultTable.item(i, 0).text()}""")
                    self.currentData[i][j] = self.resultTable.item(i, j).text()
                    self.con.commit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
