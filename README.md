# Milestone 2 – Containerization & CI/CD Pipeline

## Overview

This milestone demonstrates containerization of the application and implementation of an automated CI/CD pipeline using GitHub Actions and Docker Hub.

The pipeline performs:

• Dependency installation  
• Test execution using pytest  
• Docker image build  
• Docker image push to Docker Hub  

---

## Workflow Configuration

The CI/CD pipeline is defined in:

.github/workflows/build.yml

---

## Docker Image

Docker Hub Repository:

https://hub.docker.com/r/sahithigundapaneni/milestone2

Example Image:

sahithigundapaneni/milestone2:v0.1.13

---

## Pull & Run Instructions

To pull the image:

docker pull sahithigundapaneni/milestone2:v0.1.13

To run the container:

docker run --rm sahithigundapaneni/milestone2:v0.1.13

---

## CI/CD Behaviour

The GitHub Actions workflow automatically triggers on tagged commits.

Pipeline stages:

1. Test Stage  
   - Installs dependencies  
   - Runs pytest  

2. Build & Push Stage  
   - Builds Docker image  
   - Pushes image to Docker Hub  

---

## Verification Evidence

• Successful GitHub Actions pipeline run  
• Docker image available in Docker Hub  
• Image pull & execution supported  

---

## Conclusion

The application is fully containerized and integrated with an automated CI/CD pipeline.  
Every tagged release produces a validated Docker image stored in Docker Hub.
