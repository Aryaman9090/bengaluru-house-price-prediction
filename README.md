
# Bengaluru House Price Prediction 🏠

## Overview

This project builds a regression model to predict house prices in Bengaluru using property details such as location, area type, total square feet, bathrooms, balconies, and BHK.

The main goal was to work with messy real-world housing data, clean it properly, understand price-driving factors, and build a reliable prediction pipeline.

**Final Test Performance:**

* R²: 0.72
* MAE: ~22.5 lakhs

On average, the model’s prediction error is about 22 lakhs.

---

## Why This Project?

Housing prices vary significantly across locations and property types. Instead of just training a model, I focused on:

* Handling inconsistent and missing data
* Reducing high-cardinality location noise
* Preventing data leakage using pipelines
* Comparing models before choosing the final one
* Interpreting performance in practical terms

This project was built to reflect how real-world data science workflows actually look.

---

## Dataset

* Source: Kaggle – Bengaluru House Prices dataset
* Target variable: `price` (in lakhs)
* Key features:

  * Location
  * Area Type
  * Availability
  * Total Square Feet
  * Bathrooms
  * Balconies
  * Size (used to extract BHK)

---

## Data Cleaning & Preparation

The dataset contained missing values, inconsistent formats, and many unique location names.

Steps taken:

* Dropped irrelevant column (`society`)
* Filled missing values

  * Median for numeric features
  * Mode for categorical features
* Converted `total_sqft` to numeric
* Standardized text columns (lowercase + trimmed spaces)
* Grouped rare locations into “Other” to reduce sparsity
* Extracted BHK from the `size` column
* Removed extreme price outliers
* Applied log transformation to the target variable to reduce skewness

---

## Exploratory Data Analysis

Before modeling, I explored the dataset to understand patterns and relationships.

### Key Observations

* Price distribution is right-skewed with some very high-end properties
* Larger BHK units generally increase price
* Plot area properties tend to be more expensive
* Ready-to-move homes often show higher average prices
* Total square feet has strong positive correlation with price

---

## Visualizations

**Price Distribution**

<img width="1990" height="490" alt="8a6ab8c8-73a4-46a7-82cc-48986cff2456" src="https://github.com/user-attachments/assets/e3dc74ff-619e-4e6d-8916-23f8481d0bba" />

The distribution is right-skewed, which motivated applying a log transformation.

---

**Average Price by Area Type**

<img width="1643" height="428" alt="7e9533ab-553b-400a-b055-21bda552053d" src="https://github.com/user-attachments/assets/8f5af5e3-e3c5-4e30-93df-56964c2dfe61" />

Plot area properties show noticeably higher average prices.

---

**Average Price by BHK**

<img width="790" height="490" alt="c87d8f04-328f-4463-9709-65da2efe72df" src="https://github.com/user-attachments/assets/c87d8f04-328f-4463-9709-65da2efe72df" />

As expected, price increases with BHK size.

---

**Availability vs Price**

<img width="790" height="489" alt="96dc4416-84fe-4c76-80a8-e6f52b5039d1" src="https://github.com/user-attachments/assets/2d12a135-1145-460a-b638-b8bb7a6b91ac" />

Ready-to-move homes tend to have higher average pricing.

---

**Correlation Heatmap**

<img width="908" height="790" alt="e249f374-83d2-413d-83c3-90840b874ce8" src="https://github.com/user-attachments/assets/7c4b68ce-312a-4c2e-bbaf-8ade082bc5af" />

Total square feet and BHK show strong positive correlation with price.

---

## Modeling Approach

### Train-Test Split

* 80% training
* 20% testing
* Fixed random state for reproducibility

### Pipeline Design

To prevent data leakage and keep preprocessing consistent, I built a full pipeline using:

* ColumnTransformer
* OneHotEncoder (`handle_unknown="ignore"`)
* RandomForestRegressor

This ensures the same transformations are applied during training and future predictions.

---

## Model Comparison

I tested a baseline Linear Regression model first.

Random Forest performed better because:

* It captures non-linear relationships
* It handles mixed data types well
* It is more robust to noise

| Model             | MAE (Lakhs) | R²   |
| ----------------- | ----------- | ---- |
| Linear Regression | —           | —    |
| Random Forest     | 22.5        | 0.72 |

(Hyperparameters were tuned using RandomizedSearchCV with 5-fold cross-validation.)

---

## Model Performance

Test set results:

* MAE: ~22.5 lakhs
* R²: 0.72

MAE was chosen because it is easy to interpret in pricing terms and less sensitive to extreme values than RMSE.

The model performs well for mid-range properties but shows higher error for very high-priced homes.

---

## Model Saving

The final trained pipeline (including preprocessing) was saved using joblib:

ben_house_price_model.pkl

This allows easy reuse for deployment or integration into applications.

---

## Limitations

* Based on historical Kaggle dataset; current market trends may differ
* Unseen locations may reduce prediction accuracy
* High-end luxury homes show higher prediction variance
* Economic indicators and demand trends were not included

---

## Key Takeaways

* Real-world data requires heavy cleaning before modeling
* Handling location sparsity is important for performance
* Log-transforming skewed targets improves model stability
* Cross-validation gives more reliable performance estimates
* Model metrics should be interpreted in business context

---

## Tech Stack

Python, pandas, numpy, matplotlib, seaborn, scikit-learn, plotly, joblib


