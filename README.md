# EKS GitOps Platform Apps

FastAPI application and Kubernetes manifests for deployment to Amazon EKS through GitOps.

## Overview

This repository contains a sample FastAPI service, container build configuration, GitHub Actions workflows, and Kubernetes manifests used by Argo CD to deploy the application into the EKS platform.

## Goals

- Build and ship a modern Python API workload
- Deploy the application through GitOps
- Showcase clean application delivery practices for portfolio use

## Planned Stack

- FastAPI
- Docker
- GitHub Actions
- Kubernetes manifests with Kustomize
- Argo CD

## Repository Structure

```text
app/                FastAPI source code, requirements, Dockerfile, and tests
k8s/base/           Base Kubernetes manifests shared across environments
k8s/overlays/dev/   Development-specific Kustomize overlay
.github/workflows/  CI workflows
```

## Roadmap

- [x] Bootstrap repository structure
- [ ] Add FastAPI health endpoint
- [ ] Add Docker image build
- [ ] Add unit tests
- [ ] Add GitHub Actions CI workflow
- [ ] Add Kubernetes base manifests
- [ ] Add development overlay
- [ ] Deploy through Argo CD

## Related Repository

Infrastructure repository: [eks-gitops-platform-infra](https://github.com/Anandprakashh/eks-gitops-platform-infra)
