# Project Plan

## Title
**Impact of PM2.5 Concentration in atmosphere on Respiratory Hospitalizations in the United States**

## Main Question
How does the increase in PM2.5 levels affect the number of respiratory-related hospitalizations in the United States?

## Description
The impact of air pollution, specifically fine particulate matter (PM2.5), on public health is a significant concern in urban areas across the United States. This project aims to analyze the relationship between elevated PM2.5 concentrations and the rate of hospitalizations due to respiratory diseases. By studying air quality data alongside health statistics, the project seeks to provide insights into how poor air quality directly impacts public health, particularly in terms of respiratory conditions. The findings could contribute to informing policies aimed at reducing air pollution and improving public health.

## Data Sources

1. **Respiratory Hospitalizations due to PM2.5 (age 20+)**
   - **Datasource Name**: New York City Department of Health and Mental Hygiene (DOHMH)
   - **Data URL**: (https://a816-dohbesp.nyc.gov/IndicatorPublic/data-explorer/health-impacts-of-air-pollution/?id=2119#display=summary)
   - **Data Type**: CSV
   - **Description**: This dataset provides statistics on hospital admissions related to respiratory diseases. It includes hospitalization data by region, which can be correlated with air quality data to understand health trends.

2. ** Daily Mean PM2.5 Concentration and the AQI level**
   - **Datasource Name**: EPA United States Environmental Protection Agency
   - **Metadata URL**: (https://www.epa.gov/outdoor-air-quality-data/download-daily-data)
   - **Data URL**: [CDC Respiratory Disease Data](https://www3.epa.gov/cgi-bin/broker?_service=data&_server=134.67.99.91&_port=4072&_sessionid=cBmqwRlTS52&_PROGRAM=dataprog.ad_viz_plotval_getdata.sas)
   - **Data Type**: CSV
   - **Description**: This dataset provides daily air quality summary statistics for PM2.5

## Work Packages

### Work Package 1: **Data Collection**
   - Collect the PM2.5 air quality data for various U.S. cities.
   - Download hospitalization data for respiratory diseases.
   - Ensure that the data covers overlapping time periods to correlate air quality with hospitalization rates.

### Work Package 2: **Data Cleaning and Preprocessing**
   - Clean the datasets by handling missing values, duplicates, and inconsistencies.
   - Format the data to ensure compatibility between the two datasets (e.g., aligning the time frames and locations).
   - Perform exploratory data analysis (EDA) to identify trends and anomalies in the data.

### Work Package 3: **Statistical Analysis**
   - Conduct correlation and regression analysis to examine the relationship between PM2.5 levels and hospitalization rates.
   - Use visualization tools (e.g., histograms, scatter plots) to explore the data and highlight any significant trends.
   - Interpret the statistical findings to assess whether increases in PM2.5 concentrations lead to higher hospitalization rates for respiratory diseases.