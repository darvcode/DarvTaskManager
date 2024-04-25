import os
import sqlite3
from datetime import datetime

def get_database_path():
    """Determine the filesystem path to the database file."""
    home_dir = os.path.expanduser('~')
    app_data_dir = os.path.join(home_dir, 'Documents', 'vimScripts', 'Python', 'taskManager1.3', 'db') #Modify this path as needed
    if not os.path.exists(app_data_dir):
        os.makedirs(app_data_dir)
    return os.path.join(app_data_dir, 'tasks.db')

class DBManager:
    """Manage database operations for tasks within a SQLite database."""
    
    def __init__(self):
        """Initialize the connection to the SQLite database."""
        db_path = get_database_path()
        self.conn = sqlite3.connect(db_path)

    def load_tasks(self, completed=None, sort_by=None, order='ASC'):
        """Fetch tasks from the database optionally filtering and sorting them."""
        query = 'SELECT id, name, table_name, email, saved_email, task_description, completed FROM tasks'
        params = ()
        if completed is not None:
            query += ' WHERE completed = ?'
            params = (completed,)
        if sort_by:
            query += f' ORDER BY {sort_by} COLLATE NOCASE {order}'

        cursor = self.conn.execute(query, params)
        tasks = []
        for row in cursor.fetchall():
            tasks.append({
                "id": row[0],
                "name": row[1],
                "table_name": row[2],
                "email": row[3],
                "saved_email": row[4],
                "task_description": row[5],
                "completed": bool(row[6])
            })
        cursor.close()
        return tasks 

    def add_task(self, name, table, email, saved_email, task_desc, created_at=None, last_updated=None):
        """Insert a new task into the database."""
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not created_at or not last_updated:
            created_at = last_updated = current_timestamp
        query = "INSERT INTO tasks (name, table_name, email, saved_email, task_description, completed, created_at, last_updated) VALUES (?, ?, ?, ?, ?, 0, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(query, (name, table, email, saved_email, task_desc, created_at, last_updated))
        self.conn.commit()
        cursor.close()

    def delete_task(self, task_id):
        """Remove a task from the database by its ID."""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        changes = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return changes > 0

    def archive_task(self, task_id):
        """Mark a task as completed."""
        cursor = self.conn.cursor()
        cursor.execute('UPDATE tasks SET completed=? WHERE id=?', (1, task_id))
        self.conn.commit()
        changes = cursor.rowcount
        cursor.close()
        return changes > 0

    def unarchive_task(self, task_id):
        """Mark a task as not completed."""
        cursor = self.conn.cursor()
        cursor.execute('UPDATE tasks SET completed=? WHERE id=?', (0, task_id))
        self.conn.commit()
        changes = cursor.rowcount
        cursor.close()
        return changes > 0

    def execute_query(self, query, params):
        """Execute an SQL query directly."""
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        cursor.close()

    def get_task_by_index(self, task_id):
        """Retrieve a single task by its database ID."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, name, table_name, email, saved_email, task_description, completed FROM tasks WHERE id=?', (task_id,))
        task = cursor.fetchone()
        cursor.close()
        if task:
            return {
                "name": task[1],
                "table_name": task[2],
                "email": task[3],
                "saved_email": task[4],
                "task_description": task[5],
            }
        return None

    def update_task(self, task_id, **kwargs):
        """Update fields of an existing task."""
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')        
        query = """UPDATE tasks SET name=?, table_name=?, email=?, saved_email=?, task_description=?, last_updated=? WHERE id=?"""
        params = (
            kwargs['name'],
            kwargs['table_name'],
            kwargs['email'],
            kwargs['saved_email'],
            kwargs['task_description'],
            current_timestamp,
            task_id,
        )
        self.execute_query(query, params)


