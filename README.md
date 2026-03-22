# 🔐 Cloud Compliance Readiness Toolkit

A portfolio-ready **FastAPI + Streamlit** application designed to simulate how organisations assess cloud compliance readiness across frameworks such as **SOC 2, ISO/IEC 27001, and PCI DSS**.
---

> A full-stack GRC platform for modelling cloud compliance readiness across SOC 2, ISO 27001, and PCI DSS.

---
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Status](https://img.shields.io/badge/Status-Portfolio_Project-orange)
---
## 🚀 Live Demo
Run locally to explore full functionality

Frontend Dashboard:
http://localhost:8501

API Docs:
http://127.0.0.1:8000/docs
---

## 🚀 Overview

This toolkit models the full lifecycle of a cloud compliance assessment, including:

- Control implementation tracking  
- Evidence collection  
- Risk identification (findings)  
- Remediation task management  
- Readiness scoring and dashboard reporting  
- Cross-framework control mapping  
- PDF report generation  

The goal is to demonstrate practical understanding of **GRC (Governance, Risk & Compliance)** workflows used in real-world cyber assurance engagements.

---
## 🧱 Architecture
![Architecture Diagram](docs/screenshots/architecture.png)
---
## ❗ Problem Statement

Cloud compliance assessments are often:
- Manual and spreadsheet-driven  
- Difficult to track across multiple frameworks  
- Lacking clear visibility into readiness and risk  

This toolkit provides a structured, API-driven approach to:
- Model control implementation  
- Track evidence and findings  
- Manage remediation workflows  
- Quantify compliance readiness  

It bridges the gap between **technical controls** and **business-level risk visibility**.
---

## 🏢 Use Case

A SaaS company preparing for SOC 2 or ISO 27001 certification can use this toolkit to:

- Track control implementation status
- Collect and manage audit evidence
- Identify security gaps and risks
- Assign remediation tasks to teams
- Monitor readiness through dashboards
- Generate stakeholder-ready reports
---

## ⭐ Key Highlights

- Full-stack GRC platform (backend + frontend + reporting)
- Models real-world compliance workflows (SOC 2, ISO 27001, PCI DSS)
- Demonstrates control lifecycle, risk tracking, and remediation
- Includes dashboard visualisation and PDF export
- Designed to reflect real cyber assurance engagements
---

### 🔹 Project-Based Assessments
Create and manage compliance readiness assessments for SaaS or cloud environments.

### 🔹 Control Lifecycle Management
Track controls through:
- Not Started  
- In Progress  
- Implemented  
- Validated  
- Gap Identified

---
### 🔹 Evidence Tracking
Attach and manage audit evidence such as:
- Cloud configuration exports  
- Screenshots  
- System logs  

### 🔹 Findings & Risk Management
Identify and classify risks by severity:
- Low / Medium / High / Critical  

### 🔹 Remediation Workflow
Assign and track remediation tasks with:
- Priority  
- Ownership  
- Status  

### 🔹 Dashboard Reporting
Visualise:
- Readiness percentage  
- Control status breakdown  
- Risk distribution  
- Open remediation workload  

### 🔹 Cross-Framework Mapping
Map controls across:
- SOC 2  
- ISO/IEC 27001  
- PCI DSS  

### 🔹 PDF Report Export
Generate consultant-style readiness reports for stakeholders.

---

## 🖥️ Frontend Dashboard (Streamlit)

Interactive dashboard for:
- Viewing project readiness  
- Monitoring risks and remediation  
- Exploring control mappings  
- Downloading PDF reports  

---

## 🏗️ Tech Stack

| Layer        | Technology |
|-------------|------------|
| Backend API | FastAPI |
| Database    | SQLite + SQLAlchemy |
| Frontend    | Streamlit |
| Reporting   | ReportLab |
| Data Handling | Pandas |
| HTTP Client | Requests |

---

## 📂 Project Structure

```text
cloud-compliance-readiness-toolkit/
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── db.py
│   └── main.py
├── docs/
│   ├── sample-report.pdf
│   └── screenshots/
├── streamlit_app.py
├── requirements.txt
└── README.md
```
---

### 📸 Screenshots

### Dashboard
[![Dashboard](docs/screenshots/dashboard.png)](docs/screenshots/dashboard.png)

### Risk & Remediation
[![Findings](docs/screenshots/findings.png)](docs/screenshots/findings.png)

### Controls View
[![Controls](docs/screenshots/controls.png)](docs/screenshots/controls.png)

### Crosswalk Mapping
[![Crosswalk](docs/screenshots/crosswalk.png)](docs/screenshots/crosswalk.png)

### PDF Report
[![PDF](docs/screenshots/pdf.png)](docs/screenshots/pdf.png)[![PDF](docs/screenshots/pdf.png)](docs/screenshots/pdf.png)

---

## 📄 Sample Report

Download a generated readiness report:

👉 [Sample PDF Report](docs/sample-report.pdf)

---
## ⚙️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start FastAPI backend
```bash
uvicorn app.main:app --reload
```

### 3. Launch Streamlit frontend
```bash
streamlit run streamlit_app.py
```
---
## 🎯 Learning Outcomes

This project demonstrates:

Practical GRC workflow implementation
Control-based risk assessment methodology
Evidence-driven assurance
API-driven architecture design
Reporting and stakeholder communication
---
## 🚀 Future Enhancements
* AWS integration (CloudTrail, IAM, S3 checks)
* Automated evidence ingestion
* Role-based access control (RBAC)
* Multi-project analytics dashboard
* React-based frontend
---
## 🧠 Skills Demonstrated

- Governance, Risk & Compliance (GRC)
- ISO/IEC 27001 & SOC 2 control concepts
- Risk identification and remediation tracking
- API development (FastAPI)
- Data modelling with SQLAlchemy
- Dashboard development (Streamlit)
- Reporting and stakeholder communication
---


## 👤 Author

**Patrick Adefowora**  
Cyber Risk & Assurance Analyst | ISO/IEC 27001 | SOC 2 | Cloud Security  

🔗 LinkedIn: https://www.linkedin.com/in/patrickadefowora/
