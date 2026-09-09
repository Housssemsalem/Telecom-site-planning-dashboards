# Telecom Site Planning & BI Dashboards

A portfolio of **telecom network planning, monitoring, data quality and business intelligence dashboards** developed during my internship in the mobile network domain.

> **Confidentiality notice**
>
> The original internship work used internal SFR/Bouygues Telecom data and environments. This repository contains only **sanitized, non-confidential material** intended to demonstrate the methodology, technical approach and dashboard design. No proprietary datasets, credentials, internal identifiers or confidential business information are included.

## About the project

The project focused on transforming telecom operational data into reliable datasets, automated monitoring processes and decision-ready dashboards.

The work covered:

- ETL and data preparation
- Historical data loading and change monitoring
- Data Quality controls and KPI validation
- Telecom site and cell analysis
- 4G / 5G monitoring
- Network-sharing / operational monitoring use cases
- Interactive BI dashboards and geographic analysis

## Technology stack

| Area | Technologies |
|---|---|
| Data engineering | Python, SQL, PostgreSQL, ETL |
| Data integration | Talend, SSIS, SFTP |
| Data quality | Validation rules, KPI controls, monitoring |
| BI & visualization | Tableau, Power BI |
| Development | Python, Git, VS Code |
| Geospatial | PostGIS / geographic analysis |

## Repository structure

```text
Telecom-site-planning-dashboards/
├── README.md
├── dashboards/
│   ├── dashboard-01/
│   ├── dashboard-02/
│   ├── dashboard-03/
│   ├── dashboard-04/
│   ├── dashboard-05/
│   ├── dashboard-06/
│   └── dashboard-07/
├── data-model/
│   ├── data-model.png
│   └── README.md
├── monitoring-etl/
│   ├── monitoring_example.py
│   ├── README.md
│   └── examples/
└── assets/
    ├── architecture.png
    └── workflow.png
```

## Dashboards

### 01 — Plancell / Site Planning Monitoring

Monitoring view dedicated to telecom sites and planning information, including operational indicators and data-quality-oriented checks.

**Public dashboard:** `ADD_PUBLIC_LINK_HERE`

![Dashboard 01](dashboards/dashboard-01/dashboard.png)

---

### 02 — Synthèse SFR 4G / 5G

Executive monitoring of 4G and 5G network information with date-based KPI analysis and historical evolution.

**Public dashboard:** `ADD_PUBLIC_LINK_HERE`

![Dashboard 02](dashboards/dashboard-02/dashboard.png)

---

### 03 — STI OA SFR

Geographic and operational analysis of SFR sites associated with shared network zones and operational areas.

**Public dashboard:** `ADD_PUBLIC_LINK_HERE`

![Dashboard 03](dashboards/dashboard-03/dashboard.png)

---

### 04 — STI OA BYT

Complementary view focused on Bouygues Telecom-related operational areas and shared network analysis.

**Public dashboard:** `ADD_PUBLIC_LINK_HERE`

![Dashboard 04](dashboards/dashboard-04/dashboard.png)

---

### 05 — Network Monitoring

Monitoring of operational network indicators, site status and historical KPI evolution.

**Public dashboard:** `ADD_PUBLIC_LINK_HERE`

![Dashboard 05](dashboards/dashboard-05/dashboard.png)

---

### 06 — Data Quality Monitoring

A dedicated view for identifying missing, inconsistent or unexpected values and supporting data reliability.

**Public dashboard:** `ADD_PUBLIC_LINK_HERE`

![Dashboard 06](dashboards/dashboard-06/dashboard.png)

---

### 07 — Operational KPI Overview

Consolidated KPI view designed to provide a high-level understanding of network and planning activity.

**Public dashboard:** `ADD_PUBLIC_LINK_HERE`

![Dashboard 07](dashboards/dashboard-07/dashboard.png)

## Data model

The original solution relied on structured telecom datasets connected through an ETL and reporting architecture. The diagram below is a **sanitized representation** of the data model and processing flow.

![Sanitized data model](data-model/data-model.png)

### High-level flow

```text
Source systems
     ↓
Data extraction / SFTP
     ↓
ETL & transformation
     ↓
PostgreSQL data layer
     ↓
Monitoring & Data Quality
     ↓
Tableau / Power BI dashboards
```

## Non-confidential monitoring example

The repository can include sanitized Python examples showing the general logic used to:

- compare the latest batch with the previous batch,
- calculate KPI variations,
- detect changes,
- validate required fields,
- log execution results.

The example code intentionally uses **synthetic/public-safe data structures** and does not reproduce proprietary queries, credentials, internal table names or business rules.

See [`monitoring-etl/monitoring_example.py`](monitoring-etl/monitoring_example.py).

## What this project demonstrates

This portfolio is intended to demonstrate my ability to work across the full data-to-insight chain:

**Extract → Transform → Validate → Monitor → Visualize → Communicate**

It reflects my strongest areas in **Data Engineering, Data Quality, SQL, Python, ETL and Business Intelligence**.

## Professional context

Developed as part of a telecom data internship involving mobile network planning, 4G/5G data and operational monitoring.

All screenshots, links and examples published here should be understood as **portfolio representations** unless explicitly identified as public dashboards.

## Author

**Houssem Salem**  
Data Engineer | Data Analytics | Business Intelligence

[GitHub](https://github.com/Housssemsalem) · [LinkedIn](https://www.linkedin.com/)
