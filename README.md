📝 Dockerized Notepad

> A simple full-stack notes application, automatically builds and pushes `latest` and versioned Docker images (`v1.0.0`, etc.) to Docker Hub

---

## Features
-  **FastAPI backend** with SQLite for notes
-  **Vanilla JS frontend** (static HTML + JS)
-  **Docker**: Ready to deploy anywhere
-  **CI/CD with GitHub Actions**: Tags like `v1.0.0` trigger builds + Docker Hub pushes
-  Supports versioned + latest Docker tags
-  Fully open source and self-contained

---

## Quick Start (local Dev)

```bash
git clone https://github.com/bhornpat/dockerized-notepad.git
cd dockerized-notepad

docker compose up --build

---

🐳 Docker hub images
                                                                                     
 Backend  | [bhornpat/dockerized-notepad-backend] 
 Frontend | [bhornpat/dockerized-notepad-frontend]

---

## CI/CD: Versioned Build with Git Tags

git tag v1.0.0
git push origin v1.0.0
