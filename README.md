# Interactive Data Visualization Dashboard

A full-stack data analytics platform that transforms raw CSV datasets into interactive dashboards, visual insights, and downloadable PDF reports.

The application allows users to upload datasets, automatically clean and process the data, explore KPIs and visualizations, identify trends, and export analytical reports.

---

## Overview

The Interactive Data Visualization Dashboard is designed to simplify exploratory data analysis through a web-based interface.

Users can upload CSV datasets and the application handles data cleaning, validation, analysis, visualization, and report generation through an integrated workflow.

---

## Key Features

- User registration and secure login
- Session-based authentication
- CSV dataset upload
- Automatic data cleaning and validation
- Missing-value handling
- Dynamic KPI generation
- Interactive data visualizations
- Real-time filtering
- Automated statistical insights
- Trend identification
- Dashboard report generation
- PDF export

---

## Technology Stack

| Category | Technologies |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask |
| Database | MySQL |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| PDF Generation | ReportLab, Kaleido |
| Authentication | Flask-Login, Werkzeug |
| Version Control | Git, GitHub |

---

## System Architecture

```text
                    User
                     │
                     ▼
             ┌─────────────────┐
             │    Frontend     │
             │ HTML/CSS/JS     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Flask Backend   │
             └────────┬────────┘
                      │
       ┌──────────────┼──────────────┐
       │              │              │
       ▼              ▼              ▼
 Authentication   Data Processing   Visualization
       │              │              │
       └──────────────┼──────────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  MySQL Database │
             └─────────────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ PDF Report      │
             │ Generation      │
             └─────────────────┘
