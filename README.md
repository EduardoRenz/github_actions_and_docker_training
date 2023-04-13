## Github Actions Workflow and Amazon EC2 Deployment for a Python Flask Application
This application is a study on how to create a workflow using Github Actions and deploy a Python Flask application to Amazon EC2.

### Requirements
To use this workflow, you need the following:

- An Amazon Web Services (AWS) account
- An EC2 instance running Ubuntu Server 18.04 LTS or later
- SSH access to the EC2 instance
- Python 3 installed on the EC2 instance
- Flask and other dependencies installed on the EC2 instance
- Docker installed on the EC2 instance

### Workflow
The workflow is defined in the .github/workflows/main.yml file. It consists of the following steps:

- Checkout: This step checks out the source code from the repository.
- Setup Python: This step sets up Python on the runner machine.
- Install dependencies: This step installs the dependencies required for the application.
- Test with pytest: This step runs the unit tests for the application.
- Build Docker Image: This step builds a Docker image for the application.
- Push Docker Image to Docker Hub: This step pushes the Docker image to Docker Hub.
- Deploy to EC2: This step uses SSH to connect to the EC2 instance, pull the Docker image, and run the application.
