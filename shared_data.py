"""
Shared data loading for Vaigai North Bank Road Project.
Data file selection is stored in st.session_state["selected_data_file"].
"""
import pandas as pd
import streamlit as st
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

# Available data files (CSV) - same column structure
DATA_FILES = [
    ("RCC RW data.csv", "RCC Retaining Wall"),
    ("PCC RW Data.csv", "PCC Retaining Wall"),
    ("boxculvert data.csv", "Box Culvert"),
]

DEFAULT_FILE = "RCC RW data.csv"


def get_available_files():
    """Return list of (filename, label) for files that exist."""
    result = []
    for fname, label in DATA_FILES:
        path = PROJECT_ROOT / fname
        if path.exists():
            result.append((fname, label))
    return result if result else [(DEFAULT_FILE, "RCC Retaining Wall")]


def get_selected_data_file():
    """Get currently selected data file from session state."""
    if "selected_data_file" not in st.session_state:
        available = get_available_files()
        st.session_state["selected_data_file"] = available[0][0]
    return st.session_state["selected_data_file"]


def get_data_path(filename=None):
    """Get full path to data file."""
    if filename is None:
        filename = get_selected_data_file()
    return PROJECT_ROOT / filename


def normalize_columns(df):
    """Normalize column names to standard format."""
    col_map = {
        "Est Length": "Est_Length",
        "Bill No": "Bill_No",
    }
    df = df.rename(columns=col_map)
    return df


@st.cache_data
def load_data(filename):
    """
    Load and normalize data from CSV file (cached by filename).
    Returns DataFrame with columns: Estimate, Est_Length, Bill_No, Item, Height, Stretch, Length, Mbook, Pages, Date
    """
    path = PROJECT_ROOT / filename
    if not path.exists():
        return pd.DataFrame()

    df = pd.read_csv(path)
    df = normalize_columns(df)
    # Ensure standard column names (CSV may have slightly different headers)
    expected = ["Estimate", "Est_Length", "Bill_No", "Item", "Height", "Stretch", "Length", "Mbook", "Pages", "Date"]
    for col in expected:
        if col not in df.columns:
            df[col] = pd.NA

    df = df[df["Estimate"].astype(str).str.strip() != "Estimate"].copy()
    df = df.dropna(how="all")
    df["Length"] = pd.to_numeric(df["Length"], errors="coerce")
    df["Est_Length"] = pd.to_numeric(df["Est_Length"], errors="coerce")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Mbook"] = df["Mbook"].astype(str).str.strip()
    df["Stretch"] = df["Stretch"].astype(str).str.strip()
    return df
