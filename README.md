## DarvTaskManager
DarvTaskManager is a versatile task management application designed to efficiently organize, track, archive, and manage tasks. Equipped with features like task addition, editing, archiving, and viewing in different modes (active and archived), DarvTaskManager ensures that you stay on top of your tasks. Ideal for personal productivity and auditing, this app provides tools to manage your tasks from creation to completion.

Fields are customizable to suit individual or business needs, reflecting the versatility of the app.

## Features
- **Task Addition**: Easily add new tasks with comprehensive details.
- **Task Editing**: Update existing tasks to reflect changes or current status.
- **Task Deletion**: Remove tasks that are no longer necessary.
- **Task Archiving**: Keep your active task list clutter-free by moving completed tasks to an archived state.
- **View Switching**: Switch between active and archived views to focus on tasks relevant to your current needs.
- **Task Viewing**: Access detailed descriptions and status of tasks through a modal dialogue by double-clicking a task.
- **Sorting**: Sorting available: alphabetical order and last date modified.

## Roadmap
Planned features for future releases:

- **Filters**: Enhance task visibility and management efficiency by implementing filters that allow users to easily audit tasks based on various criteria.
- **Dynamic GUI**: Improve the user experience across different devices with a dynamic layout that adjusts seamlessly to various screen sizes.
- **Export Data**: Enable data export to CSV or Excel formats for improved project tracking and communication with management.

## Prerequisites
Before installation, ensure you have Python installed on your system. If not, download it from python.org.

## Installation
To install DarvTaskManager, follow these steps:

Clone the repository:
1. git clone https://github.com/darvcode/DarvTaskManager.git

2. Navigate to the project directory

3. Install the necessary dependencies (ensure you have Python installed)

4. To start the application, you have two primary options:

### Running Directly with Python

Navigate to the root of the project directory and run the following command:

```bash
python main.py /bash
```

This method allows you to run the application directly from the source code.

### Creating an Executable

If you prefer to create an executable, navigate to the main folder and execute the following command in the command prompt (cmd):

```bash
pyinstaller --onefile --windowed main.py
```

This command uses PyInstaller to compile the application into a single executable file, which will be located in a folder named `dist` within your project directory.

### Note on Database Configuration

The application uses a fixed path for the database file, located within the `db_manager.py` file. If the default database path does not suit your needs or if you encounter issues with database access (particularly after moving the application to a different environment), you may need to modify the path accordingly:

1. Open the `db_manager.py` file.
2. Locate the `get_database_path` function.
3. Adjust the path in the `app_data_dir` line to an appropriate location on your system.

Ensure the chosen path is accessible and writable by the application to avoid any runtime errors.

## Database Setup
DarvTaskManager uses a pre-configured SQLite database (tasks.db). This database should exist in the project directory with the following schema:

**tasks table:
- **id: Integer**, primary key, auto-increment.
- **name**: String.
- **table_name**: String.
- **email: String**.
- **saved_email**: String.
- **task_description**: Text.
- **completed**: Integer (0 for active, 1 for archived).

No syntax restrictions are imposed on the fields, offering flexibility for adaptation and use.

## Additional Tools
For data retrieval and management, DBeaver is used to execute SQL queries effectively, facilitating ongoing communication with management and aiding in task review and personal audits.





