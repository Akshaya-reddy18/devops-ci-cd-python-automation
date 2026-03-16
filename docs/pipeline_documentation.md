# CI/CD Pipeline Documentation

The CI/CD pipeline for this project is implemented using GitHub Actions. The pipeline consists of three main stages defined in `.github/workflows/ci-cd.yml`:

## 1. Build & Test (`build-and-test`)

This job triggers on every `push` and `pull_request` to the `main` branch.
- **Environment:** `ubuntu-latest`
- **Steps:**
  - Check out the source code.
  - Set up Python 3.11 with `pip` caching enabled.
  - Install standard project dependencies inside the GitHub Actions runner.
  - Run the `pytest` test suite to validate the Flask API functionality.

## 2. Docker Build & Push (`docker-build-push`)

This job triggers only on a `push` to the `main` branch, ensuring that PRs do not overwrite production artifacts. This job requires `build-and-test` to succeed first.
- **Steps:**
  - Login to Docker Hub using the `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets.
  - Build the Dockerfile present in the project root.
  - Push the generated image to Docker Hub with tags: `latest` and the unique `github.sha`.

## 3. Deploy to Production (`deploy`)

Also triggers on a `push` to `main`, and depends on the successful completion of `docker-build-push`.
- **Environment Context:** Linux-based execution using SSH to access the deployment server.
- **Steps:**
  - Configure the SSH key from GitHub secrets.
  - Log into the remote Linux instance.
  - Pull the latest `devops-python-api:latest` Docker image.
  - Restart the Docker container on the host server safely without interrupting unrelated services.
