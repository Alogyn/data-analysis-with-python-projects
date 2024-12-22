# 📊 Page View Time Series Visualizer

## 🔧 Project Overview
Visualize time series data using:
- 🎨 Line charts
- 📊 Bar charts
- 🔄 Box plots

You will work with Pandas, Matplotlib, and Seaborn to analyze the number of daily page views on the freeCodeCamp.org forum between **2016-05-09** and **2019-12-03**.

---

## 🔍 Objective
Gain insights into user behavior by identifying trends and seasonal patterns in forum visits.

---

## 📊 Data Description
The dataset contains daily page view counts from the freeCodeCamp forum. The cleaning process filters out extreme outliers (top 2.5% and bottom 2.5%).

- **File:** `fcc-forum-pageviews.csv`
- **Columns:**
  - `date` (Index): Date of page views.
  - `value`: Daily page view count.

---

## 🗒 Tasks
1. **Data Import and Cleaning**
   - Import the data using Pandas.
   - Remove top and bottom 2.5% of page views.

2. **Visualizations**
   - **Line Plot**
     - Visualize daily page views over time.
     - Include title, axis labels, and proper formatting.
     
   - **Bar Chart**
     - Display average daily page views per month grouped by year.
     - Add month legends and axis labels.

   - **Box Plots**
     - Show yearly trends and monthly seasonality.
     - Create two side-by-side box plots.

---

## 🎨 Visualizations
### 1. 🔮 Line Chart
**Title:** `Daily freeCodeCamp Forum Page Views 5/2016-12/2019`

### 2. 🌈 Bar Chart
- **X-Axis:** Years
- **Y-Axis:** Average Page Views

### 3. 🔢 Box Plots
- **Year-wise Trend:** Highlights yearly distribution.
- **Month-wise Seasonality:** Focuses on monthly patterns.

---

## 🛠️ Development
### 🗋 Files
- `time_series_visualizer.py`: Main script.
- `main.py`: Testing script.
- `test_module.py`: Unit tests.

### 🎧 Instructions
1. Clone the repository.
   ```bash
   git clone https://github.com/Alogyn/data-analysis-with-python-projects
   cd data-analysis-with-python-projects/boilerplate-page-view-time-series-visualizer
   ```

2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script for development.
   ```bash
   python main.py
   ```

4. Generate visualizations.
   - Ensure the `fcc-forum-pageviews.csv` file is in the working directory.

5. Save and return the charts.

---

## 🔢 Testing
- Use `test_module.py` to verify functionality.
- Run tests with:
   ```bash
   python -m unittest test_module.py
   ```

---

## 🔄 Key Features
- ✅ **Cleaned Time Series Data**: Outliers removed for accurate trends.
- 📊 **Three Types of Visualizations**: Line, Bar, and Box Plots.
- 🏆 **Python Libraries**: Leveraging Pandas, Matplotlib, and Seaborn.

---

## 🔧 Tools Used
- **Languages**: Python
- **Libraries**: Pandas, Matplotlib, Seaborn
- **Environment**: Gitpod Starter Code

---

## 🛠️ Future Improvements
- Add interactivity to the visualizations.
- Expand the analysis to include more metrics.

---

## 🎥 Example Outputs
### Line Plot
![Line Plot](examples/Figure_1.png)

### Bar Chart
![Bar Chart](examples/Figure_2.png)

### Box Plots
![Box Plots](examples/Figure_3.png)

---

## 🌐 License
This project is licensed under the MIT License.
