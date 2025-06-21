# Messaging App Docker Setup

This is a Django REST API messaging application containerized with Docker and Docker Compose.

## Prerequisites

- Docker and Docker Compose installed
- Git

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd messaging_app
```

2. Create your environment file (already provided as `.env`):
```bash
# The .env file contains:
MYSQL_DB=messaging_app_db
MYSQL_USER=messaging_user
MYSQL_PASSWORD=messaging_password123
MYSQL_ROOT_PASSWORD=root_password123
SECRET_KEY=django-insecure-wk4e+8ub51x5n5$e_z%3+%l=3i)zn!uc$-(bhdwggvmumj8)5p
DEBUG=True
```

3. Build and run the application:
```bash
docker-compose up --build
```

4. Run database migrations (in another terminal):
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

5. Create a superuser (optional):
```bash
docker-compose exec web python manage.py createsuperuser
```

## Services

- **Web Service**: Django application running on port 8000
- **Database Service**: MySQL 8.0 running on port 3306

## Features

- Django REST Framework API
- JWT Authentication
- MySQL Database with persistent volumes
- Environment variable configuration
- Docker containerization

## API Endpoints

The application will be available at `http://localhost:8000`

## Stopping the Application

```bash
docker-compose down
```

To stop and remove volumes:
```bash
docker-compose down -v
```

## Development

For development, you can mount your local code and make changes:
```bash
docker-compose up
```

The application will reload automatically when you make changes to the code.
