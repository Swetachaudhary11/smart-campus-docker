# Smart Campus Management System using Docker

## Project Overview

This project is a Dockerized Smart Campus Management System built using Python Flask and Docker Compose.

The project contains multiple services running inside separate Docker containers:

- Student Portal
- Attendance Service
- Notification Service
- Admin Dashboard
- MySQL Database

The main goal of this project is to demonstrate Docker, multi-container architecture, container networking, persistent storage, and CI/CD integration.

---

# Technologies Used

- Python
- Flask
- Docker
- Docker Compose
- MySQL
- GitHub Actions

---

# Project Structure

```text
smart-campus/
│
├── student-portal/
├── attendance-service/
├── notification-service/
├── admin-dashboard/
│
├── docker-compose.yml
├── .env
│
└── .github/
    └── workflows/
        └── docker.yml
```

---

# Services

| Service | Port |
|---|---|
| Student Portal | 5000 |
| Attendance Service | 5001 |
| Notification Service | 5002 |
| Admin Dashboard | 5003 |
| MySQL Database | 3306 |

---

# Docker Features Implemented

- Dockerfile
- Docker Images
- Docker Containers
- Docker Compose
- Multi-container Architecture
- Docker Networking
- Docker Volumes
- Environment Variables
- Restart Policies
- CI/CD Workflow

---

# Run Project

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

---

## Go to Project Folder

```bash
cd smart-campus
```

---

## Start Docker Compose

```bash
docker compose up --build
```

---

# Access Application

Open browser:

```text
http://localhost:5000
http://localhost:5001
http://localhost:5002
http://localhost:5003
```

---

# Useful Docker Commands

## Check Containers

```bash
docker ps
```

---

## Check Networks

```bash
docker network ls
```

---

## Check Volumes

```bash
docker volume ls
```

---

## Stop Containers

```bash
docker compose down
```

---

# Environment Variables

Create `.env` file:

```env
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=campusdb
```

---

# CI/CD

GitHub Actions is used for CI/CD automation.

Workflow file:

```text
.github/workflows/docker.yml
```

The workflow automatically:
- builds Docker images
- starts containers
- verifies services

---

# Learning Outcomes

This project helped in understanding:

- Docker Fundamentals
- Containerization
- Docker Compose
- Multi-container Applications
- Networking and Volumes
- CI/CD Integration

---

# Author

Sweta Chaudhary