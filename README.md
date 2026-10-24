# DevOps Platform

An end-to-end, locally hosted DevOps platform built to practice modern DevOps and GitOps workflows without depending on a cloud account.

## Technology Stack

- Docker: Containerize the application.
- Kubernetes (Kind): Run workloads locally.
- Helm: Package and deploy Kubernetes applications.
- GitHub Actions: Automate continuous integration.
- Argo CD: Implement GitOps-based continuous delivery.
- Prometheus: Collect metrics and monitor services.
- Grafana: Visualize metrics through dashboards.

## Project Goals

- Build and test a containerized application.
- Deploy it to a local Kubernetes cluster.
- Automate code checks and image builds.
- Manage Kubernetes deployments declaratively with Helm.
- Synchronize deployments through Argo CD.
- Monitor application and cluster health with Prometheus and Grafana.

## Environment

- OS: Ubuntu on WSL2
- Container runtime: Docker Desktop
- Local Kubernetes: Kind
- Kubernetes context: kind-devops-platform

## Cloud Dependency

Application workloads and Kubernetes infrastructure run locally. GitHub Actions will provide CI when the repository is pushed to GitHub.
