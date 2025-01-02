from PyQt6.QtWidgets import (
    QApplication, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QWidget, QMessageBox
)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 輸入與互動")
        self.resize(500, 400)
        
        #元件
        self.title = QLabel("請輸入任務名稱：", self)
        self.input_title = QLineEdit(self)
        self.description = QLabel("請輸入任務描述（可選）：", self)
        self.input_description = QLineEdit(self)
        self.due_date = QLabel("請輸入完成期限（格式: YYYY-MM-DD，可選）：", self)
        self.input_due_date = QLineEdit(self)
        self.add_button = QPushButton("新增任務", self)
        self.show_button = QPushButton("顯示任務清單", self)
        self.complete_button = QPushButton("完成任務", self)
        self.delete_button = QPushButton("刪除任務", self)

        #設定布局
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.input_title)
        layout.addWidget(self.description)
        layout.addWidget(self.input_description)
        layout.addWidget(self.due_date)
        layout.addWidget(self.input_due_date)
        layout.addWidget(self.add_button)
        layout.addWidget(self.show_button)
        layout.addWidget(self.complete_button)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)
        
        #事件連接
        self.add_button.clicked.connect(self.add_task)
        self.show_button.clicked.connect(self.show_tasks)
        self.complete_button.clicked.connect(self.complete_task)
        self.delete_button.clicked.connect(self.delete_task)

    def add_task(self):
        text = self.input_title.text()
        if text.strip():
            self.title.setText(f"成功新增任務:{text}")
        else:
            QMessageBox.warning(self, "警告", "任務名稱不能為空白!")

    # 顯示任務清單
    def show_tasks():
        print("\n=== 任務清單 ===")
        print("未完成的任務：")
        if not pending_tasks:
            print("\n  目前沒有任何任務！\n")
        else:
            for idx, task in enumerate(pending_tasks, start=1):
                print(f"  {idx}. {task['title']} ({task['description'][:40]}) ({task['due_date']})") # 描述部份最多顯示 40 個字元
    
        print("\n已完成的任務：")
        if not completed_tasks:
            print("\n  目前沒有任何任務！\n")
        else:
            for idx, task in enumerate(completed_tasks, start=1):
                print(f"  {idx}. {task['title']} ({task['description'][:40]})") # 描述部份最多顯示 40 個字元
        print()

    #完成任務
    def complete_task():
        if not pending_tasks:
            print("\n目前沒有未完成的任務！\n")
            return

        show_tasks()
        try:
            task_idx = int(input("請輸入要完成的任務編號：")) - 1
            if 0 <= task_idx < len(pending_tasks):
                task = pending_tasks.pop(task_idx)
                completed_tasks.append(task)
                print(f"\n成功完成任務：{task['title']}\n")
            else:
                print("\n無效的編號！請重新選擇。\n")
        except ValueError:
            print("\n輸入無效！請輸入數字。\n")

    #刪除任務
    def delete_task():
        print("\n=== 刪除任務 ===")
        show_tasks()

        task_type = input("請選擇任務類型（1: 未完成, 2: 已完成）：").strip()
        if task_type not in ["1", "2"]:
            print("\n無效的選擇！請輸入 1 或 2。\n")
            return

        task_list = pending_tasks if task_type == "1" else completed_tasks
        if not task_list:
            print("\n選擇的任務清單中沒有任務。\n")
            return

        try:
            task_idx = int(input("請輸入要刪除的任務編號：")) - 1
            if 0 <= task_idx < len(task_list):
                task = task_list.pop(task_idx)
                print(f"\n成功刪除任務：{task['title']}\n")
            else:
                print("\n無效的編號！請重新選擇。\n")
        except ValueError:
            print("\n輸入無效！請輸入數字。\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())