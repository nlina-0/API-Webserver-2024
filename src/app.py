from marshmallow.exceptions import ValidationError
from init import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.exercises_bp import exercises_bp
from blueprints.sessions_bp import sessions_bp


app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(exercises_bp)
app.register_blueprint(sessions_bp)

# Initial test route
@app.route("/")
def hello():
    return "Hello World!"

@app.errorhandler(404)
def not_found(err):
    return {'error': 'Not Found'}, 404

@app.errorhandler(ValidationError)
def invalid_request(err):
    return {"error": vars(err)["messages"]}, 400

@app.errorhandler(KeyError)
def missing_key(err):
    return {"error": f"Missing field: {str(err)}"}, 400

# prints all routes
print(app.url_map)
