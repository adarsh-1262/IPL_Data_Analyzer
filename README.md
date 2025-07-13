# 🏏 IPL Data Analyzer – CLI Project

A terminal-based Python application to analyze IPL (Indian Premier League) data. This tool helps you explore batting performances and team stats through real-time data summaries and visual charts.

![Banner](https://img.shields.io/badge/Project-IPL%20Analyzer-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=flat-square) ![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📌 Features

✨ Built using **Python, Pandas, Matplotlib**
✨ CLI-based menu with real-time stats
✨ Exports result to CSV
✨ Visualizes data using bar charts
✨ Clean and modular code structure

---

## 📂 Folder Structure

```
IPL_Data_Analyzer/
├── data/                   # Contains IPL CSV datasets
│   ├── deliveries_2008-2024.csv
│   └── matches_2008-2024.csv
├── analysis/               # All logic separated into modules
│   ├── batting.py
│   ├── teams.py
│   └── visualize.py
├── main.py                 # Main CLI entrypoint
├── utils.py                # Data loading & export functions
├── requirements.txt        # Python packages
└── README.md               # You're reading it!
```

---

## 💥 How It Works

Run the application:

```bash
python main.py
```

Choose from the options:

```
📊 IPL Data Analyzer
1. Top Run Scorers
2. Top Six Hitters
3. Top Teams by Wins
4. Exit
```

Each option will:

* ✅ Display the results in the terminal
* 📁 Export a `.csv` file
* 📊 Show a bar chart using matplotlib

---

## 📸 Sample Visuals

> Add your screenshots below (replace these placeholder texts with your own screenshots)

### 🔝 Top 10 Run Scorers

![Top Scorers Graph](screenshots/top_scorers.png)

### 💥 Most Sixes by Batsmen

![Most Sixes Graph](screenshots/most_sixes.png)

### 🏆 Top Winning Teams

![Top Teams Graph](screenshots/top_teams.png)

---

## 📦 Installation & Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/IPL_Data_Analyzer.git
   cd IPL_Data_Analyzer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure your data is in the `/data` folder:

   * `deliveries_2008-2024.csv`
   * `matches_2008-2024.csv`

4. Run:

   ```bash
   python main.py
   ```

---

## 🧰 Tech Stack

* Python 🐍
* Pandas 📊
* Matplotlib 📈

---

## 🧠 What I Learned

* Working with real-world CSV data
* Data aggregation with `groupby`
* Building modular and reusable Python code
* CLI-based user interaction
* Visualizing insights from data
* Exporting clean CSV files from Python

---

## 💡 Future Ideas

* Add player vs player analysis
* Build a Streamlit or Tkinter GUI version
* Add a prediction model (coming next in Phase 2!)
* Use Seaborn for advanced plots

---

## 🧑‍💻 Author

**Adarsh Singh** – [LinkedIn](https://www.linkedin.com/in/adarsh-cse/)
Full Stack Engineer | Passionate about AI, Data & Cricket 🏏

---

## 📜 License

This project is licensed under the MIT License.
# IPL_Data_Analyzer
