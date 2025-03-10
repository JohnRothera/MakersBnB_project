import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/register', methods=['GET'])
def get_register():
    connection = get_flask_database_connection(app)
    return render_template('register_user.html')

@app.route('/register', methods=['POST'])
def send_new_registration():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    new_user = User(request.form)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


