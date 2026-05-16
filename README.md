# Project 06 – FastAPI CRUD API

## Overview

This project focuses on building a simple REST API using **Python** and **FastAPI**.

The API manages a list of DevOps portfolio projects through standard CRUD operations. Data is stored temporarily in an in-memory dictionary, keeping the project lightweight and focused on API design, testing and project structure.

The main goal of this project is to create a clean, local-first API that can be easily tested, documented and prepared for future deployment scenarios such as Docker, AWS Lambda, App Runner, EC2 or Kubernetes.

## Architecture

```
Client / Browser / curl / Postman
        |
        v
FastAPI Application
        |
        v
In-Memory Project Store
```

## What This Project Demonstrates

This project demonstrates how to:

- Build a REST API with FastAPI
- Structure a Python API project professionally
- Implement CRUD operations
- Validate data using Pydantic models
- Test API endpoints with pytest
- Use FastAPI automatic OpenAPI/Swagger documentation
- Prepare an application for future Docker usage
- Keep the application portable across different deployment targets

## Main Technologies

- **Python** – Programming language
- **FastAPI** – Modern web framework for building APIs
- **Uvicorn** – ASGI application server
- **Pydantic** – Data validation using Python type hints
- **Pytest** – Testing framework
- **OpenAPI / Swagger** – Automatic API documentation
- **Docker-ready structure** – Containerization ready
- **Optional AWS Lambda wrapper** – Serverless deployment option

## Project Status

In progress

## Jira

Epic: **DEVOPS-26** – Build FastAPI CRUD API for DevOps portfolio management

### Tasks

- **DEVOPS-27** – Create FastAPI project structure
- **DEVOPS-28** – Implement CRUD endpoints
- **DEVOPS-29** – Add pytest unit tests
- **DEVOPS-30** – Add OpenAPI documentation
- **DEVOPS-31** – Prepare Docker-ready structure
- **DEVOPS-32** – Prepare optional AWS Lambda wrapper

## API Endpoints

The API includes the main CRUD operations for managing DevOps portfolio projects.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/projects` | Returns all projects from the in-memory store |
| GET | `/projects/{project_id}` | Returns a single project by ID |
| POST | `/projects` | Creates a new project |
| PUT | `/projects/{project_id}` | Updates an existing project |
| DELETE | `/projects/{project_id}` | Deletes an existing project |

## Implementation Notes

The CRUD logic was split into separate application layers to keep the project clean and easy to extend.

The `models.py` file defines the Pydantic models used for request validation and response formatting.

The `store.py` file contains the in-memory dictionary used as temporary storage for the projects.

The `main.py` file exposes the FastAPI routes and connects the API endpoints with the store logic.

At this stage, the API uses local in-memory storage only. No external database is used yet, because the focus of this project is API structure, validation, testing and portability.

## Error Handling

The API returns a `404 Not Found` response when a requested project does not exist.

This was added for:

- retrieving a project by ID
- updating a project by ID
- deleting a project by ID


## Automated Testing

Automated tests were added using pytest and FastAPI TestClient.

The test suite validates the main API behavior without requiring the server to be started manually.

The tests cover:

- health check endpoint
- listing projects
- creating a project
- retrieving a project by ID
- updating a project
- deleting a project
- handling missing projects with `404 Not Found` responses

Because the API currently uses an in-memory dictionary, the test state is reset before each test. This keeps the tests isolated and prevents one test from affecting another.

At this stage, the test suite confirms that the CRUD flow works correctly and that the API returns the expected response codes for both successful and failed requests.
