import tkinter as tk
from tkinter import messagebox
from task_details_dialog import TaskDetailsDialog

class TaskView(tk.Frame):
    """A view class for displaying tasks and managing user interactions in a task management application."""
    
    def __init__(self, master, controller):
        """Initialize the frame on the given master widget with a reference to the controller."""
        super().__init__(master)
        self.controller = controller

        # Set up the grid configuration for layout management.
        self.grid(sticky="nsew")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Create widgets for the task view.
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange widgets in the frame."""
        # Listbox for displaying tasks.
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Frame for holding action buttons.
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.grid(row=0, column=1, sticky="ns", pady=10)

        # Buttons for various task operations.
        self.archive_button = tk.Button(self.buttons_frame, text="Archive Task", command=lambda: self.controller.archive_task(self.get_selected_task_id()))
        self.archive_button.pack(fill=tk.X, padx=2, pady=6)

        self.switch_view_button = tk.Button(self.buttons_frame, text="", command=self.switch_view)
        self.switch_view_button.pack(fill=tk.X, padx=2, pady=6)

        self.add_button = tk.Button(self.buttons_frame, text="Add Task", command=lambda: self.controller.open_task_dialog())
        self.add_button.pack(fill=tk.X, padx=2, pady=6)

        self.edit_button = tk.Button(self.buttons_frame, text="Edit Task", command=lambda: self.controller.open_task_dialog(self.get_selected_task_id()))
        self.edit_button.pack(fill=tk.X, padx=2, pady=6)

        self.delete_button = tk.Button(self.buttons_frame, text="Delete Task", command=lambda: self.controller.delete_task(self.get_selected_task_id()))
        self.delete_button.pack(fill=tk.X, padx=2, pady=6)

        # Set initial view state based on controller's current view.
        self.update_view_state(self.controller.current_view)

        # Frame for sorting buttons.
        self.sort_buttons_frame = tk.Frame(self)
        self.sort_buttons_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        
        # Buttons for sorting tasks.
        tk.Button(self.sort_buttons_frame, text="Sort by Table Name", command=lambda: self.controller.toggle_sort('table_name')).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=2)
        tk.Button(self.sort_buttons_frame, text="Sort by Last Updated", command=lambda: self.controller.toggle_sort('last_updated')).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=2)

        # Ensure the listbox and button frame use the available space effectively.
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Bind double-click event to display task details.
        self.listbox.bind("<Double-1>", self.display_task_details)

    def update_tasks(self, tasks):
        """Update the list of tasks displayed in the listbox."""
        self.listbox.delete(0, tk.END)
        self.task_ids = [task['id'] for task in tasks]
        for task in tasks:
            self.listbox.insert(tk.END, task['name'])

    def display_task_details(self, event=None):
        """Display the details of the selected task."""
        selected_id = self.get_selected_task_id()
        if selected_id:
            self.controller.display_task_details(selected_id)

    def get_selected_task_id(self):
        """Return the ID of the currently selected task."""
        selected_indices = self.listbox.curselection()
        if selected_indices:
            return self.task_ids[selected_indices[0]]
        return None

    def switch_view(self):
        """Switch the view between active and archived tasks."""
        self.controller.switch_view()

    def update_view_state(self, current_view):
        """Update the UI elements based on the current view state."""
        if current_view == "archived":
            self.archive_button.config(text="Unarchive Task", command=lambda: self.controller.unarchive_task(self.get_selected_task_id()))
            self.switch_view_button.config(text="Switch to Active View")
            self.add_button.pack_forget()
            self.edit_button.pack_forget()
            self.delete_button.pack_forget()
        else:
            self.archive_button.config(text="Archive Task", command=lambda: self.controller.archive_task(self.get_selected_task_id()))
            self.switch_view_button.config(text="Switch to Archived View")
            self.add_button.pack(fill=tk.X, padx=2, pady=6)
            self.edit_button.pack(fill=tk.X, padx=2, pady=6)
            self.delete_button.pack(fill=tk.X, padx=2, pady=6)


