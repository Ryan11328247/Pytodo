from PyQt6.QtWidgets import (
    QApplication, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QWidget, QMessageBox, QListWidget
)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("任務清單")
        self.resize(500, 400)
        
        # 元件
        self.title = QLabel("請輸入任務名稱：", self)
        self.input_title = QLineEdit(self)
        self.description = QLabel("請輸入任務描述 (可選)：", self)
        self.input_description = QLineEdit(self)
        self.due_date = QLabel("請輸入完成期限 (格式: YYYY-MM-DD)：", self)
        self.input_due_date = QLineEdit(self)
        self.add_button = QPushButton("新增任務", self)
        self.complete_button = QPushButton("完成任務", self)
        self.delete_button = QPushButton("刪除任務", self)
        self.task_list = QListWidget(self)

        # 佈局
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.input_title)
        layout.addWidget(self.description)
        layout.addWidget(self.input_description)
        layout.addWidget(self.due_date)
        layout.addWidget(self.input_due_date)
        layout.addWidget(self.add_button)
        layout.addWidget(self.complete_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.task_list)
        self.setLayout(layout)

        # 事件連接
        self.add_button.clicked.connect(self.add_task)
        self.complete_button.clicked.connect(self.complete_task)
        self.delete_button.clicked.connect(self.delete_task)

        # 任務列表
        self.tasks = []

    def add_task(self):
        title = self.input_title.text().strip()
        description = self.input_description.text().strip()
        due_date = self.input_due_date.text().strip()
        if title:
            task_info = f"{title} 〔{description}, {due_date}〕"
            self.tasks.append(task_info)
            self.task_list.addItem(task_info)
            self.input_title.clear()
            self.input_description.clear()
            self.input_due_date.clear()
        else:
            QMessageBox.warning(self, "警告", "請輸入任務名稱!")

    def complete_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            task_info = self.tasks[selected]
            task, info = task_info.split(" 〔")
            info = info[:-1]
            self.tasks[selected] = f"[已完成] {task} 〔{info}〕"
            self.task_list.item(selected).setText(self.tasks[selected])
            QMessageBox.information(self, "任務完成", f"已完成任務: {task}")

    def delete_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            task_info = self.tasks[selected]
            task, info = task_info.split(" 〔")
            self.tasks.pop(selected)
            self.task_list.takeItem(selected)
            QMessageBox.information(self, "任務刪除", f"已刪除任務: {task}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())