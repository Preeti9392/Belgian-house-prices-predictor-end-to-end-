# 🤖 Machine Learning Model

**Part of:** [Belgian Real Estate Price Predictor](../) | **Status:** ✅ Complete

---

## 🎯 Purpose

Train a CatBoost regression model to predict Belgian property prices with 71% R² accuracy.

---

## 📊 Model Performance

| Metric | Score | Interpretation |
|--------|-------|----------------|
| **R²** | 0.71 | Explains 71% of price variance |
| **MAE** | €12,345 | Average prediction error |
| **MAPE** | 15% | Typical 15% deviation |

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Train model
python main.py
```

**Runtime:** ~5-10 minutes  
**Output:** Trained model saved in `model/`

---

## 🧠 Why CatBoost?

- ✅ Native categorical feature handling
- ✅ Superior to LinearRegression (R² 0.71 vs 0.54)
- ✅ Fast training with early stopping
- ✅ Robust to overfitting

---

## 📈 Feature Importance

1. **Surface Area** (35%)
2. **Locality** (28%)
3. **Province** (18%)
4. **Bedrooms** (9%)
5. **Condition** (6%)

---

➡️ **Next:** Go to `03_deployment/` to deploy the model as API
