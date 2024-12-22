# 🩺 Medical Data Visualizer

Visualize and analyze medical examination data using Python libraries like Matplotlib, Seaborn, and Pandas. Gain insights into the relationships between cardiac disease, body measurements, blood markers, and lifestyle choices.

---

## 📋 Features

- Import and preprocess medical data.
- Add and normalize features such as overweight, cholesterol, and glucose.
- Create:
  - **Categorical Plots**: Compare good vs. bad outcomes for various health features.
  - **Heatmaps**: Correlation matrix for in-depth data relationships.
- Clean the dataset by removing incorrect or outlier data.
- Perform analysis and generate visualizations programmatically.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Alogyn/data-analysis-with-python-projects.git
   cd data-analysis-with-python-projects/medical-data-visualizer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠 Usage

1. Place the dataset (`medical_examination.csv`) in the project directory.
2. Write your implementation in `medical_data_visualizer.py`.
3. Test your code using `main.py`:
   ```bash
   python main.py
   ```
4. Run unit tests to validate functionality:
   ```bash
   python test_module.py
   ```

---

## 📂 Dataset Description

| Feature                       | Type                | Values                        |
|-------------------------------|---------------------|-------------------------------|
| **Age**                       | Objective Feature   | `int` (days)                 |
| **Height**                    | Objective Feature   | `int` (cm)                   |
| **Weight**                    | Objective Feature   | `float` (kg)                 |
| **Gender**                    | Objective Feature   | Categorical code             |
| **Systolic Blood Pressure**   | Examination Feature | `int`                        |
| **Diastolic Blood Pressure**  | Examination Feature | `int`                        |
| **Cholesterol**               | Examination Feature | `1: normal`, `2: above normal`, `3: well above normal` |
| **Glucose**                   | Examination Feature | `1: normal`, `2: above normal`, `3: well above normal` |
| **Smoking**                   | Subjective Feature  | Binary                       |
| **Alcohol Intake**            | Subjective Feature  | Binary                       |
| **Physical Activity**         | Subjective Feature  | Binary                       |
| **Cardiovascular Disease**    | Target Variable     | Binary                       |

---

## 🏆 Tasks Breakdown

1. **Preprocessing:**
   - Add an `overweight` column using BMI.
   - Normalize `cholesterol` and `glucose` columns.

2. **Categorical Plot:**
   - Visualize counts for features like `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `overweight`.

3. **Heatmap:**
   - Clean data to remove outliers and inconsistencies.
   - Plot correlations between variables.

---

## ✨ Example Visualizations

### Categorical Plot

Compare feature distributions for patients with and without cardiovascular disease.

### Heatmap

Identify correlations between variables like blood pressure, cholesterol, and BMI.

---

## 🛡 License

This project is licensed under the MIT License.

---

## 💬 Acknowledgments

- **Dataset**: Medical Examination Data
- **Resources**: freeCodeCamp.org Python and Pandas courses

---

## 📈 GitHub Stats

![Repo Stats](https://github-readme-stats.vercel.app/api?username=Alogyn&show_icons=true&theme=radical)
