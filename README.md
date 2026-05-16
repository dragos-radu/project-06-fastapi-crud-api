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
