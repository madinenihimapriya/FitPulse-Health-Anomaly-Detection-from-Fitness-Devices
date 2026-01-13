# Milestone 4 – Dashboard for Insights

## Objective
The objective of Milestone 4 is to design and implement an interactive dashboard for visualizing health anomalies detected from fitness device data. The dashboard is executed in Google Colaboratory using Streamlit and ngrok, enabling users to upload data, view anomalies, and download reports.

## Dashboard Workflow
1. User uploads fitness data in CSV or JSON format through the Streamlit interface.
2. Uploaded data is preprocessed and reshaped for analysis.
3. Metric-wise anomaly detection is performed using Isolation Forest.
4. Interactive visualizations display trends and detected anomalies.
5. Users can download anomaly summary reports in CSV format.

## Tools & Libraries Used
- Google Colaboratory
- Streamlit
- ngrok
- Python
- pandas
- plotly
- scikit-learn

## Key Insights from the Dashboard
- Heart rate anomalies highlight abnormal physiological behavior.
- Sleep duration irregularities indicate poor or insufficient sleep patterns.
- Step count variations reveal changes in physical activity levels.
- Anomaly markers enable quick identification of abnormal health metrics.

## Screenshot References
- screenshots/dashboard_ui.png
- screenshots/report_download.png
