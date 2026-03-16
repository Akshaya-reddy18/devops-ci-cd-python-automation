# Python DevOps CI/CD Automation Project

This project demonstrates a complete CI/CD pipeline using GitHub Actions for a Python Flask application. It includes containerization with Docker, automated testing, and a separate API health monitoring script.

## Project Structure

- `app/`: Source code for the Flask application and its unit tests.
- `scripts/`: Python scripts for API health monitoring.
- `.github/workflows/`: GitHub Actions pipeline configuration.
- `docs/`: Additional documentation including runbooks and troubleshooting guides.
- `Dockerfile`: Instructions to build the Docker image for the Flask app.

## Getting Started

### Local Development

1. **Install App Requirements:**
   ```bash
   pip install -r app/requirements.txt
   ```
2. **Run the Application:**
   ```bash
   python app/main.py
   ```
3. **Run Tests:**
   ```bash
   pytest app/tests/
   ```

### Docker

Build and run the container locally:

```bash
docker build -t devops-python-api .
docker run -p 5000:5000 devops-python-api
```

### Monitoring Script

To run the API health monitoring script:

```bash
pip install -r scripts/requirements.txt
python scripts/monitor.py
```
*Note: You can configure the monitor using environment variables like `MONITOR_API_URL` and `ALERT_EMAIL`.*

## Documentation

- [Deployment Runbook](docs/deployment_runbook.md)
- [Pipeline Documentation](docs/pipeline_documentation.md)
- [Troubleshooting Guide](docs/troubleshooting_guide.md)
