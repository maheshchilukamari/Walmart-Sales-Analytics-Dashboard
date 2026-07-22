# Walmart Sales Analytics Dashboard

![Python](https://img.shields.io/badge/Python-Data%20Analytics-3776AB?logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-Interactive%20Dashboard-008DE5)
![Plotly](https://img.shields.io/badge/Plotly-Data%20Visualization-3F4F75?logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7?logo=render&logoColor=black)

An interactive retail analytics dashboard built with **Python, Pandas, Plotly, Dash, and Dash Bootstrap Components** to analyze Walmart weekly sales, store performance, holiday trends, temperature patterns, and economic indicators.

## Live Dashboard

### [Open the Walmart Sales Analytics Dashboard](https://walmart-sales-analytics-dashboard.onrender.com/)

> The application is hosted on Render. The free hosting service may take approximately one minute to restart after a period of inactivity.

---

## Project Overview

This project transforms historical Walmart sales data into an interactive dashboard that helps users explore sales performance across stores and time periods.

The dashboard provides visual analysis of:

- Store-level weekly sales
- Holiday and non-holiday performance
- Monthly sales patterns
- Fuel price and sales relationships
- Consumer Price Index effects
- Unemployment and sales relationships
- Temperature-based sales distributions
- Store contribution to total sales
- Year-over-year and store-level performance

The project was originally developed as a graduate academic data-visualization project and has been organized, documented, and deployed as a portfolio application.

---

## Business Questions

The dashboard was designed to answer questions such as:

1. How does weekly sales performance vary across Walmart stores?
2. Which stores contribute the most to total sales?
3. How do holiday weeks affect weekly sales?
4. Are fuel prices associated with changes in sales?
5. How do CPI and unemployment relate to weekly sales?
6. How does sales performance vary across temperature ranges?
7. Which months and years show the strongest sales activity?
8. Where do major sales peaks and seasonal patterns occur?

---

## Dashboard Features

### Store-Level Sales Analysis

Users can select an individual Walmart store and view its weekly sales performance through an interactive bar chart.

### Weekly Sales Trend

The line chart displays weekly sales over time for the selected store. A holiday filter allows users to isolate holiday-week sales.

### Fuel Price vs. Weekly Sales

An interactive scatter plot compares fuel prices with weekly sales. CPI is represented through the chart's color scale.

### Monthly Sales Heatmap

The heatmap displays average monthly sales across all stores, making seasonal and store-level patterns easier to identify.

### Unemployment Impact Analysis

A bubble chart compares unemployment rates with weekly sales. Bubble size represents CPI, while color identifies the store.

### Temperature-Based Sales Distribution

A violin plot shows the distribution of weekly sales across different temperature ranges and includes summary box plots.

### Store Sales Contribution

A pie chart shows the percentage contribution of each store to total Walmart sales.

### Total Weekly Sales Trend

An area chart displays total weekly sales across all stores and highlights major increases and decreases over time.

### Year and Store Hierarchy

A sunburst chart presents sales hierarchically by year and store.

### Radial Store Comparison

A radial bar chart provides an alternative visual comparison of total sales across stores.

### Holiday and Temperature Analysis

A population-pyramid-style chart compares sales across temperature ranges and holiday categories.

---

## Dataset

The dataset contains **6,435 weekly sales records from 45 Walmart stores**, covering the period from **February 2010 through October 2012**.

### Dataset Attributes

| Column | Description |
|---|---|
| `Store` | Unique identifier for each Walmart store |
| `Date` | Date of the weekly sales record |
| `Weekly_Sales` | Total weekly sales for the store |
| `Holiday_Flag` | Indicates whether the week contains a major holiday |
| `Temperature` | Regional temperature during the recorded week |
| `Fuel_Price` | Regional fuel price |
| `CPI` | Consumer Price Index |
| `Unemployment` | Regional unemployment rate |

### Data Preparation

The application performs the following transformations:

- Converts the `Date` column into datetime format
- Creates a monthly field for monthly aggregation
- Extracts the year from each sales record
- Groups temperature values into ranges
- Aggregates sales by store, date, month, and year
- Separates holiday and non-holiday sales records

### Dataset Source

The dataset used for this academic project is available through Kaggle:

[Walmart Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/walmart-dataset/data)

The dataset remains subject to the terms and conditions of its original publisher.

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas |
| Interactive Visualization | Plotly Express |
| Web Dashboard | Dash |
| User Interface | Dash Bootstrap Components |
| Notebook Development | Jupyter Notebook |
| Production Server | Gunicorn |
| Version Control | Git and GitHub |
| Deployment | Render |

---

## Project Structure

```text
walmart-sales-analytics-dashboard/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets/
│   ├── flowchart.png
│   └── visualizations/
│       ├── holiday-sales-distribution.png
│       ├── highest-sales-weeks.png
│       └── correlation-heatmap.png
│
├── data/
│   └── Walmart.csv
│
├── docs/
│   └── Scientific-Data-Visualization-Project-Report.pdf
│
└── notebooks/
    └── walmart-dashboard.ipynb
```

---

## Running the Project Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd walmart-sales-analytics-dashboard
```

### 3. Create a virtual environment

#### Windows

```bash
py -m venv .venv
.venv\Scripts\activate
```

#### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Start the dashboard

```bash
python app.py
```

### 6. Open the local application

Open the following address in a browser:

```text
http://127.0.0.1:8050/
```

---

## Requirements

The application requires the following Python packages:

```text
dash
dash-bootstrap-components
pandas
plotly
gunicorn
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## Render Deployment

The application is deployed as a Render web service.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:server --bind 0.0.0.0:$PORT
```

The following line in `app.py` exposes the Dash application server to Gunicorn:

```python
server = app.server
```

Render automatically rebuilds and redeploys the application when new changes are pushed to the connected GitHub repository.

---

## Academic Documentation

The original class project documentation is included for academic reference:

### [View the Scientific Data Visualization Project Report](docs/Scientific-Data-Visualization-Project-Report.pdf)

The public version of the report should exclude student identification numbers and other private academic information.

---

## Academic Project Context

This dashboard was developed as a collaborative graduate academic project.

### Project Contributors

- Vishnu Vardhan Madasi
- Mahesh Chilukamari
- Uday Kiran Duvvala
- Venkata Sowmya Kancharla

The project involved data preparation, exploratory analysis, feature engineering, interactive visualization, dashboard design, analytical storytelling, and documentation.

### Portfolio Maintainer

**Mahesh Chilukamari**

My work focused on data preparation and improving the usability, visual structure, and interactive presentation of the dashboard.

---

## Static Analytical Visualizations

The academic project also includes supporting static visualizations:

- Holiday vs. non-holiday sales distribution
- Highest-performing sales weeks
- Correlation heatmap of sales and economic indicators

These visualizations are stored in:

```text
assets/visualizations/
```

---

## Key Observations

The exploratory analysis shows that:

- Weekly sales vary considerably across stores.
- Major sales peaks appear during important holiday periods.
- Holiday weeks have greater variation in sales performance.
- Some stores contribute a substantially larger share of total sales.
- Temperature, CPI, fuel prices, and unemployment provide useful economic context, although their relationships with weekly sales are not uniformly strong.
- Monthly and annual visualizations reveal recurring seasonal patterns.

These findings are exploratory and should not be interpreted as evidence of causation.

---

## Current Project Scope

The deployed application focuses on:

- Historical sales analytics
- Exploratory data analysis
- Interactive data visualization
- Store-level comparisons
- Holiday and economic-factor analysis

Although the original academic report discusses sales forecasting and possible SARIMAX, XGBoost, and LSTM models, the current deployed application does **not** include a production forecasting model.

This distinction is maintained to ensure that the GitHub repository accurately represents the available source code.

---

## Future Improvements

Potential improvements include:

- Add KPI cards for total sales, average weekly sales, and top-performing stores
- Add date-range and multi-store filters
- Implement store-level sales forecasting
- Compare SARIMAX, XGBoost, and LSTM forecasting models
- Add MAE, RMSE, MAPE, and R² evaluation results generated directly from code
- Display actual versus predicted sales
- Add downloadable filtered datasets
- Improve mobile responsiveness
- Add automated testing and data-validation checks
- Containerize the application using Docker
- Add a continuous integration and deployment workflow

---

## Repository Purpose

This repository is maintained for:

- Academic documentation
- Data analytics portfolio demonstration
- Interactive dashboard development
- Exploratory retail sales analysis
- Python and Plotly Dash practice

---


## Acknowledgments

- Walmart sales dataset contributors
- Kaggle dataset hosting
- Plotly and Dash documentation
- Academic instructors and project collaborators
