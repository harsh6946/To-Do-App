---

# 📂 Project 2: To-Do App (Python Console)

**Files to create:**  
- `todo.py`  
- `README.md`  

---

### `todo.py`
```python
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"✅ Task added: {task}")

def view_tasks():
    print("\n📌 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def remove_task(index):
    try:
        removed = tasks.pop(index-1)
        print(f"❌ Removed: {removed}")
    except:
        print("⚠️ Invalid task number.")

# Example usage
add_task("Finish GitHub project")
add_task("Study for exams")
view_tasks()
remove_task(1)
view_tasks()
