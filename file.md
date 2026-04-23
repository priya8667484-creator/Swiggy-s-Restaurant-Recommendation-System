# Swiggy's Restaurant Recommendation System using Streamlit

## Overview
This project recommends restaurants based on user preferences such as city, cuisine, minimum rating, and maximum cost. It also supports restaurant-to-restaurant similarity recommendations.

## Features
- Data cleaning and preprocessing
- One-Hot Encoding for categorical variables
- Standard scaling for numeric features
- Cosine similarity-based recommendation engine
- Streamlit web application
- Cleaned and encoded data export
- Saved encoder, scaler, and similarity artifacts

## Dataset Columns
- id
- name
- city
- rating
- rating_count
- cost
- cuisine
- lic_no
- link
- address
- menu

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Setup

### 1. Clone project
```bash
git clone <your_repo_url>
cd swiggy_recommendation_system
