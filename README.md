# Reservation App

Welcome to the Reservation App! This application is designed to manage and track reservations with a backend powered by PostgreSQL. Below you'll find all the necessary steps to get the app up and running, including how to access and seed the database.

## 🚀 Getting Started

### 1. Build and Run the Containers

To build and start the entire application using Docker Compose, run:

```bash
docker-compose up --build
```

### 2. Run the PostgreSQL Service in Detached Mode

If you only need to start the PostgreSQL service, you can do so with:

```bash
docker-compose up -d postgres
```

### 3. Seed the Database

Populate your database with initial data by running the seed script:

```bash
python db/seed_script.py
```

### 4. Access the Database via a DB Management Tool

If you prefer a GUI to manage your database, such as DBeaver, use the following connection details:

- **Host:** `localhost`
- **Port:** `54320`
- **Database:** `reservation_system`

### 5. Access the Database from Within the `web` Service

For internal service communication, use these settings:

- **Host:** `192.168.96.2`
- **Port:** `5432`
- **Database:** `reservation_system`

> **Note:** If you're unsure of the IP address, you can easily find it by running:
>
> ```bash
> docker inspect CONTAINER_ID | grep "IPAddress"
> ```
```
