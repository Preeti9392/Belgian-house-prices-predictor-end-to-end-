# 🚀 Deployment & APIs

**Part of:** [Belgian Real Estate Price Predictor](../) | **Status:** ✅ Live in Production

---

## 🌐 Live Demos

- **Streamlit App:** https://immoelizahousepriceprediction.streamlit.app/
- **FastAPI Docs:** https://immoelizaprediction-latest.onrender.com/docs

---

## 🎯 Two Production Interfaces

### 1. Streamlit Web App
User-friendly interface for non-technical users
- Interactive form
- Instant predictions
- Visual results

### 2. FastAPI REST API
For developers and integrations
- RESTful endpoints
- JSON request/response
- Auto-generated docs

---

## 💻 Run Locally

### Streamlit App
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### FastAPI
```bash
pip install -r requirements.txt
uvicorn app:app --reload
# Visit: http://localhost:8000/docs
```

---

## 📡 API Usage Example

```bash
curl -X POST "https://immoelizaprediction-latest.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "bedroomCount": 3,
    "habitableSurface": 120,
    "locality": "Brussels",
    "type": "APARTMENT",
    "buildingCondition": "GOOD"
  }'
```

**Response:**
```json
{
  "predicted_price": 385000,
  "currency": "EUR"
}
```

---

## 🐳 Docker Deployment

```bash
docker build -t belgian-property-predictor .
docker run -p 8000:8000 belgian-property-predictor
```

---

## 🛠️ Tech Stack

- **FastAPI** - Modern Python API framework
- **Streamlit** - Interactive web apps
- **Docker** - Containerization
- **Render.com** - Cloud hosting

---

✅ **Production Ready:** Error handling, logging, optimization included
