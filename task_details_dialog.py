import tkinter as tk
from tkinter import simpledialog, Label, Text, Entry, StringVar
from config import FIELD_LABELS

class TaskDetailsDialog(simpledialog.Dialog):
    """
    Custom dialog class for displaying and editing details of a task.
    Extends simpledialog.Dialog to provide specific functionality for task management.
    """
    
    def __init__(self, parent, title, task_details, configuration):
        """
        Initialize the dialog with task details and configuration.
        
        :param parent: Parent window.
        :param title: Dialog title.
        :param task_details: Dictionary containing task details to display.
        :param configuration: Configuration options for dialog (editable, expand_description).
        """
        self.task_details = task_details
        self.configuration = configuration
        super().__init__(parent, title)

    def body(self, master):
        """
        Create the body of the dialog with task fields.
        
        :param master: Master widget to which body components are added.
        """
        self.entry_widgets = {}
        row = 0
        description_field = None

        # Create entries for all fields except the description, which is handled separately.
        for field, value in self.task_details.items():
            if field == "task_description":
                description_field = (field, value)
                continue

            label = Label(master, text=f"{field}:")
            label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
            entry_var = StringVar(master, value=value)
            entry = Entry(master, textvariable=entry_var, width=50)
            entry.grid(row=row, column=1, sticky="ew", padx=5, pady=5)
            if not self.configuration.get('editable', True):
                entry.configure(state='readonly')
            self.entry_widgets[field] = entry
            row += 1

        # Add a larger text widget for the description field, if present.
        if description_field:
            field, value = description_field
            label = Label(master, text=f"{field}:")
            label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
            text_widget = Text(master, height=10, width=60)
            text_widget.insert("1.0", value)
            if not self.configuration.get('editable', True):
                text_widget.configure(state='disabled')
            text_widget.grid(row=row, column=1, sticky="ew", padx=5, pady=5)
            self.entry_widgets[field] = text_widget

    def buttonbox(self):
        """
        Add standard button box with OK and Cancel.
        """
        box = tk.Frame(self)
        ok_btn = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        ok_btn.pack(side=tk.LEFT, padx=5, pady=5)
        if self.configuration.get('editable', True):
            cancel_btn = tk.Button(box, text="Cancel", width=10, command=self.cancel)
            cancel_btn.pack(side=tk.RIGHT, padx=5, pady=5)
        box.pack()

    def validate(self):
        """
        Validate the data entered by the user.
        """
        return True  # For self convenince no validation needed for now 

    def apply(self):
        """
        Process the data entered by the user when the dialog is closed with OK.
        """
        self.result = {}
        for field, widget in self.entry_widgets.items():
            if isinstance(widget, Text):
                self.result[field] = widget.get("1.0", "end-1c").strip()  # Trim the last newline.
            else:
                self.result[field] = widget.get()

