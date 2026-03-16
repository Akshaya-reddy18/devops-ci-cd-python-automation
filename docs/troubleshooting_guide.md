# Troubleshooting Guide

## Issue: Docker Build Fails in Pipeline
**Symptoms:** The GitHub Actions `docker-build-push` step fails at the dependency installation.
**Resolution:**
- Confirm `app/requirements.txt` does not have conflicting package versions.
- Check if Dockerfile paths align with the context logic (e.g. `COPY app/requirements.txt .`).

## Issue: Pipeline Cannot Connect to Deployment Server
**Symptoms:** The `deploy` step fails with an SSH timeout or "Permission denied (publickey)".
**Resolution:**
- Validate that the `DEPLOY_SERVER_IP` is publicly accessible or reachable by GitHub Actions.
- Ensure the `DEPLOY_SSH_KEY` added to GitHub Secrets is valid, properly formatted (including `-----BEGIN OPENSSH PRIVATE KEY-----`), and its corresponding public key is appended to the `~/.ssh/authorized_keys` file of `DEPLOY_SSH_USER` on the remote server.

## Issue: Python Monitoring Script Raises ConnectionError
**Symptoms:** `monitor.py` logs mention "Failed to connect to http://localhost:5000/health. Is the service running?"
**Resolution:**
- Manually run `docker ps` on your server to verify the container is actually running.
- Ensure you bound the ports properly (`-p 5000:5000`) and the Flask app is listening on `0.0.0.0` internally.

## Issue: Monitoring Script is not Sending Emails
**Symptoms:** `monitor.py` logs an error at health check, but no email is received.
**Resolution:**
- Check if the `ALERT_EMAIL` environment variable is defined.
- If using an external SMTP server (e.g., Gmail, AWS SES), make sure `SMTP_HOST` and `SMTP_PORT` environment variables are correct and the server accepts connections without authentication, or modify the script to inject SMTP credentials.
