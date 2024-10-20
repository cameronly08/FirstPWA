from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
   data = dbHandler.listExtension()
   return render_template('/index.html', content=data)

@app.route('/add.html', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        if dbHandler.insertContact(email, name):
            return render_template('add.html', is_done=True)  # Successful submission
        else:
            return render_template('add.html', is_done=False, error="Email already exists.")  # Handle duplicate email
    else:
        return render_template('add.html', is_done=False)  # Initial load



if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)

