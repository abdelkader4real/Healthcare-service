from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('healthcare.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    services = conn.execute('SELECT * FROM services').fetchall()
    conn.close()
    return render_template('index.html', services=services)

@app.route('/service/<int:service_id>')
def service(service_id):
    conn = get_db_connection()
    service = conn.execute('SELECT * FROM services WHERE id = ?', (service_id,)).fetchone()
    
    if service['name'] == 'Clinics':
        items = conn.execute('SELECT * FROM clinics').fetchall()
        template = 'clinics.html'
    elif service['name'] == 'Pharmacies':
        items = conn.execute('SELECT * FROM pharmacies').fetchall()
        template = 'pharmacies.html'
    elif service['name'] == 'Blood Donors':
        items = conn.execute('SELECT * FROM blood_donors WHERE available = 1').fetchall()
        template = 'blood_donors.html'
    
    conn.close()
    return render_template(template, service=service, items=items)

if __name__ == '__main__':
    app.run(debug=True)