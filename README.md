# Marketing Funnel & Conversion Performance Analysis

## 📌 Project Overview

This project performs an **end-to-end marketing funnel and conversion analysis** using a real-world banking marketing dataset. The goal is to identify **drop-off points**, evaluate **channel effectiveness**, and generate **actionable insights** that can improve lead-to-customer conversion rates.

This project was completed as part of **Future Interns – Data Science Task 03** and is designed to reflect **industry-level exploratory data analysis (EDA)** and visualization practices.

---

## 🎯 Objectives

* Analyze customer conversion behavior across demographics and channels
* Identify funnel drop-offs based on campaign contact frequency
* Visualize conversion performance using clear, interpretable charts
* Generate summary metrics for business decision-making

---

## 📂 Dataset

**Source:** UCI Machine Learning Repository – Bank Marketing Dataset

**Files Used:**

* `bank-additional-full.csv`

**Key Features:**

* Customer demographics (age, job, education)
* Marketing channel and campaign details
* Contact frequency
* Conversion outcome (`y`: yes/no)

---

## 🛠️ Tech Stack

* **Python 3**
* **Pandas** – data manipulation
* **Matplotlib & Seaborn** – visualization
* **NumPy** – numerical operations

---

## 📁 Project Structure

```
FUTURE_DS_03/
│── bank_marketing/        # Dataset files
│── outputs/               # Generated plots & summary CSV
│── src/
│   └── funnel_analysis.py # Main analysis script
│── requirements.txt
│── README.md
│── LICENSE
```

---

## 📊 Analysis & Visualizations

### 1️⃣ Conversion by Age

Shows how conversion rate varies across different age groups.

📌 **Insight:** Middle-aged customers show higher conversion likelihood.

---

### 2️⃣ Conversion by Channel

Compares conversion rates across marketing contact channels.

📌 **Insight:** Certain channels consistently outperform others.

---

### 3️⃣ Conversion Drop-off by Campaign Contacts

Analyzes how repeated contact attempts affect conversion probability.

📌 **Insight:** Conversion rate drops sharply after excessive follow-ups.

---

## 📈 Outputs Generated

* `conversion_by_age.png`
* `conversion_by_channel.png`
* `dropoff_by_campaign.png`
* `summary_metrics.csv`

All outputs are stored in the **`outputs/`** directory.

---

## 🚀 How to Run the Project

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate environment
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run analysis
python src/funnel_analysis.py
```

---

## 💡 Key Business Takeaways

* Over-contacting customers reduces conversion probability
* Targeted campaigns by age and channel improve efficiency
* Funnel-based analysis enables smarter marketing decisions

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Antony Remane S**
Data Science Intern Aspirant

🔗 GitHub: [https://github.com/Antonyremay](https://github.com/Antonyremay)

---

⭐ *If you find this project useful, consider starring the repository!*
