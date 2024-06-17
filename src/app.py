from init import app
from blueprints.cli_bp import db_commands

app.register_blueprint(db_commands)

# Initial test route
@app.route("/")
def hello():
    return "Hello World!"