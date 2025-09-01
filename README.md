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
- Flask app + core routes → **Application Development**
- Git initialized & GitHub-ready structure → **VCS Implementation**
- `tests/test_app.py` with Pytest → **Unit Testing**
- `pytest -q` locally and in CI → **Automated Testing**
- Dockerfile + container run → **Containerization**
- `.github/workflows/ci.yml` → **CI/CD pipeline (build + test on push)**
```

