<div align="center">

# 📊 Functional Treat

### A Python CLI data analyzer and transformer — sort, filter, summarize, and compute with built-in functions

![Python](https://img.shields.io/badge/Python-3.10%2B-14b8a6?style=flat&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen?style=flat)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat)
![Level](https://img.shields.io/badge/Level-Intermediate-yellow?style=flat)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat)

</div>

---

## 📖 About

**Functional Treat** is an interactive Python CLI tool for analyzing and transforming a 1D integer dataset. You input space-separated numbers, then apply a rich set of operations — compute statistics, calculate factorials recursively, filter values with a `lambda`, sort ascending or descending, and view a full statistical summary. It demonstrates Python's functional programming tools alongside recursion, higher-order functions, and the `match/case` dispatch pattern.

---

## 🗂️ Menu Options

| Option | Action | Description |
|--------|--------|-------------|
| `1` | Input data | Enter space-separated integers — parsed and appended to the global dataset |
| `2` | Display data summary | Shows count, min, max, sum, and average using Python built-ins |
| `3` | Calculate factorial | Computes n! via a recursive function defined inside the case block |
| `4` | Filter by threshold | Returns values above a threshold using `filter()` with a `lambda` |
| `5` | Sort data | Sub-menu to sort dataset ascending or descending with `list.sort()` |
| `6` | Dataset statistics | Calls `data_statistics()` — returns a tuple of 4 computed stats |
| `7` | Exit | Breaks the main loop and terminates the program gracefully |

### Sort sub-menu (option 5)

| Option | Action |
|--------|--------|
| `1` | Sort ascending — `all_data.sort()` |
| `2` | Sort descending — `all_data.sort(reverse=True)` |
| `3` | Exit sort menu |

---

## 🔧 Functions Defined

### `factorial(num)` — Recursive
```python
def factorial(num):
    if num == 0:
        return 0
    return num * factorial(num - 1)
```
Recursively computes n! — base case returns `0` when `num == 0`.

### `data_statistics(list)` — Returns tuple
```python
def data_statistics(list):
    min_value = min(list)
    max_value = max(list)
    total_sum = sum(list)
    average_value = sum(list) / len(list)
    return min_value, max_value, total_sum, average_value
```
Returns `(min, max, sum, average)` as a tuple — accessed by index from the result.

---

## 🛠️ Built-in Tools Used

| Tool | Type | Used for |
|------|------|----------|
| `min()`, `max()` | built-in | Finding smallest and largest value |
| `sum()` | built-in | Total of all elements |
| `len()` | built-in | Count of elements |
| `filter()` | functional | Filtering values above threshold |
| `lambda x: x > threshold` | lambda | Anonymous predicate passed to `filter()` |
| `list.sort()`, `sort(reverse=True)` | built-in | In-place ascending and descending sort |
| `str.split(" ")` | built-in | Parsing space-separated input into a list |

---

## ✅ Requirements

- **Python 3.10 or above** — required for `match/case` syntax
- No third-party libraries — standard library only
- A terminal or command prompt

---

## 🚀 Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/raj-jivani/functional-treat.git

# 2. Navigate into the project folder
cd functional-treat

# 3. Run the script
python functional-treat.py
```

---

## ⚙️ How It Works

1. **Dataset initialized** — `all_data = []` is a global list that accumulates all input across sessions
2. **Input parsed (option 1)** — Space-separated string is split, each token cast to `int`, appended to `all_data` via a loop
3. **Factorial computed (option 3)** — A recursive `factorial(num)` is defined and called inline — base case returns `0` at `num == 0`
4. **Filter applied (option 4)** — `filter(lambda x: x > threshold, all_data)` returns an iterator; wrapped in `list()` for display
5. **Sort sub-menu (option 5)** — Nested `while True` loop offers ascending or descending in-place sort
6. **Statistics returned as tuple (option 6)** — `data_statistics()` returns `(min, max, sum, average)` — accessed by index

---

## 🖥️ Sample Session

```
Welcome to the Data Analyzer and Transformer programme
Main Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display dataset Statistics
7. Exit Programme

Enter your choice: 1
Enter data for 1D array (separated by space): 10 25 3 47 8 16
data added successfully

Enter your choice: 2
Data Summary:
- Total Elements: 6
- Minimum value: 3
- Maximum value: 47
- Sum of all value: 109
- Average value: 18.166666666666668

Enter your choice: 4
Enter a threshold value to filter out data above this value: 15
Filtered Data (values > 15): [25, 47, 16]
```

---

## 📁 Project Structure

```
functional-treat/
│
├── functional-treat.py    # Main script — all logic and functions
└── README.md              # Project documentation
```

---

## 📚 Concepts Covered

- **Recursion** — `factorial()` calls itself until base case is reached
- **`filter()` function** — Higher-order function for data filtering
- **Lambda expressions** — Anonymous predicate `lambda x: x > threshold`
- **`match/case`** — Python 3.10+ structural pattern matching
- **`while True` loops** — Main loop and sort sub-menu
- **`list.sort()`** — In-place ascending and descending sort
- **`def` functions** — Named reusable functions returning tuples
- **Tuple return values** — Multiple stats returned and accessed by index
- **Built-ins** — `min()`, `max()`, `sum()`, `len()`
- **`str.split()`** — Parsing user input into a list
- **Type casting** — `int()` conversion from string tokens
- **f-strings** — Formatted output throughout the program

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ as a Python functional programming practice project &nbsp;·&nbsp; © 2026 raj-jivani

</div>
