![CI](https://github.com/aashishkumargaur/aceest-fitness-devops/actions/workflows/ci.yml/badge.svg?branch=main)


# ACEest Fitness & Gym — DevOps Assignment Starter

A minimal Flask application for a fictional gym/fitness startup with unit tests, Docker containerization, and a GitHub Actions CI pipeline.

## 🧰 Tech Stack
- **Python 3.11**, **Flask**
- **Pytest** for unit tests
- **Docker** for containerization
- **GitHub Actions** for CI (build + test on every push)

## 🚀 Quick Start (Local)

1. Create & activate a virtualenv (optional but recommended).
2. Install deps:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   # or with gunicorn
   gunicorn -b 0.0.0.0:8000 "app:create_app()"
   ```
4. Visit: `http://localhost:8000`

## ✅ Run Tests (Local)
```bash
pytest -q
```

## 🐳 Docker (Local)
Build the image:
```bash
docker build -t aceest-fitness:latest .
```
Run the API:
```bash
docker run --rm -p 8000:8000 aceest-fitness:latest
```
Run tests *inside* the container:
```bash
docker run --rm aceest-fitness:latest pytest -q
```

## 🔁 CI/CD (GitHub Actions)
This repo includes a workflow at `.github/workflows/ci.yml` that triggers on every push and PR to:
1. Set up Python and install dependencies  
2. Run unit tests on the host  
3. Build the Docker image  
4. Run the same unit tests **inside the built Docker image**

## 📦 Project Structure
```
.
├── app.py
├── requirements.txt
├── pytest.ini
├── tests
│   └── test_app.py
├── Dockerfile
├── .github
│   └── workflows
│       └── ci.yml
└── README.md
```

## ✍️ Notes
- Endpoints:
  - `GET /` → health
  - `GET /classes` → list available classes
  - `POST /members` (JSON: `{ "member_id": "...", "name": "..." }`) → add member
  - `GET /members/<member_id>` → fetch a member

## 📚 Assignment Mapping

- **Application Development (Flask app)**
  - `app.py` exposes:
    - `GET /` → health check
    - `POST /workouts` → add a workout `{ "workout": "Yoga", "duration": 30 }`
    - `GET /workouts` → list workouts

- **Version Control (Git & GitHub)**
  - Public repo with meaningful commits on `main`.

- **Unit Testing (Pytest)**
  - `tests/test_app.py` validates:
    - health endpoint
    - add + list workouts flow
    - invalid input handling
  - `pytest.ini` sets test discovery and options.

- **Automated Testing Configuration**
  - Tests run locally via `pytest -q` and automatically in CI.

- **Containerization (Docker)**
  - `Dockerfile` builds a Python 3.11 slim image and runs the app with Gunicorn on port 8000.

- **CI/CD (GitHub Actions)**
  - `.github/workflows/ci.yml` triggers on every push/PR to:
    1. Install dependencies
    2. Run Pytest on the host
    3. Build the Docker image
    4. Run Pytest **inside** the Docker container

- **Documentation**
  - `README.md` explains local setup, testing, Docker usage, and CI/CD behavior.


