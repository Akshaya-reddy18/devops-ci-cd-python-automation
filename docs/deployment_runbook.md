# Deployment Runbook

This document describes the process required to deploy the DevOps Python API.

## Prerequisites

1. Target Linux Server with Docker and SSH access.
2. A user (`DEPLOY_SSH_USER`) on the server who has permissions to pull and run Docker containers.
3. Access to configuring GitHub Secrets on your repository.

## GitHub Secrets Configuration

Before the pipeline can successfully deploy the application, ensure the following secrets are added to your GitHub repository:

- `DOCKERHUB_USERNAME`: Your Docker Hub username.
- `DOCKERHUB_TOKEN`: A Docker Hub Personal Access Token for securely pushing images.
- `DEPLOY_SERVER_IP`: The IP address or hostname of the target deployment server.
- `DEPLOY_SSH_USER`: The SSH username used for the connection.
- `DEPLOY_SSH_KEY`: The private SSH key matching the public key deployed on the server for `DEPLOY_SSH_USER`.
- `APP_SECRET_KEY`: Random string for your Flask app context (optional, but good practice).

## Manual Deployment Process (Fallback)

If the automated CI/CD pipeline fails, you can manually deploy the application:

1. SSH into the deployment server:
   ```bash
   ssh user@your-server-ip
   ```
2. Pull the latest Docker Image from Docker Hub:
   ```bash
   docker pull yourusername/devops-python-api:latest
   ```
3. Stop and Remove the existing container:
   ```bash
   docker stop devops-api
   docker rm devops-api
   ```
4. Run the new container:
   ```bash
   docker run -d -p 5000:5000 --name devops-api --restart unless-stopped yourusername/devops-python-api:latest
   ```
5. Verify the API is up by running the `scripts/monitor.py` or manually curling the health endpoint:
   ```bash
   curl http://localhost:5000/health
   ```
