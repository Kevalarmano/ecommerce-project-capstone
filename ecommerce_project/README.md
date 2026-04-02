# E-Commerce Project Capstone

## Overview

This project is a full-stack e-commerce backend system built using Django. It demonstrates core concepts of web development, RESTful API design, and deployment.

The application provides a scalable backend capable of handling product management, user interactions, and API-based communication for an e-commerce platform.

---

## Key Features

### Backend Functionality

* RESTful API architecture
* Full CRUD (Create, Read, Update, Delete) operations
* Modular Django app structure
* SQLite database integration (default)

### API Capabilities

* Endpoint-based data access
* JSON responses
* Easily extendable for frontend integration (React, mobile apps, etc.)

### Deployment Ready

* Dockerized application
* Environment isolation using virtual environments
* Production-ready structure

---

## Tech Stack

* Backend Framework: Django
* Language: Python
* Database: SQLite
* Containerization: Docker
* Version Control: Git and GitHub

---

## Project Structure

```bash
ecommerce-project-capstone/
│── manage.py
│── requirements.txt
│── db.sqlite3
│── Dockerfile
│
├── project/              # Main Django project
│   ├── settings.py
│   ├── urls.py
│
├── app/                  # Core application (CRUD logic)
│
├── docs/                 # Sphinx documentation
│   ├── conf.py
│   ├── index.rst
│   ├── _build/
```

---

## Local Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Kevalarmano/ecommerce-project-capstone.git
cd ecommerce-project-capstone
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run Server

```bash
python manage.py runserver
```

### 7. Access Application

http://127.0.0.1:8000/

---

## Docker Setup

### 1. Build Docker Image

```bash
docker build -t ecommerce-app .
```

### 2. Run Container

```bash
docker run -p 8000:8000 ecommerce-app
```

### 3. Access Application

http://localhost:8000/

---

## API Endpoints (Example)

| Method | Endpoint      | Description          |
| ------ | ------------- | -------------------- |
| GET    | /api/items/   | Retrieve all items   |
| GET    | /api/items/id | Retrieve single item |
| POST   | /api/items/   | Create new item      |
| PUT    | /api/items/id | Update item          |
| DELETE | /api/items/id | Delete item          |

---

## Documentation

This project includes documentation generated using Sphinx.

To build documentation:

```bash
cd docs
make html
```

Then open:
docs/_build/html/index.html

---

## Testing (Optional)

Run tests using:

```bash
python manage.py test
```

---

## Future Improvements

* User authentication (JWT or OAuth)
* Payment gateway integration
* Frontend (React or Next.js)
* PostgreSQL database upgrade
* CI/CD pipeline integration

---

## Author

Keval Armano Ramchander
GitHub: https://github.com/Kevalarmano

---

## License

This project is for academic purposes and learning.

---

## Submission Notes

* Fully functional Django backend
* Dockerized environment included
* Sphinx documentation configured
* GitHub repository properly structured
