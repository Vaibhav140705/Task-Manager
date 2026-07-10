import os

# -----------------------------
# Base Directory
# -----------------------------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# -----------------------------
# Database Configuration
# -----------------------------
DATABASE_NAME = "taskmanager.db"
DATABASE_PATH = os.path.join(BASE_DIR, "database", DATABASE_NAME)

# -----------------------------
# Flask Configuration
# -----------------------------
SECRET_KEY = "task_manager_secret_key"

# -----------------------------
# Default Login Credentials
# -----------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

# -----------------------------
# Task Dropdown Options
# -----------------------------
TASK_OPTIONS = [
    "Create Excel",
    "Create Document",
    "Generate MOM",
    "Write Automation Script",
    "Prepare Presentation",
    "Send Email Report"
]

# -----------------------------
# Task Status Options
# -----------------------------
STATUS_OPTIONS = [
    "Pending",
    "In Progress",
    "Completed"
]

# -----------------------------
# Task Priority Options
# -----------------------------
PRIORITY_OPTIONS = [
    "High",
    "Medium",
    "Low"
]