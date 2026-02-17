# RUNBOOK - Milestone 2

## Dependency pinning strategy
Dependencies are pinned in requirements.txt.

## Image optimization
Multi-stage builds reduce image size.

## Security considerations
Slim images reduce attack surface.

## CI/CD workflow
GitHub Actions runs tests → builds → pushes image.

## Versioning strategy
Semantic versioning vX.Y.Z used.

## Troubleshooting
Check Docker login & GitHub Secrets if push fails.
