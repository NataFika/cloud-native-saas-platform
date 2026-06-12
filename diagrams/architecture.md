# Architecture Diagram

```text
User
 |
 v
AWS Load Balancer
 |
 v
React Frontend (EKS)
 |
 v
FastAPI Backend (EKS)
 |
 v
PostgreSQL RDS

Supporting Services:
- Terraform provisions infrastructure
- Docker builds application images
- Amazon ECR stores images
- GitHub Actions deploys to EKS
- Prometheus collects metrics
- Grafana visualizes monitoring data