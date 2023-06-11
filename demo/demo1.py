from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

app = QApplication([])
window = QMainWindow()
widget = QWidget()
layout = QVBoxLayout(widget)
table = QTableView()

model = QStandardItemModel()
model.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])  # 设置属性名

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in data:
    row_items = [QStandardItem(str(item)) for item in row]
    model.appendRow(row_items)

table.setModel(model)

# 清空表格数据
model.clear()
# 清空表格属性名（表头）
model.setHorizontalHeaderLabels([])

table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

layout.addWidget(table)
window.setCentralWidget(widget)
window.show()
app.exec_()
