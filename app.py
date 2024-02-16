from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file # For webpage rendering and management
import json

app = Flask(__name__)

def parse(file):
    with open(file, 'r') as json_file:
        data = json.load(json_file)
        return data['sites']

config = 'conf.json'
site_details = parse(config)[0]

# fetch butler ip from the conf.json
host = next((server['ip'] for server in site_details['ips'] if server['server'] == 'butler'), None)
print(host)

@app.route('/')
def index():
    sitename = site_details['name']
    print(sitename)
    
    return render_template('index.html', sitename=sitename)

if __name__ == '__main__':
    app.run(host=host, port=5005)
    # app.run(debug=True)