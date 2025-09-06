# URL Shortener (FastAPI + DynamoDB)

A minimal, free‑tier‑friendly URL shortener:
- FastAPI + Uvicorn
- AWS DynamoDB for storage
- Dockerized for easy deploy on EC2
- Optional GitHub Actions deploy workflow

## Quick Start (local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export BASE_URL=http://localhost:8000 DDB_TABLE=urls
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
