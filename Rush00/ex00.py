import os

class SmartFarm:
    def __init__(self):
        self.task_types = {}
        self.tasks_list = {}
        self.index = 1

    def show_select_option(self):
        print("====== Smart Farm Task Organizer ======")
        print("1. เพิ่มงานในฟาร์ม")
        print("2. แสดงรายการงานทั้งหมด")
        print("3. ลบงาน")
        print("4. สรุปจำนวนงานในแต่ละประเภท")
        print("5. ออกจากโปรแกรม")
        option = str(input("เลือกเมนู (1-5): "))
        if option == "1":
            self.add_task()
        elif option == "2":
            self.show_tasks_list()
        elif option == "3":
            self.delete_task()
        elif option == "4":
            self.show_types()
        elif option == "5":
            self.exit_app()

    def add_task(self):
        task_name = str(input("📌 ป้อนชื่องาน: "))
        task_date = str(input("📆 ป้อนวันที่ (dd/mm/yyyy): "))
        task_type = str(input("🌾 ประเภทงาน (พืช/ปศุสัตว์/อื่นๆ): "))
        self.tasks_list.update({task_name: {"date": task_date, "type": task_type}})

        if task_type in self.task_types:
            self.task_types[task_type] += 1
        else:
            self.task_types[task_type] = 1

        print("✅ เพิ่มงานสำเร็จ")
        self.show_select_option()

    def show_tasks_list(self):
        print("📃 รายการทั้งหมด")
        if self.tasks_list:
            for name, task in self.tasks_list.items():
                print(f"{self.index}. {task['date']} - {name} ({task['type']})")
            self.index = 1
        else:
            print("⚠️ ไม่มีรายการงาน")
        self.show_select_option()

    def delete_task(self):
        if not self.tasks_list:
            print("⚠️ ไม่มีงานให้ลบ")
            self.show_select_option()
            return

        index_to_delete = int(input("🔻 ลำดับของงานที่ต้องการลบ: ")) - 1
        for i, (name, task) in enumerate(self.tasks_list.items()):
            if i == index_to_delete:
                if task['type'] in self.task_types:
                    self.task_types[task['type']] -= 1
                    if self.task_types[task['type']] == 0:
                        del self.task_types[task['type']]
                del self.tasks_list[name]
                print(f"🗑️ ลบงาน: {name} แล้ว")
                break
        self.show_select_option()

    def show_types(self):
        print("📊 สรุปจำนวนงานแต่ละประเภท:")
        if not self.task_types:
            print("⚠️ ไม่มีรายการงาน")
            self.show_select_option()
            return
        for task_type, size in self.task_types.items():
            print(f"- {task_type}: {size} งาน")
        self.show_select_option()

    def exit_app(self):
        print("👋 ขอบคุณที่ใช้โปรแกรม Smart Farm!")
        os._exit(0)

def main():
    """ MAIN """
    smart_farm = SmartFarm()
    smart_farm.show_select_option()

main()
