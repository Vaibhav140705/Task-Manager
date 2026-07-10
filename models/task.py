from database import get_db_connection
from datetime import datetime


class TaskModel:

    @staticmethod
    def get_all_tasks():

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tasks
            ORDER BY deadline ASC, created_at DESC
        """)

        tasks = cursor.fetchall()

        conn.close()

        return tasks

    @staticmethod
    def add_task(
        task,
        assigned_to,
        priority,
        deadline,
        description,
        status
    ):

        completed = 1 if status == "Completed" else 0

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tasks
            (
                task,
                assigned_to,
                priority,
                deadline,
                description,
                status,
                completed
            )

            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            task,
            assigned_to,
            priority,
            deadline,
            description,
            status,
            completed
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_task(task_id):

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id=?",
            (task_id,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def toggle_task(task_id):

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT completed FROM tasks WHERE id=?",
            (task_id,)
        )

        task = cursor.fetchone()

        if task:

            if task["completed"] == 1:

                cursor.execute("""
                    UPDATE tasks
                    SET completed=0,
                        status='Pending'
                    WHERE id=?
                """,
                (task_id,)
                )

            else:

                cursor.execute("""
                    UPDATE tasks
                    SET completed=1,
                        status='Completed'
                    WHERE id=?
                """,
                (task_id,)
                )

        conn.commit()
        conn.close()

    @staticmethod
    def get_statistics():

        tasks = TaskModel.get_all_tasks()

        total_tasks = len(tasks)

        completed_tasks = sum(
            1 for task in tasks
            if task["completed"] == 1
        )

        pending_tasks = total_tasks - completed_tasks

        overdue_tasks = 0

        today = datetime.today().date()

        for task in tasks:

            if task["completed"] == 0:

                deadline = datetime.strptime(
                    task["deadline"],
                    "%Y-%m-%d"
                ).date()

                if deadline < today:
                    overdue_tasks += 1

        return {
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": pending_tasks,
            "overdue": overdue_tasks
        }