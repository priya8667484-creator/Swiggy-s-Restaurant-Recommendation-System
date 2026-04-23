import re
import numpy as np
import pandas as pd


def clean_text(value):
    if pd.isna(value):
        return np.nan
    value = str(value).strip()
    value = re.sub(r"\s+", " ", value)
    return value


def clean_cost(value):
    """
    Convert cost values like '₹250', '250 for one', '300', etc. to float.
    """
    if pd.isna(value):
        return np.nan
    value = str(value)
    value = re.sub(r"[^\d.]", "", value)
    if value == "":
        return np.nan
    return float(value)


def clean_rating(value):
    """
    Convert ratings to float and coerce invalid values to NaN.
    """
    if pd.isna(value):
        return np.nan
    value = str(value).strip()
    if value in ["--", "NEW", "NaN", "nan", ""]:
        return np.nan
    try:
        return float(value)
    except ValueError:
        return np.nan


def clean_rating_count(value):
    """
    Convert rating_count values like '1.2K+', '500 ratings', etc. to numeric.
    """
    if pd.isna(value):
        return np.nan

    value = str(value).strip().upper().replace(",", "")
    value = value.replace("RATINGS", "").replace("RATING", "").replace("+", "").strip()

    if "K" in value:
        try:
            return float(value.replace("K", "")) * 1000
        except ValueError:
            return np.nan

    numeric = re.sub(r"[^\d.]", "", value)
    if numeric == "":
        return np.nan
    return float(numeric)


def normalize_cuisine(value):
    if pd.isna(value):
        return np.nan
    value = str(value).strip().lower()
    cuisines = [c.strip().title() for c in value.split(",") if c.strip()]
    cuisines = sorted(set(cuisines))
    return ", ".join(cuisines)


def safe_fill_mode(series):
    mode = series.mode()
    if len(mode) > 0:
        return series.fillna(mode[0])
    return series.fillna("Unknown")
