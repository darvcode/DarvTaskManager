import tkinter as tk
from task_view import TaskView
from task_controller import TaskController
from db_manager import DBManager

def main():
    root = tk.Tk()
    root.title("Task Manager")
    
    # Initialize the core components of the MVC architecture
    db_manager = DBManager()
    app_controller = TaskController(db_manager=db_manager, parent_window=root)
    app_view = TaskView(master=root, controller=app_controller)
    
    app_controller.set_view(app_view)  # Link the view to the controller
    
    root.geometry("400x300")  # Set initial window size
    root.minsize(400, 300)    # Set minimum window size

    app_controller.refresh_task_list()  # Display the initial list of tasks
    root.mainloop()  # Start the GUI event loop

if __name__ == "__main__":
    main()
