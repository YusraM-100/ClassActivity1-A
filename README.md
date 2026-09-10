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