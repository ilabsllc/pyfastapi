# 🐍 FastAPI Microservice – Containerized and Ready for Cloud

This repo contains a minimal FastAPI app packaged as a Docker container and ready to deploy to any container platform (Cloud Run, GKE, AKS, etc.).

---

## 🛠️ Development Setup

### 1. Clone the Repository

```bash
git clone git@github.com:your-org/your-repo-name.git
cd your-repo-name
```

_Use HTTPS if you prefer: `git clone https://github.com/your-org/your-repo-name.git`_

---

### 2. Checkout to `dev` Branch

```bash
git checkout dev
```

---

### 3. Create a Python Virtual Environment

```bash
python3 -m venv .venv
```

---

### 4. Activate the Virtual Environment

- **Fish shell**:
  ```bash
  source .venv/bin/activate.fish
  ```

- **Bash/Zsh**:
  ```bash
  source .venv/bin/activate
  ```

---

### 5. Add `main.py`

Create a file called `main.py` and add the following:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AddRequest(BaseModel):
    a: float
    b: float

@app.get("/healthz")
def liveness():
    return {"status": "alive"}

@app.get("/readiness")
def readiness():
    return {"status": "ready"}

@app.post("/add")
def add(req: AddRequest):
    return {"result": req.a + req.b}
```

---

### 6. Install FastAPI and Dependencies

```bash
pip install "fastapi[standard]"
```

---

### 7. Run Locally with Dev Server

```bash
fastapi dev main.py
```

Then open:

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) – Swagger UI
- [http://127.0.0.1:8000/healthz](http://127.0.0.1:8000/healthz) – Liveness probe

---

## 🐳 Dockerization

### 8. Add a `Dockerfile`

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

---

### 9. Add `requirements.txt`

```
fastapi[standard]
```

---

### 10. Build the Docker Image

```bash
docker build -t ilabsllc/pyfastapi:latest .
```

---

### 11. Run the Container Locally

```bash
docker run -p 8080:8080 ilabsllc/pyfastapi:latest
```

Open [http://localhost:8080/docs](http://localhost:8080/docs) to test again.

---

## ☁️ Push to Docker Hub

### 12. Push the Image

```bash
docker push ilabsllc/pyfastapi:latest
```

> Make sure you’ve logged in first using `docker login`.

---

## ✅ Summary

| Step | Description                            |
|------|----------------------------------------|
| `main.py`       | FastAPI app with health + add route |
| `Dockerfile`    | Builds Python-based container |
| `requirements.txt` | Declares FastAPI deps         |
| `docker push`   | Publishes image to Docker Hub  |

---

## 🧩 Next Steps

- ✅ Deploy to **Google Cloud Run** or **GKE**
- ✅ Add GitHub Actions for CI/CD
- ✅ Add tests with `pytest` + `httpx`

---

## 📎 References

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Docker Hub](https://hub.docker.com/)
- [Google Cloud Run Docs](https://cloud.google.com/run/docs)

