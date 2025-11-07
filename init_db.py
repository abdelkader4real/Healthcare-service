import sqlite3

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect('healthcare.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS clinics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    specialization TEXT,
    working_hours TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pharmacies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    working_hours TEXT,
    is_24h BOOLEAN DEFAULT 0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS blood_donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    blood_type TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT,
    last_donation_date TEXT,
    city TEXT,
    available BOOLEAN DEFAULT 1
)
''')

# Insert sample data
cursor.executescript('''
INSERT INTO services (name, description) VALUES 
    ("Clinics", "Medical clinics and specialized centers"),
    ("Pharmacies", "Pharmacies and drug stores"),
    ("Blood Donors", "Blood donors information");

INSERT INTO clinics (name, address, phone, specialization, working_hours) VALUES
    ("City General Hospital", "123 Main St", "(555) 123-4567", "General Medicine", "Mon-Fri 8AM-6PM"),
    ("Heart Specialists", "456 Heart Ave", "(555) 987-6543", "Cardiology", "Mon-Fri 9AM-5PM");

INSERT INTO pharmacies (name, address, phone, working_hours, is_24h) VALUES
    ("QuickCare Pharmacy", "789 Drug Lane", "(555) 456-7890", "24/7", 1),
    ("Neighborhood Pharmacy", "321 Health St", "(555) 234-5678", "Mon-Sat 8AM-10PM", 0);

INSERT INTO blood_donors (name, blood_type, contact_number, city) VALUES
    ("John Smith", "A+", "(555) 111-2222", "Cityville"),
    ("Maria Garcia", "O-", "(555) 333-4444", "Townsville");
''')

conn.commit()
conn.close()