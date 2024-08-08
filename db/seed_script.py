import psycopg2
from faker import Faker
import random

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="reservation_system",
    user="dp",
    password="password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
fake = Faker()

def create_tables(cur):
    try:
        # drop tables if they exist
        drop_tables = """
        DROP TABLE IF EXISTS reservations CASCADE;
        DROP TABLE IF EXISTS seat_holds CASCADE;
        DROP TABLE IF EXISTS seats CASCADE;
        DROP TABLE IF EXISTS customers CASCADE;
        DROP TABLE IF EXISTS venues CASCADE;
        """
        cur.execute(drop_tables)
        
        # create tables
        create_venues_table = """
        CREATE TABLE venues (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            location VARCHAR(255),
            capacity INT
        );
        """
        
        create_seats_table = """
        CREATE TABLE seats (
            id SERIAL PRIMARY KEY,
            venue_id INT REFERENCES venues(id),
            section VARCHAR(255),
            row VARCHAR(255),
            number VARCHAR(255),
            is_held BOOLEAN DEFAULT FALSE
        );
        """
        
        create_customers_table = """
        CREATE TABLE customers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(255)
        );
        """
        
        cur.execute(create_venues_table)
        cur.execute(create_seats_table)
        cur.execute(create_customers_table)
        conn.commit()
        print("Tables created successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error creating tables: {e}")

def seed_venues(cur, num_venues=30):
    try:
        venues = []
        for i in range(num_venues):
            venues.append((fake.company(), fake.city(), random.randint(25000, 100000)))
        cur.executemany("INSERT INTO venues (name, location, capacity) VALUES (%s, %s, %s)", venues)
        conn.commit()
        print(f"Seeded {num_venues} venues successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error seeding venues: {e}")

def seed_seats(cur, num_venues=30):
    try:
        cur.execute("SELECT id, capacity FROM venues")
        venues = cur.fetchall()
        for venue_id, capacity in venues:
            seats = []
            for _ in range(capacity):
                section = fake.lexify(text='Section ???')
                row = fake.lexify(text='Row ??')
                number = fake.numerify(text='Seat ###')
                seats.append((venue_id, section, row, number, False))
            cur.executemany("INSERT INTO seats (venue_id, section, row, number, is_held) VALUES (%s, %s, %s, %s, %s)", seats)
            conn.commit()
        print("Seeded seats successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error seeding seats: {e}")

def seed_customers(cur, num_customers=5000):
    try:
        customers = []
        for _ in range(num_customers):
            customers.append((fake.name(), fake.email(), fake.phone_number()))
        cur.executemany("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)", customers)
        conn.commit()
        print(f"Seeded {num_customers} customers successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error seeding customers: {e}")

def main():
    try:
        print("Creating tables if they don't exist...")
        create_tables(cur)
        print("Seeding venues...")
        seed_venues(cur)
        print("Seeding seats...")
        seed_seats(cur)
        print("Seeding customers...")
        seed_customers(cur)
        print("Seeding completed!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
