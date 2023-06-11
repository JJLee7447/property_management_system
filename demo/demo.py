from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

class MyTableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self.data = data
        self.headers = headers

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self.data[row][col])

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return str(self.headers[section])

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
headers = ['A', 'B', 'C']

app = QApplication([])
window = QMainWindow()
table = QTableView()
model = MyTableModel(data, headers)
table.setModel(model)
window.setCentralWidget(table)
window.show()
app.exec_()
