# GCP Cloud Functions – Python Integration Tests (GA4 + BigQuery)

This repository contains Python scripts and utilities for testing Google Cloud Functions integrations with **Google Analytics 4 (GA4)** and **BigQuery**.  
The goal is to provide a reusable and modular framework for extracting GA4 data, processing it in Python, and pushing it to BigQuery — using **Google Cloud Functions** as the execution environment.

## 📌 Overview

The repository demonstrates:

- **Serverless data pipelines** using **GCP Cloud Functions**.
- Pulling data directly from the **GA4 Data API**.
- Pushing processed datasets to **BigQuery** with explicit schema handling.
- Triggering workflows via **Pub/Sub** messaging.
- Optional integration with **Google Sheets** for configuration management.

## 📂 Repository Structure

| File | Purpose |
|------|---------|
| `main-job.py` | Orchestrates the execution of all other functions via Pub/Sub messages. |
| `get_metadata.py` | Pulls GA4 metadata (dimensions & metrics) into BigQuery for reference. |
| `get_geographic_acq.py` | Fetches GA4 **Geographic Acquisition** data and pushes it to BigQuery. |
| `get_traffic_acq.py` | Fetches GA4 **Traffic Acquisition** data for all configured clients. |
| `get_traffic_acq_custom.py` | Custom pull of Traffic Acquisition data for a given client and date range. |

## 🛠 Requirements

- **Python 3.9+**
- Google Cloud SDK installed & authenticated.
- Required Python packages (install via `requirements.txt`):

```bash
pip install -r requirements.txt


https://lookerstudio.google.com/reporting/3efb27ed-773b-4b6c-951c-e74f7e3ace67