from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


import os
# Get the directory where the current file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to 'data.json' relative to the current directory
data_file_path = os.path.join(current_dir, 'data.json')
@app.route('/api')
def api():
    # return current_dir AND dir contents
    # return current_dir + '\n' + str(os.listdir(current_dir)) 
    
    with open(data_file_path , mode='r') as my_file:
        text = my_file.read()
        return text