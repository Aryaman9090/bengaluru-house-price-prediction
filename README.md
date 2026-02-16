# Bengaluru House Price Prediction 🏠

## Overview
This project predicts house prices in Bengaluru using machine learning.  
It covers:
- Cleaning and preparing the data  
- Exploring the data with charts  
- Creating new features (like BHK)  
- Training a Random Forest model  
- Tuning the model for better accuracy  
- Saving the final model for reuse  

---

## Dataset
- **Source:** Bengaluru House Prices dataset (from Kaggle).  
- **Features:** Location, area type, availability, total square feet, bathrooms, balconies, and BHK.  
- **Target:** House price (in lakhs).  

---

## Steps
1. **Data Cleaning**  
   - Filled missing values.  
   - Converted `total_sqft` to numbers.  
   - Simplified categories like location and availability.  
   - Removed rare values and extreme outliers.  

2. **Exploratory Data Analysis (EDA)**  
   - Price distribution plots.  
   - Correlation heatmap.  
   - Average price comparisons by availability, area type, and BHK.  

<img width="1990" height="490" alt="8a6ab8c8-73a4-46a7-82cc-48986cff2456" src="https://github.com/user-attachments/assets/e3dc74ff-619e-4e6d-8916-23f8481d0bba" />

<img width="1643" height="428" alt="7e9533ab-553b-400a-b055-21bda552053d" src="https://github.com/user-attachments/assets/8f5af5e3-e3c5-4e30-93df-56964c2dfe61" />
<img width="790" height="490" alt="c87d8f04-328f-4463-9709-65da2efe72df" src="https://github.com/user-attachments/assets/d1178f96-b283-4191-a5df-6a93a780b17e" />

<img width="790" height="489" alt="96dc4416-84fe-4c76-80a8-e6f52b5039d1" src="https://github.com/user-attachments/assets/2d12a135-1145-460a-b638-b8bb7a6b91ac" />
<img width="908" height="790" alt="e249f374-83d2-413d-83c3-90840b874ce8" src="https://github.com/user-attachments/assets/7c4b68ce-312a-4c2e-bbaf-8ade082bc5af" />


3. **Feature Engineering**  
   - Extracted BHK from `size`.  
   - One‑Hot Encoding for categorical columns.  

4. **Modeling**  
   - Random Forest Regressor inside a pipeline.  
   - Hyperparameter tuning with `RandomizedSearchCV`.  

5. **Evaluation**  
   - **MAE:** 22.53  
   - **R²:** 0.72  

6. **Model Saving**  
   - Final model saved as `ben_house_price_model.pkl`.  

---

## Results
- The model explains about 72% of the variation in house prices.  
- Average prediction error is ~22.5 lakhs.  
- **Insights:**  
  - Ready‑to‑move properties are the most expensive.  
  - Plot area properties have the highest average prices.  
  - Bigger BHKs cost more, while small units like 1 RK are cheapest.  
  - Price distribution is skewed, with most homes in lower ranges and a few very expensive ones.  

---

## Tech Stack
- Python (pandas, numpy, matplotlib, seaborn, scikit‑learn, plotly)  
- Random Forest Regressor  
- Jupyter Notebook, joblib  

---

## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/bengaluru-house-price-prediction.git
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:
   ```bash
   jupyter notebook bengaluru_house_price_prediction.ipynb
   ```
4. Load the model:
   ```python
   import joblib
   model = joblib.load("ben_house_price_model.pkl")
   ```

---

## Next Steps
- Add a Streamlit dashboard for predictions.  
- Try other models like Gradient Boosting or Linear Regression.  
- Deploy the model as a web app.  

---

👉 **Repo name:** `bengaluru-house-price-prediction`  
👉 **Description:** *“Machine learning project to predict Bengaluru house prices with data cleaning, EDA, Random Forest, and model saving.”*



