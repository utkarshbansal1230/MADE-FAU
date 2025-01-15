# Impact of PM2.5 Concentration on Respiratory Hospitalizations in New York City

## Overview
This project explores the relationship between PM2.5 concentrations in the atmosphere and respiratory hospitalizations across neighborhoods in New York City. By combining air quality data with hospitalization records, the study aims to identify trends, assess the impact of air pollution on public health, and uncover disparities that require targeted interventions. The findings emphasize the importance of addressing environmental and systemic factors to improve respiratory health outcomes.

## Datasets Used

### 1. Air Quality Data
- **Source:** NYC Open Data
- **URL:** [Air Quality Data](https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r/)
- **Description:** Provides detailed measurements of PM2.5 levels across various locations in New York City, disaggregated by UHF-42, time period, and pollutant type.
- **Format:** CSV
- **Quality:** Verified for consistency and cleaned for analysis.
- **Licensing:** Publicly accessible for research and analysis. Attribution to the NYC Department of Health and Mental Hygiene is required. Details available [here](https://opendata.cityofnewyork.us/overview/).

### 2. Hospitalization Data
- **Source:** NYC Environmental Public Health Data Explorer
- **URL:** [Hospitalization Data](https://a816-dohbesp.nyc.gov/IndicatorPublic/data-explorer/health-impacts-of-air-pollution/?id=2119#display=summary)
- **Description:** Contains data on hospitalizations caused by air pollution, including PM2.5 exposure, categorized by UHF-42 neighborhoods and time periods.
- **Format:** Structured for demographic and temporal analysis.
- **Licensing:** Licensed under Apache License Version 2.0. Details available [here](https://github.com/nychealth/EH-dataportal?tab=Apache-2.0-1-ov-file).

## Methodology

### 1. Data Cleaning and Preparation
- **Air Quality Data:** 
  - Removed missing values and irrelevant columns (e.g., “messages”).
  - Retained only PM2.5 data and stored the cleaned dataset in a database.
- **Hospitalization Data:**
  - Already pre-cleaned; stored directly in the database.

### 2. Aggregation and Joining
- Aggregated air quality data into multi-year time periods (e.g., 2009–2011) to align with hospitalization data.
- Calculated PM2.5 averages for each UHF-42 region.
- Joined air quality and hospitalization datasets using UHF-42 regions and time periods as keys.

## Key Insights
- **Decline in Hospitalizations:** Significant reduction in respiratory hospitalizations over time, primarily driven by decreased PM2.5 levels.
- **Disparities:** Cluster analysis revealed neighborhoods with high pollution but low hospitalization rates, suggesting gaps in healthcare access or underreporting.
- **Unexplained Variation:** With an \(R^2 = 0.29\), the relationship between PM2.5 and hospitalizations is only partially explained by air pollution, indicating a need to consider additional factors like demographics, healthcare infrastructure, and pre-existing conditions.

## Future Work
- Investigate additional variables influencing respiratory hospitalizations, such as age distribution, socioeconomic status, and healthcare access.
- Develop targeted interventions for neighborhoods with identified disparities.
- Explore the long-term effects of sustained air quality improvements on public health.

## Licensing and Attribution
- This study utilizes publicly available datasets licensed under respective agreements.
- Air Quality Data: NYC Open Data ([License Details](https://opendata.cityofnewyork.us/overview/)).
- Hospitalization Data: NYC Environmental Public Health Data Explorer ([License Details](https://github.com/nychealth/EH-dataportal?tab=Apache-2.0-1-ov-file)).