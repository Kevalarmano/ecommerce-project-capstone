# Django E-commerce API

## Description
This is a Django-based web application that provides API functionality for an e-commerce system.

## Features
- REST API
- CRUD operations
- Django backend

## Setup (Local)
git clone <your-repo-link>
cd project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

## Docker Setup
docker build -t ecommerce-app .
docker run -p 8000:8000 ecommerce-app

## Documentation
Open docs/index.html
