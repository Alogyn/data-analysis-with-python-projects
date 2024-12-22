# 📊 Mean-Variance-Standard Deviation Calculator

A Python project to calculate various statistical metrics (mean, variance, standard deviation, max, min, and sum) for a 3x3 matrix using **NumPy**. This project is part of the **freeCodeCamp Data Analysis with Python Certification**.

---

## 🚀 Features
- Computes statistical metrics for rows, columns, and the flattened matrix:
  - 📈 Mean
  - 🧮 Variance
  - 📊 Standard Deviation
  - 🔼 Max
  - 🔽 Min
  - ➕ Sum
- 🚨 Input validation to ensure the list contains exactly 9 numbers.

---

## 📂 Project Structure
```
📁 project-root
├── mean_var_std.py      # Core function implementation
├── main.py              # Test and run the function
├── test_module.py       # Unit tests
└── README.md            # Project documentation
```

---

## 🛠️ Technologies Used
- **Python 3** 🐍
- **NumPy** 📦

---

## 🧑‍💻 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Alogyn/data-analysis-with-python-projects
   cd Mean-Variance-Standard-Deviation-Calculator
   ```
2. Install NumPy (if not already installed):
   ```bash
   pip install numpy
   ```
3. Run the project:
   ```bash
   python3 main.py
   ```

---

## ✅ Example Output

Input:
```python
calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

Output:
```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

---

## 🧪 Running Tests
Run the unit tests with:
```bash
python3 main.py
```

Ensure all tests in `test_module.py` pass before submitting the project.

---

## 📝 License
This project is licensed under the MIT License. 📝x
