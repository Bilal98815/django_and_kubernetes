# Django Application with GitHub Actions and Kubernetes

This project is a Django application integrated with GitHub Actions for CI/CD and deployed on Kubernetes. It includes automated linting, testing, and image creation, along with notifications to Sentry and Slack.

## If you like it Give it a Star :)

## Features

- **Linting**: Automatically checks for code linting errors on every push.
- **Testing**: Runs unit tests after successful linting.
- **Docker Image Creation**: Builds Docker images for the Django app, PostgreSQL, and Redis, and pushes them to GitHub Container Registry.
- **Sentry Alerts**: Notifies Sentry about new releases.
- **Slack Notifications**: Sends notifications to a Slack channel based on pipeline success or failure.
- **Kubernetes Deployment**: Pulls images from GitHub Registry and manages deployments.

## Getting Started

### Prerequisites

- Ensure you have a GitHub account and a repository set up.
- Have access to a Kubernetes cluster.
- Set up Sentry and Slack, and obtain the necessary API keys.

### Configuration

1. **Sentry and Slack Integration**:
   - Connect your Sentry account and obtain the DSN for notifications.
   - Configure Slack integration for alerts on pipeline status.
   - Update the GitHub Actions workflow file with your Sentry and Slack credentials.

2. **Kubernetes Configuration**:
   - Create or update the necessary Secrets and ConfigMaps in your Kubernetes cluster:
     - Store sensitive data (like database credentials) in Secrets.
     - Use ConfigMaps for application configuration.

### CI/CD Workflow

On every push to the repository:

1. **Linting**: The workflow checks for linting errors.
2. **Testing**: If linting passes, it runs the tests.
3. **Docker Image Creation**: If tests pass, it builds Docker images for the Django app, PostgreSQL, and Redis, and pushes them to GitHub Container Registry.
4. **Sentry Notification**: Sends a notification to Sentry regarding the new release.
5. **Slack Notifications**: Notifies the specified Slack channel whether the pipeline succeeded or failed.

### Kubernetes Deployment

The Kubernetes configuration includes:

- **Deployments**:
  - Django application
  - Celery Beat (for periodic tasks)
  - Celery Worker (for background tasks)
  - Redis
  - PostgreSQL

- **Persistent Volume and Claim**: Set up for static media files.

- **Services**: Exposes the Django app, PostgreSQL, and Redis deployments.

### Periodic Task

A Celery task runs every 4 minutes to delete data from the database that is older than 4 minutes.

## Usage

1. Clone this repository.
2. Update the GitHub Actions workflow file with your specific Sentry and Slack configurations.
3. Deploy the application to your Kubernetes cluster by applying the provided manifests.

## Acknowledgments

- Django for the web framework.
- GitHub Actions for CI/CD.
- Kubernetes for orchestration.
- Sentry for error tracking.
- Slack for notifications.
