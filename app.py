from flask import Flask
from config import SECRET_KEY
from routes.auth import auth_bp
from routes.tasks import task_bp
from database import init_db

app = Flask(__name__)

# Secret key for session management
app.secret_key = SECRET_KEY

# Initialize SQLite database
init_db()

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)

if __name__ == "__main__":
    app.run(debug=True)