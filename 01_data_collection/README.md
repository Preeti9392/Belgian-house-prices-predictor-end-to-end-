# 📥 Data Collection Module

**Part of:** [Belgian Real Estate Price Predictor](../) | **Status:** ✅ Complete

---

## 🎯 Purpose

Automated web scraper that collects Belgian property listings from Immoweb.be, extracting structured data for machine learning analysis.

---

## ✨ Key Features

- **Multi-threaded Scraping:** 5 concurrent workers for 5x faster data collection
- **Robust Error Handling:** Automatic retries and graceful failure recovery  
- **Rate Limiting:** Respects robots.txt and implements delays
- **Data Validation:** Ensures data quality before saving
- **Progress Tracking:** Real-time console updates

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run scraper
python main.py
```

**Expected Runtime:** ~20-30 minutes for 10,000 properties

---

## 📊 Output

**Dataset:** 10,247 properties with 13 features  
**File:** `data/dataset_file.csv`

---

➡️ **Next:** Go to `02_modeling/` to train the ML model
