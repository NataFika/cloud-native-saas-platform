# Cloud Native SaaS Platform

A production-style cloud-native application built on AWS using modern DevOps practices.

## Overview

This project demonstrates a complete cloud-native architecture including:

* React Frontend
* FastAPI Backend
* PostgreSQL RDS Database
* Docker Containers
* Amazon ECR
* Amazon EKS
* Terraform Infrastructure as Code
* GitHub Actions CI/CD
* Prometheus Monitoring
* Grafana Dashboards

---

## Architecture

```text
React Frontend
       |
       v
AWS Load Balancer
       |
       v
FastAPI Backend (EKS)
       |
       v
PostgreSQL RDS
```

Infrastructure is provisioned with Terraform and deployed to AWS EKS using Docker containers.

---

## Technology Stack

### Frontend

* React
* Vite
* Recharts

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL

### Cloud

* AWS EKS
* AWS ECR
* AWS RDS
* VPC
* Load Balancer

### DevOps

* Terraform
* Docker
* Kubernetes
* GitHub Actions
* Prometheus
* Grafana

---

## Features

### Influencer Search

* Search by name
* Search by location
* Search by niche
* Platform filtering
* Ranking and sorting

### Analytics Dashboard

* Total Influencers
* Total Reach
* Average Engagement
* Average Campaign Price
* Top Platform
* Top Niche

### Visualizations

* Followers by Platform
* Average Engagement by Niche
* Campaign Price by Creator

---

## Infrastructure

Terraform provisions:

* VPC
* Public Subnets
* Private Subnets
* NAT Gateway
* Security Groups
* EKS Cluster
* RDS PostgreSQL

---

## Kubernetes

Workloads deployed on Amazon EKS:

* Backend Deployment
* Frontend Deployment
* Services
* Secrets
* Load Balancers

---

## CI/CD

GitHub Actions automatically:

1. Builds Docker images
2. Pushes images to Amazon ECR
3. Deploys updates to Amazon EKS

---

## Monitoring

Monitoring stack includes:

* Prometheus
* Grafana
* Alertmanager
* Node Exporter
* Kubernetes Metrics

---

## Screenshots

Add screenshots of:

* Dashboard
* Grafana Monitoring
* Kubernetes Workloads
* AWS Architecture

---

## Architecture Diagram

See: [Architecture Diagram](diagrams/architecture.md)
---

## Author

Natalia Finkovskaya

GitHub: https://github.com/NataFika

LinkedIn: https://www.linkedin.com/in/natalia-finkovskaya-2b3748335
