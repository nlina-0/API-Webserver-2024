from init import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.exercises_bp import exercises_bp

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(exercises_bp)

# Initial test route
@app.route("/")
def hello():
    return "Hello World!"

@app.errorhandler(404)
# Why does 'err' need to go into the parameter?
def not_found(err):
    return {'error': 'Not Found'}, 404