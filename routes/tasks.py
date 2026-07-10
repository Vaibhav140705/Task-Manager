from flask import Blueprint, render_template, request, redirect, url_for, session

from config import TASK_OPTIONS, STATUS_OPTIONS, PRIORITY_OPTIONS
from models.task import TaskModel

task_bp = Blueprint("task", __name__)


# ---------------- Dashboard ----------------

@task_bp.route("/dashboard")
def dashboard():

    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    tasks = TaskModel.get_all_tasks()

    stats = TaskModel.get_statistics()

    return render_template(
        "dashboard.html",
        username=session["username"],
        tasks=tasks,
        task_options=TASK_OPTIONS,
        status_options=STATUS_OPTIONS,
        priority_options=PRIORITY_OPTIONS,
        total_tasks=stats["total"],
        completed_tasks=stats["completed"],
        pending_tasks=stats["pending"],
        overdue_tasks=stats["overdue"]
    )


# ---------------- Add Task ----------------

@task_bp.route("/add_task", methods=["POST"])
def add_task():

    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    TaskModel.add_task(
        request.form.get("task"),
        request.form.get("assigned_to"),
        request.form.get("priority"),
        request.form.get("deadline"),
        request.form.get("description"),
        request.form.get("status")
    )

    return redirect(url_for("task.dashboard"))


# ---------------- Toggle Task ----------------

@task_bp.route("/toggle/<int:task_id>")
def toggle_task(task_id):

    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    TaskModel.toggle_task(task_id)

    return redirect(url_for("task.dashboard"))


# ---------------- Delete Task ----------------

@task_bp.route("/delete/<int:task_id>")
def delete_task(task_id):

    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    TaskModel.delete_task(task_id)

    return redirect(url_for("task.dashboard"))