# Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
 """Thêm một công việc mới vào danh sách."""
 tasks.append({
    'name': task_name,
    'completed': False
})
def complete_task(task_index):
    """Đánh dấu một công việc là hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("Chỉ số công việc không hợp lệ!")

    print(f"Đã thêm công việc: {task_name}'")
def delete_task(task_index):
    """Xóa công việc theo chỉ số."""
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Đã xóa: {removed['name']}")
    else:
        print("Chỉ số không hợp lệ, không thể xóa!")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
 print("Chào mừng đến với ứng dụng To-Do List!")
 add_task("Học bài Git và GitHub")
 add_task("Làm bài tập thực hành ở nhà")
 
 def list_tasks():
    """In ra danh sách các công việc hiện có."""
    if not tasks:
        print("Không có công việc nào.")
    else:
        print("\nDanh sách công việc:")
        for i, task in enumerate(tasks, 1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")
if __name__ == "__main__":
 complete_task(0)
 list_tasks()
