from tkinter import messagebox
from task_details_dialog import TaskDetailsDialog
from config import FIELD_LABELS

class TaskController:
    """Controller managing task operations between the view and the database."""
    
    def __init__(self, db_manager, parent_window):
        """Initialize the controller with a database manager and the main application window."""
        self.db_manager = db_manager
        self.parent_window = parent_window
        self.view = None
        self.current_view = "active"
        self.sort_order = {'table_name': 'DESC', 'last_updated': 'DESC'} 

    def set_view(self, view):
        """Set the view component that this controller will manage."""
        self.view = view

    def load_tasks(self, completed=None):
        """Load and display tasks based on completion status."""
        tasks = self.db_manager.load_tasks(completed, self.sort_by)
        self.view.update_tasks(tasks) 

    def toggle_sort(self, sort_field):
        """Toggle the sorting order of the task list."""
        current_order = self.sort_order.get(sort_field, 'DESC')
        new_order = 'ASC' if current_order == 'DESC' else 'DESC'
        self.sort_order[sort_field] = new_order
        self.refresh_task_list(sort_by=sort_field, order=new_order)

    def refresh_task_list(self, sort_by=None, order='ASC'):
        """Refresh the task list based on the current view and sort order."""
        completed = None if self.current_view == "all" else (self.current_view == "archived")
        tasks = self.db_manager.load_tasks(completed, sort_by, order)
        self.view.update_tasks(tasks) 

    def switch_view(self):
        """Switch between active and archived task views."""
        self.current_view = "archived" if self.current_view == "active" else "active"
        self.refresh_task_list()
        self.view.update_view_state(self.current_view) 

    def display_task_details(self, task_id):
        """Display details of a task in a dialog."""
        raw_task_details = self.db_manager.get_task_by_index(task_id)
        if raw_task_details:
            task_details = {k: v for k, v in raw_task_details.items() if k not in ['id', 'completed']}
            TaskDetailsDialog(self.parent_window, "View Task", task_details, {'editable': False, 'expand_description': True})
        else:
            messagebox.showerror("Error", "Task not found.", parent=self.parent_window)

    def open_task_dialog(self, task_id=None):
        """Open a dialog to add or edit a task."""
        title = "Edit Task" if task_id else "Add New Task"
        task_details = self.db_manager.get_task_by_index(task_id) if task_id else {key: "" for key in FIELD_LABELS.keys()}
        dialog = TaskDetailsDialog(self.parent_window, title, task_details, {'editable': True, 'expand_description': True})
        if dialog.result:
            if task_id:
                self.db_manager.update_task(task_id, **dialog.result)
            else:
                self.db_manager.add_task(name=dialog.result.get('name'), 
                                         table=dialog.result.get('table_name'), 
                                         email=dialog.result.get('email'), 
                                         saved_email=dialog.result.get('saved_email'), 
                                         task_desc=dialog.result.get('task_description'))
            self.refresh_task_list()
         
    def delete_task(self, task_id):
        """Delete a specified task after confirmation."""
        if not task_id:
            messagebox.showerror("Error", "No task selected for deletion.")
            return
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this task?"):
            if self.db_manager.delete_task(task_id):
                messagebox.showinfo("Success", "Task successfully deleted.")
                self.refresh_task_list()
            else:
                messagebox.showerror("Error", "Failed to delete task.")

    def archive_task(self, task_id):
        """Archive a specified task."""
        if not task_id:
            messagebox.showerror("Error", "No task selected for archiving.")
            return
        if self.db_manager.archive_task(task_id):
            messagebox.showinfo("Success", "Task successfully archived.")
            self.refresh_task_list()
        else:
            messagebox.showerror("Error", "Failed to archive task.")

    def unarchive_task(self, task_id):
        """Unarchive a specified task."""
        if not task_id:
            messagebox.showerror("Error", "No task selected for unarchiving.")
            return
        if self.db_manager.unarchive_task(task_id):
            messagebox.showinfo("Success", "Task successfully unarchived.")
            self.refresh_task_list()
        else:
            messagebox.showerror("Error", "Failed to unarchive task.")


