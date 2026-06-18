\# Interactive Data Visualization Dashboard



A web-based data analytics platform that enables users to upload CSV datasets, automatically clean and process data, generate interactive visualizations, derive meaningful insights, and export dashboard reports in PDF format.



This project was developed as part of the Master of Computer Applications (MCA) curriculum and demonstrates the practical application of Data Analytics, Web Development, Database Management, and Data Visualization techniques.



\---



\## Overview



The Interactive Data Visualization Dashboard helps users transform raw datasets into meaningful visual reports without requiring advanced technical knowledge. Users can upload CSV files, apply filters, analyze data through dynamic charts, and generate professional PDF reports.



\---



\## Key Features



\### User Authentication

\- User Registration

\- Secure Login System

\- Session Management

\- Logout Functionality



\### Data Processing

\- CSV File Upload

\- Automatic Data Cleaning

\- Missing Value Handling

\- Data Validation



\### Data Visualization

\- Dynamic Dashboard Generation

\- Interactive Charts

\- KPI Calculations

\- Real-Time Filtering



\### Insight Generation

\- Automated Data Insights

\- Summary Statistics

\- Trend Identification

\- Data Interpretation



\### Reporting

\- PDF Report Export

\- KPI Summary

\- Dashboard Snapshot Generation



\---



\## Technology Stack



\### Frontend

\- HTML5

\- CSS3

\- JavaScript



\### Backend

\- Python

\- Flask



\### Database

\- MySQL



\### Data Analytics Libraries

\- Pandas

\- NumPy

\- Plotly



\### Reporting Tools

\- ReportLab

\- Kaleido



\### Authentication

\- Flask-Login

\- Werkzeug Security



\---



\## System Architecture



```text

User

&#x20; │

&#x20; ▼

Flask Application

&#x20; │

&#x20; ├── Authentication Module

&#x20; ├── CSV Upload Module

&#x20; ├── Data Cleaning Module

&#x20; ├── Visualization Module

&#x20; ├── Insights Engine

&#x20; └── PDF Report Generator

&#x20; │

&#x20; ▼

MySQL Database

```



\---



\## Project Structure



```text

interactive-data-visualization-dashboard/

│

├── app.py

├── README.md

├── requirements.txt

├── .gitignore

│

├── database/

│   └── schema.sql

│

├── processing/

│   ├── cleaner.py

│   ├── schema.py

│   ├── insights.py

│   └── visualizer.py

│

├── templates/

│   ├── login.html

│   ├── register.html

│   └── upload.html

│

├── static/

│

└── sample\_data.csv

```



\---



\## Installation Guide



\### Clone Repository



```bash

git clone https://github.com/YOUR\_USERNAME/interactive-data-visualization-dashboard.git

cd interactive-data-visualization-dashboard

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## Database Setup



\### Create Database



```sql

CREATE DATABASE interactive\_viz;

```



\### Create Users Table



```sql

CREATE TABLE users (

&#x20;   id INT AUTO\_INCREMENT PRIMARY KEY,

&#x20;   username VARCHAR(100),

&#x20;   email VARCHAR(100) UNIQUE,

&#x20;   password VARCHAR(255)

);

```



\### Create Dashboards Table



```sql

CREATE TABLE dashboards (

&#x20;   id INT AUTO\_INCREMENT PRIMARY KEY,

&#x20;   user\_id INT,

&#x20;   dashboard\_name VARCHAR(255),

&#x20;   filters\_json JSON,

&#x20;   data\_json LONGTEXT,

&#x20;   created\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP

);

```



\---



\## Configuration



Update database credentials in:



```python

app.py

```



```python

db = mysql.connector.connect(

&#x20;   host="localhost",

&#x20;   user="root",

&#x20;   password="YOUR\_PASSWORD",

&#x20;   database="interactive\_viz"

)

```



\---



\## Running the Application



Start the Flask server:



```bash

python app.py

```



Open your browser and navigate to:



```text

http://127.0.0.1:5000

```



\---



\## Application Workflow



1\. Register a new account

2\. Login to the system

3\. Upload a CSV dataset

4\. System cleans and processes the data

5\. Dashboard visualizations are generated

6\. Review KPIs and insights

7\. Export dashboard report as PDF



\---



\## Screenshots



\### Login Page



Add screenshot here



\### Registration Page



Add screenshot here



\### Dashboard View



Add screenshot here



\### PDF Report



Add screenshot here



\---



\## Learning Outcomes



This project demonstrates practical knowledge of:



\- Data Analytics

\- Data Visualization

\- Python Programming

\- Flask Web Development

\- Database Management Systems

\- User Authentication

\- Report Generation

\- Software Development Lifecycle



\---



\## Future Enhancements



\- Power BI Integration

\- Machine Learning Based Predictions

\- Advanced Filtering Options

\- Cloud Deployment

\- User Profile Management

\- Multiple Dataset Support

\- Real-Time Analytics



\---



\## Author



\### Yash Kothule



Master of Computer Applications (MCA)  

Savitribai Phule Pune University (SPPU)



\### Connect With Me



LinkedIn:

https://www.linkedin.com/in/yash-kothule-6b251b411/



GitHub:

https://github.com/yashkothule



\---



\## License



This project is developed for academic, learning, and educational purposes.

