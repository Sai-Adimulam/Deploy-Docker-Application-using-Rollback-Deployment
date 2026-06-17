# Deploy-Docker-Application-using-Rolling-Deployment

# Deploy Docker Application to AWS ECS Using Jenkins (Rolling Deployment)

## Project Flow

### Step 1: Create Application Files

Create the following files:

* app.py
* Dockerfile
* Jenkinsfile
* requirements.txt

### Step 2: Create AWS Resources Manually

Create the following AWS resources:

1. ECR Repository
2. ECS Cluster
3. Task Definition
4. Target Group
5. Application Load Balancer (ALB)

### Step 3: Create ECS Service

Create an ECS Service using the Task Definition.

Initially, the service may not start successfully if the Docker image has not yet been pushed to ECR.

### Step 4: Update Jenkins Pipeline

Update the Jenkinsfile with:

* AWS Region
* ECR Repository Name
* ECS Cluster Name
* ECS Service Name

### Step 5: Push Code to GitHub

Push all project files to the GitHub repository.

### Step 6: Create Jenkins Pipeline Job

1. Open Jenkins.
2. Create a Pipeline Job.
3. Configure GitHub Repository URL.
4. Save and Build.

### Step 7: First Deployment

Jenkins Pipeline performs the following actions:

1. Pulls source code from GitHub.
2. Builds Docker Image.
3. Tags Docker Image.
4. Pushes Docker Image to ECR.
5. Updates ECS Service.
6. ECS pulls the image from ECR.
7. Application becomes available through the ALB DNS URL.

### Step 8: Access Application

Copy the ALB DNS URL and access the application from a browser.

Example:

http://your-alb-dns-name

---

# Rolling Deployment Process

### Step 9: Modify Application

Make changes in app.py.

Example:

* Change application version.
* Update HTML content.
* Add new features.

### Step 10: Push Changes to GitHub

Commit and push the updated code.

### Step 11: Jenkins Builds New Version

Jenkins automatically:

1. Builds a new Docker Image.
2. Tags the image with a new version.
3. Pushes the image to the existing ECR Repository.

### Step 12: Create New Task Definition Revision

Register a new ECS Task Definition revision using the latest image.

Example:

* Revision 1 → Version 1
* Revision 2 → Version 2
* Revision 3 → Version 3

### Step 13: Update ECS Service

Update the ECS Service to use the latest Task Definition revision.

### Step 14: ECS Rolling Deployment

ECS performs a Rolling Deployment:

1. Starts new tasks with the latest image.
2. ALB performs health checks.
3. Traffic is routed to healthy new tasks.
4. Old tasks are gradually stopped.
5. No downtime occurs during deployment.

### Step 15: Verify Deployment

Open the ALB DNS URL and verify that the latest application version is running.

## Technologies Used

* GitHub
* Jenkins
* Docker
* Amazon ECR
* Amazon ECS
* Application Load Balancer (ALB)
* AWS IAM

## Outcome

This project demonstrates a complete CI/CD pipeline using Jenkins, Docker, Amazon ECR, Amazon ECS, and ALB. Any code change pushed to GitHub automatically triggers a rolling deployment with minimal or no downtime.


## Version-1 

from flask import Flask
import os
import socket

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v1")
HOSTNAME = socket.gethostname()

@app.route("/")
def home():
    return {
        "message": "Hello from Docker!",
        "version": VERSION,
        "hostname": HOSTNAME
    }

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

## Version 2

from flask import Flask
import os
import socket

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v2")
HOSTNAME = socket.gethostname()

@app.route("/")
def home():
   return {
     "message": "Welcome to Version 2 Deployment!",
     "version": VERSION,
     "hostname": HOSTNAME,
     "status": "Application Updated Successfully"
    }

@app.route("/health")
def health():
   return {
   "status": "healthy",
   "version": VERSION
   }, 200

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)
