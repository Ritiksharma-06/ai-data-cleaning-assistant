# AI-Powered Data Cleaning Assistant

An intelligent data cleaning system built using Python and Streamlit that automatically detects and resolves common data quality issues such as missing values, outliers, duplicates, and incorrect data types.


---

## ✨ Features

- ✅ Missing value detection and imputation  
- ✅ Intelligent outlier detection using percentile capping  
- ✅ Duplicate record removal  
- ✅ Automatic data type correction  
- ✅ Validation report with statistical improvement metrics  
- ✅ Interactive Streamlit UI  
- ✅ Download cleaned dataset  
- ✅ Modular and scalable architecture 

---

## 🏗️ System Architecture

!<img src="screenshots/architecture.png" width="800">

---

## 📁 Project Structure
```
ai-data-cleaning-assistant/
├── app.py
├── requirements.txt
├── README.md
├── src/
│ ├── cleaning_pipeline.py
│ ├── data_loader.py
│ ├── missing_handler.py
│ ├── outlier_handler.py
│ ├── duplicate_handler.py
│ ├── datatype_handler.py
│ └── report_generator.py
├── data/
│ ├── raw/
│ └── cleaned/
├── reports/
├── screenshots/
└── venv/
```



---

## Architecture Overview

The project follows a modular pipeline architecture:

- Streamlit UI → User uploads dataset  
- Cleaning Pipeline → Executes cleaning workflow  
- Missing Handler → Fixes missing values  
- Outlier Handler → Detects and corrects outliers  
- Duplicate Handler → Removes duplicate records  
- DataType Handler → Corrects data types  
- Validation Module → Validates cleaning quality  
- Report Generator → Generates validation report  

## Installation

### Step 1: Clone repository


### Step 2: Navigate to folder
cd ai-data-cleaning-assistant

### Step 3: Install dependencies
pip install -r requirements.txt


---

## Run Application
streamlit run app.py


---

🧪 Usage

1. Upload CSV or Excel dataset
2. Click "Run AI Cleaning"
3. View cleaning summary and validation report
4. Download cleaned dataset

---

---
🔬 Data Cleaning Techniques Used
Missing Value Handling

Numeric → Median imputation

Categorical → Mode imputation

Outlier Detection

Percentile capping (1st and 99th percentile)

Skew-aware detection

Duplicate Detection

Automatic duplicate removal

Data Type Correction

Automatic numeric and categorical type correction

Validation Intelligence

Standard deviation comparison

Variance reduction analysis

---

📊 Results Example

| Metric | Before | After | Improvement |
|------|--------|--------|-------------|
| Price STD | 367127 | 317438 | 13.53% reduction |
| Missing Values | 2 | 0 | 100% fixed |

---

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Streamlit
- VS Code
- GitHub

---

## Enterprise Use Cases

- Machine learning preprocessing
- Data engineering pipelines
- AIOps log preprocessing
- Business analytics

---

## Application Screenshots


### 1. Upload Dataset Screen
<img src="screenshots/1.png" width="800">

### 2. Raw Dataset Preview
<img src="screenshots/2.png" width="800">

### 3. Cleaned Dataset Preview
<img src="screenshots/3.png" width="800">

### 4. Cleaning Summary
<img src="screenshots/4.png" width="800">

### 5. Validation Report
<img src="screenshots/5.png" width="800">

### 6. Detailed report
<img src="screenshots/6.png" width="800">

👨‍💻 Author

**Ritik Sharma**  
**Software Engineer**  


---

## GitHub Repository

https://github.com/Ritiksharma-06/ai-data-cleaning-assistant
