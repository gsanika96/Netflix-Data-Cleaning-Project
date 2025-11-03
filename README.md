# Netflix Data Cleaning Project

## Author
**Sanika Dattatray Gaikwad**  
Diploma in Computer Engineering — *AISSMS Polytechnic, Pune*  
📧 sanikagaikwad@gmail.com | 📍 Pune, Maharashtra

---

## Overview
This project demonstrates **data cleaning and preprocessing** on the Netflix dataset (`netflix_titles.csv`).  
The objective is to remove duplicates, fix missing values, and standardize data for better analysis and visualization.

---

## Before Cleaning
- Raw data contains missing values in the **`director`** and **`cast`** columns.  
- Duplicate records are present in the dataset.  
- The **`date_added`** column has inconsistent date formats.  

---

## After Cleaning
- **Duplicates removed** to ensure unique entries.  
- **Missing values** filled with placeholders such as `Unknown` or `Not Specified`.  
- **Date formats standardized** using Python’s datetime functions for uniformity.  

---

## Files Included
- `netflix_titles.csv` → Original dataset  
- `netflix_titles_cleaned.csv` → Cleaned dataset  
- `before.png` → Screenshot of raw data  
- `after.png` → Screenshot of cleaned data  
- `data_cleaning.py` → Python script used for cleaning and transformation  

---

## How to Run the Project
1. Install **Python** and the required library **Pandas**:
```bash
pip install pandas
```
2. Run the cleaning script:
```bash
python data_cleaning.py
```
3. The cleaned dataset will be saved as `netflix_titles_cleaned.csv` in your project folder.

---

## Learning Outcomes
- Hands-on experience in **data wrangling, handling missing values**, and **standardizing formats**.  
- Improved understanding of **data preprocessing** using **Python (Pandas)**.  
- Practical exposure to preparing data for **analytics and visualization projects**.

---

*Project by **Sanika Dattatray Gaikwad**, AISSMS Polytechnic, Pune.*
