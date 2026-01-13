# Milestone 3: Anomaly Detection and Visualization

## Objective
The objective of Milestone 3 is to identify, label, and visualize anomalies in fitness-related data obtained from wearable devices. The focus is on detecting abnormal heart rate and sleep patterns using statistical methods and presenting the results through clear visualizations to support health monitoring and anomaly interpretation.

---

## Dataset Description
The dataset contains fitness-related attributes such as:
- Energy (used as a proxy for heart rate)
- Duration_ms (used as a proxy for sleep duration)
- Other audio/fitness-related features

Since direct physiological signals (heart rate, sleep hours) were not explicitly available, suitable proxy features were selected based on domain relevance.

---

## Steps Followed

### 1. Residual / Threshold-Based Analysis
- Statistical thresholding was applied using quantiles.
- Extreme low and high values (below 5th percentile and above 95th percentile) were considered potential anomalies.
- Energy values represent abnormal heart rate patterns.
- Duration_ms values represent abnormal sleep duration patterns.

---

### 2. Anomaly Identification
- Data points violating defined thresholds were flagged as anomalies.
- Normal observations were labeled as `1`.
- Anomalous observations were labeled as `-1`.
- A new column `anomaly` was added to the dataset for clarity.

---

### 3. Anomaly Labeling
- All records were clearly categorized as either:
  - Normal (`anomaly = 1`)
  - Anomalous (`anomaly = -1`)
- This labeling enabled easy separation for visualization and analysis.

---

### 4. Visualization of Anomalies
Two primary visualizations were created:

#### a) Heart Rate Anomaly Visualization
- Time-series plot using the `energy` feature.
- Normal points plotted as a continuous line.
- Anomalies highlighted using scatter points.
- Saved as:  
  `visualizations/heart_rate_anomalies.png`

#### b) Sleep Pattern Anomaly Visualization
- Time-series plot using the `duration_ms` feature.
- Abnormal sleep durations highlighted clearly.
- Saved as:  
  `visualizations/sleep_anomalies.png`

---

## Tools and Technologies Used
- **Google Colaboratory (Python)**
- **Pandas** – data manipulation
- **Matplotlib** – visualization
- **NumPy** – numerical operations
- **GitHub** – version control and project submission

---

## Key Insights
- Extreme energy levels indicate possible abnormal heart rate behavior.
- Very short or very long durations suggest irregular sleep patterns.
- Threshold-based anomaly detection is effective when domain limits are well-defined.
- Visualizations make anomaly patterns easy to interpret for non-technical users.

---

## Outputs
- Heart Rate Time-Series with anomalies highlighted
- Sleep Pattern Time-Series with abnormal segments highlighted
- Well-documented Jupyter Notebook (`anomaly_detection.ipynb`)

---

## Conclusion
This milestone successfully demonstrates anomaly detection and visualization techniques applied to fitness data. The results provide meaningful insights into abnormal behavioral patterns and form a strong foundation for further health analytics and alert systems.
