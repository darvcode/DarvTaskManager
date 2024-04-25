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

4. To start the application, run the following command in the root of the project directory:
   python main.py or go to main folder and execute on cmd >> pyinstaller --onefile --windowed main.py and
   an executable file will be created in a folder called dist.
   **I implemented this code with a fixed database path, modify accordlingly in db_manager.py**

   

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





