# ClassActivity1-A

## Continuous Delivery Pipeline

This project follows the path from a feature branch and pull request through
automated checks, merging, versioning, container publishing, staging, and
production approval:

```text
Feature branch -> Pull request -> CI -> Merge to main -> Release tag
-> Build and publish image -> Deploy staging -> Health check
-> Manual approval -> Deploy production
```

Continuous Integration ends after the code has been built and tested. It
answers whether the change is suitable to merge. Continuous Delivery adds
packaging and deployment to a staging environment, leaving the production
release ready for a human to approve. Continuous Deployment goes one step
further by releasing to production automatically after the checks pass.

## Build Once, Deploy Many

Each release creates one immutable Docker image identified by its version.
That same image is promoted from staging to production instead of being
rebuilt separately for each environment. This keeps the tested artifact
identical across environments and makes releases easier to audit and roll
back.

## Environment Setup

The CD workflow uses GitHub-hosted runners to simulate staging and production,
so this classroom version does not require SSH server secrets. The staging
environment runs the published image and checks `/health` before the
production environment becomes available. Configure `production` with a
required reviewer to enforce manual approval. The runner-based containers are
temporary; a real deployment can later replace these steps with SSH secrets
and a persistent server.