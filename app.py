from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file # For webpage rendering and management
import json

app = Flask(__name__)

def parse(file):
    with open(file, 'r') as json_file:
        data = json.load(json_file)
        return data['sites']

@app.route('/')
def index():
    config = 'conf.json'
    sitename = parse(config)[0]
    print(sitename)
    return render_template('index.html', sitename=sitename)

if __name__ == '__main__':
    app.run(debug=True)
