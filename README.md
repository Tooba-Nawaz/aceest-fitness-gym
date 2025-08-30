# ACEest Fitness & Gym – Flask + Docker + CI/CD (GitHub Actions)

This repository contains a minimal Flask web application that models the basic idea of logging workouts, together with
unit tests (Pytest), a Dockerfile, and a GitHub Actions workflow that builds the image and runs the tests on every push.

## 1) Run locally

### Prerequisites

- **Python 3.10+** (Windows users: prefer the `py` launcher)
- **Git**
- **Docker Desktop**

### Create and activate a virtual environment (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

### Start the app

```powershell
py app.py
```

Visit http://localhost:5000 and you should see:
`🏋️ ACEest Fitness and Gym
Welcome to ACEest Fitness – your ultimate companion for tracking and improving workouts. Whether you’re a beginner or a professional athlete, our platform helps you stay consistent and motivated.`

## 2) Run tests locally

```powershell
python -m pytest -v
```

## 3) Docker (build and run locally)

Make sure **Docker Desktop** is running.

```powershell
docker build -t aceest-fitness-app .
docker run -p 5000:5000 fitness-app
```

Then open http://localhost:5000

## 4) CI/CD with GitHub Actions

The workflow file lives at `.github/workflows/ci.yml`. On **every push**:

1. Builds the Docker image.
2. Runs **pytest** _inside_ the built container.

You can see the results under the **Actions** tab in your GitHub repository.

## 5) Project structure

```
.
├─ app.py                  # Flask app with simple workout API
├─ requirements.txt        # Python dependencies (includes pytest so tests run in CI)
├─ pytest.ini              # Pytest configuration
├─ tests/
│  └─ test_app.py          # Unit tests
├─ Dockerfile              # Container image definition
├─ .dockerignore           # Excludes files from the Docker build context
└─ .github/
   └─ workflows/
      └─ ci.yml            # GitHub Actions workflow
```

## 6) API quick peek

- `GET /` – homepage message
- `GET /api/workouts` – list all logged workouts (in-memory)
- `POST /api/workouts` – add a workout JSON body using Postman: `{ "workout": "Running", "duration": 30 }`

```

```
