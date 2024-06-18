from init import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)

# Initial test route
@app.route("/")
def hello():
    return "Hello World!"